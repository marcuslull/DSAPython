class RadixSort:

    def __init__(self, unordered_container_of_ints):
        self.unordered_container_of_ints = unordered_container_of_ints

    def get_max_length(self):

        """Helper gets the max number of digits of any number in the unordered container"""

        max_digits = 0
        for number in self.unordered_container_of_ints:
            digit_count = self.get_length(number)
            if digit_count > max_digits:
                max_digits = digit_count

        return max_digits

    def get_length(self, number):

        """Helper gets the number of digits for a given number"""

        if number == 0:
            return 1

        digits = 0
        while number != 0:
            digits += 1
            number = int(number / 10)

        return digits

    def sort(self):

        """Radix sort uses buckets to separate an unordered container of integers by significant digit."""

        buckets = []
        for i in range(10):
            buckets.append([])

        max_digits = self.get_max_length()

        powers_of_ten = 1
        for digit_index in range(max_digits):
            for num in self.unordered_container_of_ints:
                bucket_index = (abs(num) // powers_of_ten) % 10
                buckets[bucket_index].append(num)

            self.unordered_container_of_ints.clear()
            for bucket in buckets:
                self.unordered_container_of_ints.extend(bucket)
                bucket.clear()

            powers_of_ten *= 10

        negatives = []
        non_negatives = []
        for num in self.unordered_container_of_ints:
            if num < 0:
                negatives.append(num)
            else:
                non_negatives.append(num)

        negatives.reverse()
        self.unordered_container_of_ints.clear()
        self.unordered_container_of_ints.extend(negatives + non_negatives)
