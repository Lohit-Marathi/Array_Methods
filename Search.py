class ArraySearcher:
    """Class to perform different search operations on arrays"""
    
    def __init__(self, array):
        """Initialize with an array"""
        self.array = array
        self.original_array = array.copy()  # Keep original for reference
    
    def display_array(self):
        """Display the current array"""
        print(f"Array: {self.array}")
    
    def linear_search(self, target):
        """
        Linear Search - Works on UNSORTED or SORTED arrays
        Time Complexity: O(n)
        """
        print(f"\n{'='*50}")
        print("LINEAR SEARCH (Works on unsorted data)")
        print(f"{'='*50}")
        print(f"Searching for: {target}")
        self.display_array()
        
        comparisons = 0
        for index, element in enumerate(self.array):
            comparisons += 1
            print(f"Step {comparisons}: Checking index {index} -> {element}", end="")
            
            if element == target:
                print(f" ✓ FOUND!")
                print(f"\n🎉 Element {target} found at index {index}")
                print(f"Total comparisons: {comparisons}")
                return index
            else:
                print(f" ✗ Not a match")
        
        print(f"\n❌ Element {target} NOT FOUND in the array")
        print(f"Total comparisons: {comparisons}")
        return -1
    
    def binary_search(self, target):
        """
        Binary Search - Requires SORTED array
        Time Complexity: O(log n)
        """
        print(f"\n{'='*50}")
        print("BINARY SEARCH (Requires sorted data)")
        print(f"{'='*50}")
        
        # Check if array is sorted
        if not self._is_sorted():
            print("⚠️  Array is NOT sorted. Sorting first...")
            self.array.sort()
            print("✓ Array sorted!")
        
        print(f"Searching for: {target}")
        self.display_array()
        
        left = 0
        right = len(self.array) - 1
        comparisons = 0
        
        while left <= right:
            comparisons += 1
            mid = (left + right) // 2
            mid_value = self.array[mid]
            
            print(f"\nStep {comparisons}:")
            print(f"  Range: [{left}...{right}]")
            print(f"  Middle index: {mid}, Value: {mid_value}")
            
            if mid_value == target:
                print(f"  ✓ FOUND at index {mid}!")
                print(f"\n🎉 Element {target} found at index {mid}")
                print(f"Total comparisons: {comparisons}")
                return mid
            elif mid_value < target:
                print(f"  {mid_value} < {target}, search RIGHT half")
                left = mid + 1
            else:
                print(f"  {mid_value} > {target}, search LEFT half")
                right = mid - 1
        
        print(f"\n❌ Element {target} NOT FOUND in the array")
        print(f"Total comparisons: {comparisons}")
        return -1
    
    def _is_sorted(self):
        """Check if array is sorted"""
        return all(self.array[i] <= self.array[i + 1] for i in range(len(self.array) - 1))
    
    def reset_array(self):
        """Reset to original unsorted array"""
        self.array = self.original_array.copy()


def main():
    """Main program to interact with user"""
    print("="*60)
    print("          ARRAY SEARCH PROGRAM")
    print("="*60)
    
    # Get array from user
    while True:
        try:
            print("\nEnter array elements separated by spaces:")
            user_input = input("Example: 64 34 25 12 22 11 90\n> ")
            array = list(map(int, user_input.split()))
            
            if len(array) == 0:
                print("❌ Array cannot be empty! Try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter only numbers separated by spaces.")
    
    # Create searcher object
    searcher = ArraySearcher(array)
    
    print("\n" + "="*60)
    print("Array created successfully!")
    searcher.display_array()
    print(f"Is array sorted? {'Yes ✓' if searcher._is_sorted() else 'No ✗'}")
    
    # Main menu loop
    while True:
        print("\n" + "="*60)
        print("SEARCH MENU")
        print("="*60)
        print("1. Linear Search (works on unsorted data)")
        print("2. Binary Search (requires sorted data)")
        print("3. Display current array")
        print("4. Reset to original array")
        print("5. Enter new array")
        print("6. Exit")
        print("="*60)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            try:
                target = int(input("\nEnter element to search: "))
                searcher.reset_array()  # Use original unsorted array
                searcher.linear_search(target)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        elif choice == '2':
            try:
                target = int(input("\nEnter element to search: "))
                searcher.reset_array()  # Reset first
                searcher.binary_search(target)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        elif choice == '3':
            print("\nCurrent Array:")
            searcher.display_array()
            print(f"Is sorted? {'Yes ✓' if searcher._is_sorted() else 'No ✗'}")
        
        elif choice == '4':
            searcher.reset_array()
            print("\n✓ Array reset to original:")
            searcher.display_array()
        
        elif choice == '5':
            try:
                print("\nEnter new array elements separated by spaces:")
                user_input = input("> ")
                new_array = list(map(int, user_input.split()))
                
                if len(new_array) == 0:
                    print("❌ Array cannot be empty!")
                    continue
                
                searcher = ArraySearcher(new_array)
                print("\n✓ New array created!")
                searcher.display_array()
            except ValueError:
                print("❌ Invalid input! Please enter only numbers.")
        
        elif choice == '6':
            print("\n" + "="*60)
            print("Thank you for using Array Search Program! 👋")
            print("="*60)
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()



            
            
