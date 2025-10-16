class Frequency1:
    def __init__(self, array, item):
        self.array = array
        self.item = item

    def count_frequencies(self):
        # Use the built-in list.count() method for a more concise solution.
        return self.array.count(self.item)

counter = Frequency1([1, 2, 2, 3], 2)
a = counter.count_frequencies()
print(a)
