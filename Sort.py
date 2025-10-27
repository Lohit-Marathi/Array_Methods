class Sort():

    def __init__():
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
