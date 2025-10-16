class Frequency2:
    def __init__(self, array, item):
        self.array = array
        self.item = item


    def count_frequencies(self):
        # Use a loop to count occurrences of the specified item.
        return self.array.count(self.item)
    
    def count_all_frequencies(self):
        frequency_dict = {}
        for ele in self.array:
            frequency_dict[ele] = frequency_dict.get(ele, 0) + 1

        return frequency_dict
    
def get_user_input():
    """Get array size and elements from the user."""
    while True:
        try:
            size = int(input("Enter the size of the array: "))
            if size <= 0:
                print("Size should be a positive integer.please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive intefger.")
            

    array = []
    print(f"Enter {size} elements:")
    for i in range(size):
        while True:
            try:
                num = int(input(f"Element {i + 1}: "))
                array.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return array
    

def main():
    print("=====Array Frequency Counter=====")
    array = get_user_input()
    print(f"Your Array: {array}")

    freq_obj = Frequency2(array,None)


    while True:
        print("\noptions:")
        print("1. Count frequency of a specific item")
        print("2. count frequency of all items:")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            while True: 
                try:
                    item = int(input("Enter the item to count its frequency: "))
                    freq_obj.item = item
                    count = freq_obj.count_frequencies()
                    print(f"The frequency of {item} is : {count}")
                    break
                except ValueError:
                    print("Invalid input. Please enter an iteger.")


        elif choice == '2':
            frequencies = freq_obj.count_all_frequencies()
            print("Frequencies of all items:")
            for elements, count in sorted(frequencies.items()):
                print(f" {elements}: {count} times")
            
        elif choice == '3':
            print("Thank you for using the Array Frequency counter, Goodbye!")
            break
        else: 
            print("Invalid choice. Please select 1,2,3.")
        
if __name__ == "__main__":
    main()