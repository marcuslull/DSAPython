class OpenAddressingBucket:

    def __init__(self, bucket_key=None, bucket_value=None):
        self.key = bucket_key
        self.value = bucket_value
        print("9.bucket instantiated")

    def is_empty(self):
        print("6.checking to see if the bucket is empty...")
        if self is OpenAddressingBucket.EMPTY_SINCE_START:
            print("7.Found EMPTY_SINCE_START, returning true")
            return True
        return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL


OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()


class OpenAddressingHashTable:

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
        print("1.5,4.computed hash_key:", abs(hash(key)))
        return abs(hash(key))

    def probe(self, key, i):
        return (self.hash_key(key) + i) % len(self.table)

    def insert(self, key, value):
        print("1.starting insert")
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)

            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                print("2.found EMPTY_SINCE_START - breaking")
                break

            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                if key == self.table[bucket_index].key:
                    print("2.found duplicate key updating value - returning true")
                    self.table[bucket_index].value = value
                    return True

        for i in range(len(self.table)):
            print("3.probing...")
            bucket_index = self.probe(key, i)
            print("5.Probing bucket:", bucket_index)
            if self.table[bucket_index].is_empty():
                print("8.Instantiating bucket")
                self.table[bucket_index] = OpenAddressingBucket(key, value)
                print("10.returning true - done!")
                return True
            print("*****COLLISION ON ITERATION:", i)

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
