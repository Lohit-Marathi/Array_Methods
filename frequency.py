class FrequencyCounter:
    def __init__(self, array):
        self.array = array

    def count_frequencies(self):
        frequency_dict = {}
        for item in self.array:
            if item in frequency_dict:
                frequency_dict[item] += 1
            else:
                frequency_dict[item] = 1
        return frequency_dict
# Example usage:
counter = FrequencyCounter([1, 2, 2, 3, 3, 3])
print(counter.count_frequencies())  # Output: {1: 1, 2: 2, 3: 3}