class Sort:
    def __init__(self):
        self.array = []

    def bubble_sort(self):
        print("Performing bubble sort")
        self.display_array()

        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(0,n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j],self.array[j+1] = self.array[j+1],self.array[j]
                    swapped = True
            if not swapped:
                break
        
        print("\nArray is sorted in acending order")
        self.display_array()
                    


    def selection_sort(self):
        print("Performing selection sort\n")
        self.display_array()

        n = len(self.array)
        for i in range(n):
            min_ind  = i
            for j in range(i+1,n):
                if self.array[j] < self.array[min_ind]:
                    min_ind = j
            self.array[i],self.array[min_ind] = self.array[min_ind],self.array[i]
        
        print("Array is sorted in acending order.")
        self.display_array()

    def display_array(self):
        """Display the current array."""
        if self.array:
            print("Current Array:", self.array)
        else:
            print("\nArray is empty.")
            
    def is_empty(self):
        """Check if the array is empty."""
        return len(self.array) == 0
    
    def get_integer_input(self, prompt, min_val=None, max_val=None):
        """Get a validated integer input from the user."""
        while True:
            try:
                value = int(input(prompt))
                if (min_val is not None and value < min_val):
                    print(f"value must be at least {min_val}.")
                    continue
                if (max_val is not None and value > max_val):
                    print(f"value must be at most {max_val}.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def create_array(self):
        """Create an array based on user input."""
        size = self.get_integer_input("Enter the size of the array: ",min_val=1)

        self.array = []

        for i in range(size):
            element = self.get_integer_input(f"Enter element {i + 1}: ")
            self.array.append(element)

        print(f"Array created : {self.array}")

    def show_menu(self):
        """Display the sorting menu."""
        print("=" * 50)
        print("SORTING MENU")
        print("=" * 50)
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Display Array")
        print("6. Create New Array")
        print("7. exit")
        print("=" * 50)
    

    def run(self):
        """Run the sorting program."""
        print("=" * 50)
        print("WELCOME TO SORTING PROGRAM")
        print("=" * 50)
        
        self.create_array()
        
        while True:
            if self.is_empty():
                print("\nArray is empty. Please create a new array.")
                choose = input("Do you want to create a new array? (y/n): ").strip().lower()
                if choose == 'y':
                    self.create_array()
                    continue
                else:
                    print("Exiting the program. Goodbye!")
                    break

            self.show_menu()
            choice = input("Choose any option (1-7): ").strip()

            if choice == '1':
                self.bubble_sort()
        
            if choice == '2':
                self.selection_sort()

            if



if __name__ == "__main__":
    sorter = Sort()
    sorter.run()
