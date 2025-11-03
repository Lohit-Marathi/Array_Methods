class Sort:
    def __init__(self):
        self.array = []

    def bubble_sort(self):
        """Bubble Sort Algorithm"""
        print("\nPerforming Bubble Sort...")
        self.display_array()
        
        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
            if not swapped:
                break
        
        print("\nArray after Bubble Sort:")
        self.display_array()

    def selection_sort(self):
        """Selection Sort Algorithm"""
        print("\nPerforming Selection Sort...")
        self.display_array()
        
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
        
        print("\nArray after Selection Sort:")
        self.display_array()

    def insertion_sort(self):
        """Insertion Sort Algorithm"""
        print("\nPerforming Insertion Sort...")
        self.display_array()
        
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        
        print("\nArray after Insertion Sort:")
        self.display_array()

    def merge_sort(self):
        """Merge Sort Algorithm"""
        print("\nPerforming Merge Sort...")
        self.display_array()
        
        self.array = self._merge_sort_helper(self.array)
        
        print("\nArray after Merge Sort:")
        self.display_array()

    def _merge_sort_helper(self, arr):
        """Helper function for merge sort"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self._merge_sort_helper(arr[:mid])
        right = self._merge_sort_helper(arr[mid:])
        
        return self._merge(left, right)

    def _merge(self, left, right):
        """Merge two sorted arrays"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def display_array(self):
        """Display the current array"""
        if self.array:
            print(f"Current Array: {self.array}")
            print(f"Array Size: {len(self.array)}")
        else:
            print("\nArray is empty.")

    def show_menu(self):
        """Display the sorting menu"""
        print("\n" + "=" * 50)
        print("SORTING MENU")
        print("=" * 50)
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Display Array")
        print("6. Create New Array")
        print("7. Exit")
        print("=" * 50)

    def is_empty(self):
        """Check if array is empty"""
        return len(self.array) == 0

    def get_integer_input(self, prompt, min_val=None, max_val=None):
        """Get validated integer input from user"""
        while True:
            try:
                value = int(input(prompt))
                if min_val is not None and value < min_val:
                    print(f"Value must be at least {min_val}.")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Value must be at most {max_val}.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def create_array(self):
        """Create a new array with user input"""
        size = self.get_integer_input("Enter the size of the array: ", min_val=1)
        self.array = []

        for i in range(size):
            element = self.get_integer_input(f"Enter element {i + 1}: ")
            self.array.append(element)
        
        print(f"\nArray created successfully: {self.array}")

    def run(self):
        """Main loop to run the sorting program"""
        print("\n" + "=" * 50)
        print("WELCOME TO THE SORTING PROGRAM")
        print("=" * 50)

        self.create_array()
        
        while True:
            if self.is_empty():
                print("\nArray is empty. Please create a new array.")
                choice = input("Do you want to create a new array? (y/n): ").strip().lower()
                if choice == 'y':
                    self.create_array()
                    continue
                else:
                    print("\nExiting program. Goodbye!")
                    break
            
            self.show_menu()
            choice = input("Enter your choice (1-7): ").strip()

            if choice == '1':
                self.bubble_sort()
            elif choice == '2':
                self.selection_sort()
            elif choice == '3':
                self.insertion_sort()
            elif choice == '4':
                self.merge_sort()
            elif choice == '5':
                self.display_array()
            elif choice == '6':
                self.create_array()
            elif choice == '7':
                print("\nExiting program. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    sorter = Sort()
    sorter.run()