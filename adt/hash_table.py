class OpenAddressingBucket:

    """Helper class to create placeholder buckets and determine index availability"""

    def __init__(self, bucket_key=None, bucket_value=None):
        self.key = bucket_key
        self.value = bucket_value

    def is_empty(self):

        if self is OpenAddressingBucket.EMPTY_SINCE_START:

            return True

        return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL


# placeholder buckets to fill out the entire container
OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()


class OpenAddressingHashTable:

    """This implementation uses open addressing with a linear probing approach to map key/value pairs to a
    given index."""

    def __init__(self, initial_capacity=11):
        self.table = [OpenAddressingBucket.EMPTY_SINCE_START] * initial_capacity

    def __str__(self):
        out = ""

        for i in range(len(self.table)):

            if self.table[i] is OpenAddressingBucket.EMPTY_SINCE_START:
                out += "EMPTY_SINCE_START\n"

            elif self.table[i] is OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                out += "EMPTY_AFTER_REMOVAL\n"

            else:
                out += "%s, %s\n" % (self.table[i].key, self.table[i].value)

        return out

    def hash_key(self, key):

        return abs(hash(key))

    def probe(self, key, i):

        return (self.hash_key(key) + i) % len(self.table)

    def insert(self, key, value):

        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)

            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                break

            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:

                if key == self.table[bucket_index].key:
                    self.table[bucket_index].value = value

                    return True

        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)

            if self.table[bucket_index].is_empty():
                self.table[bucket_index] = OpenAddressingBucket(key, value)

                return True

        return False

    def remove(self, key):

        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)

            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                return False

            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                if key == self.table[bucket_index].key:
                    self.table[bucket_index] = OpenAddressingBucket.EMPTY_AFTER_REMOVAL
                    return True

        return False

    def search(self, key):

        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)

            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                return None

            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                if key == self.table[bucket_index].key:
                    return self.table[bucket_index].value

        return None
