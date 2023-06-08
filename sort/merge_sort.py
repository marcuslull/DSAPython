class MergeSort:
    def __init__(self, unordered_list):
        self.unordered_list = unordered_list

    def merge(self, start, mid, end):

        """The merge helper merges the sub-containers in order"""

        merged_size = end - start + 1
        merged_numbers = [0] * merged_size
        merge_position = 0
        left_position = start
        right_position = mid + 1

        while left_position <= mid and right_position <= end:
            if self.unordered_list[left_position] <= self.unordered_list[right_position]:
                merged_numbers[merge_position] = self.unordered_list[left_position]
                left_position += 1
            else:
                merged_numbers[merge_position] = self.unordered_list[right_position]
                right_position += 1
            merge_position += 1

        while left_position <= mid:
            merged_numbers[merge_position] = self.unordered_list[left_position]
            left_position += 1
            merge_position += 1

        while right_position <= end:
            merged_numbers[merge_position] = self.unordered_list[right_position]
            right_position += 1
            merge_position += 1

        for merge_position in range(merged_size):
            self.unordered_list[start + merge_position] = merged_numbers[merge_position]

    def sort(self, start_index, end_index):

        """Merge sort divides the unordered container and its subsequent sub-containers into halves recursively sorting
         them before merging them back in sorted order."""

        if start_index < end_index:
            mid_index = (start_index + end_index) // 2
            self.sort(start_index, mid_index)
            self.sort(mid_index + 1, end_index)
            self.merge(start_index, mid_index, end_index)
