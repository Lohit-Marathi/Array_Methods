# class FrequencyCounter:
#     def __init__(self, array):
#         self.array = array

#     def count_frequencies(self):
#         frequency_dict = {}
#         for item in self.array:
#             if item in frequency_dict:
#                 frequency_dict[item] += 1
#             else:
#                 frequency_dict[item] = 1
#         return frequency_dict
# # Example usage:
# counter = FrequencyCounter([1, 2, 2, 3, 3, 3])
# print(counter.count_frequencies())  # Output: {1: 1, 2: 2, 3: 3}
"""
Optimized solution to find students with the second-lowest score.
Prints only the names in alphabetical order - nothing else.
"""

if __name__ == '__main__':
    # Read number of students
    n = int(input())
    
    # Collect all student data in one pass
    students = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append((name, score))
    
    # Get unique scores sorted in ascending order
    unique_scores = sorted(set(score for name, score in students))
    
    # Get the second-lowest score
    second_lowest = unique_scores[1]
    
    # Get all students with second-lowest score, sorted alphabetically
    result = sorted(name for name, score in students if score == second_lowest)
    
    # Print each name on a new line
    for name in result:
        print(name)