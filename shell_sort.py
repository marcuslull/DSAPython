class ShellSort:

    def __init__(self, unordered_container, gap_values):
        self.unordered_container = unordered_container
        self.gap_values = gap_values

    def sort(self):

        """Shell sort utilizes the insertion sort strategy but makes use of a gaping technique to reduce the overall
        comparisons. Sort method calls the insertion_sort_interleaved method using the different gap sizes."""

        for gap_value in self.gap_values:
            for i in range(gap_value):
                self.insertion_sort_interleaved(i, gap_value)

        return self.unordered_container

    def insertion_sort_interleaved(self, start_index, gap):

        """A variation of the insertion sort algorithm using gaps."""

        for i in range(start_index + gap, len(self.unordered_container), gap):
            j = i
            while (j - gap >= start_index) and (self.unordered_container[j] < self.unordered_container[j - gap]):
                temp = self.unordered_container[j]
                self.unordered_container[j] = self.unordered_container[j - gap]
                self.unordered_container[j - gap] = temp
                j = j - gap

