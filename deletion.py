class ArrayDeletion():
    def __init__(self):
        self.array = []

    def get_integer_input(self,prompt,min_val=None, max_val=None):
        """Get a validated integer input from the user."""
        while True:
            try:
                value = int(input(prompt))
                if (min_val is not None and value < min_val):
                    print(f"value must be at least {min_val}.")
                    continue
                if (max_val is not None and value > max_val):
                    print(f"value must be at most {max_val}")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def create_array(self):
        """Create an array based on user input."""
        size = self.get_integer_input("Enter the size of the array: ", min_val=1)

        self.array = []
        for i in range(size):
            element = self.get_integer_input(f"Enter element {i + 1}: ")
            self.array.append(element)

        print(f"Array created : {self.array}")

    def display_array(self):
        if self.array:
            print("Current Array:",self.array)
            print(f"Array Size: {len(self.array)}")
        else:
            print("\nArray is empty.")

    def delete_by_index(self,index):
        if (index < 0 or index >= len(self.array)):
            raise IndexError("Index out of bounds.")
        deleted_element = self.array[index]
        self.array = self.array[:index] + self.array[index+1:]
        return deleted_element

    def delete_by_value(self,value):
        if value not in self.array:
            raise ValueError("Value not found in the array.")
        count = self.array.count(value)
        self.array.remove(value)
        return count

    def is_empty(self):
        return len(self.array) == 0
    
    def handle_deletion_by_index(self):
        self.display_array()
        print(f"Index range: 0 to {len(self.array)-1}")
        index = self.get_integer_input("Enter the index to delete: ", min_val=0, max_val=len(self.array)-1)
        
        try:
            deleted_element = self.delete_by_index(index)
            print(f"\nDeleted element:{deleted_element} from the index: {index}")
        except IndexError as e:
            print(f"\nError: {e}")
        

    def handle_deletion_by_value(self):
        self.display_array()
        value = self.get_integer_input("Enter the value to delete: ")

        try:
            count = self.delete_by_value(value)
            if count > 1:
                print(f"\nThe value {value} was found {count} times. Deleted the first occurrence.")
            else:
                print(f"\nDeleted the value: {value} from the array.")

        except ValueError as e:
            print(f"\nError: {e}")

    def show_menu(self):
        print("\nMenu:")
        print("-"*50)
        print("1. Delete by Index (index value)")
        print("2. Delete by Value (element value)")
        print("3. Display Array")
        print("4. Create New Array")
        print("5. Exit")

    def run(self):
        print("=" *50)
        print("    ARRAY DELETION PROGRAM    ")
        print("=" *50)

        self.create_array()
        while True:
            if self.is_empty():
                print("Array is empty. Connot delete more elements.")
                result = input("Do you want to create a new array? (y/n): ").strip().lower()
                if result == 'y':
                    self.create_array()
                    continue
                else:
                    break

            self.show_menu()
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                self.handle_deletion_by_index()

            elif choice == '2':
                self.handle_deletion_by_value()

            elif choice == '3':
                self.display_array()
            
            elif choice == '4':
                confirm = input("Are you sure you want to create a new array? (y/n): ").strip().lower()
                if confirm == 'y':
                    self.create_array()
            
            elif choice == '5':
                print("=" *50)
                print("Thank you for using the ARRAY DELETION PROGRAM. Goodbye!")
                print("=" *50)
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    app = ArrayDeletion()
    app.run()
        