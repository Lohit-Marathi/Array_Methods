# class Searching():
#     def merge_sort(self,array):
#         pass

#     def merge_sort_helper():
#         pass

#     def _merge():
#         pass
    
#     def is_empty():
#         pass

#     def display(self):
#         pass

#     def get_integer_input(self,prompt,min_val,max_val):
#         """This takes  validated integer input from the user"""
#         while True:
#             try:
#                 value = int(input(prompt))
#                 if min_val is not None and value < min_val:
#                     print(f"The value must be at least {min_val}")
#                     continue
#                 if max_val is not None and value > max_val:
#                     print(f"The value must be under {max_val}")
#                     continue
#                 return value
#             except ValueError:
#                 print("Invalid Input, Please enter the valid value")


#     def create(self):
#         """This Creates An Array Using User Input"""
#         size = self.get_integer_input("Enter a valid size of an array: ",min_val = 1)
#         self.array = []
#         print("Enter the array elements:")

#         for i in range(size):
#             element = get_integer_input(f"Enter the element {i + 1}")
#             self.array.append(element)

#         print(f"\nArray Successfully created: {self.array}")

    
#     def show(self):
#         pass

#     def run(self):
#         """This is the main function"""
#         print("\n" + "=" *50)
#         print("Welcome to the searching program")
#         print("="*50)

#         self.creat_array()

#         while True:
#             if self.is_empty():
class Sum():
    def __init__(self, x, y):
        # Store the initial values 5 and 10 as instance variables
        self.initial_x = x
        self.initial_y = y

    def get_int(self, prompt):
        """Helper method to safely get an integer from the user."""
        while True:
            try:
                # Get user input and convert to an integer
                return int(input(prompt))
            except ValueError:
                print("🚨 Invalid input. Please enter a whole number (integer).")

    def sum_user_input(self):
        """Asks for two new integers, sums them, and prints the result."""
        print("\n--- Phase 1: Summing User Input ---")
        
        # Ask for and store the new values (these are local to this method)
        user_y = self.get_int("Enter the integer value for y: ")
        user_x = self.get_int("Enter the integer value for x: ")
        
        user_sum = user_x + user_y
        print(f"\n✅ The sum of your entered values ({user_x} + {user_y}) is: {user_sum}")

    def print_initial_values(self):
        """Prints the values defined in the initializer (5 and 10) one by one."""
        print("\n--- Phase 2: Printing Initial Values ---")
        
        # Access the initial values using self.
        print(f"The first initial value (x) is: {self.initial_x}")
        print(f"The second initial value (y) is: {self.initial_y}")
        print(self.initial_x + self.initial_y)

# --- Execution ---
# 1. Initialize the object 'ok' with the values x=5 and y=10
print("Initializing object 'ok' with base values x=5 and y=10.")
ok = Sum(5, 10) 

# 2. Run the method to get user input, sum, and print (e.g., user enters 20 and 30)
ok.sum_user_input() 

# 3. Run the method to print the initial values (5 and 10)
ok.print_initial_values()

