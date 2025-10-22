def insert_element(arr,index,element):
    if index < 0 or index > len(arr):
        reise IndexError("Index out of bounds")
    return arr[:index] + [element] + arr[index:]

while True:
    try:
        n = int(input("Enter the number of elements in the array: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Enter the elements:")
arr = []
for i in range(n):
    while True:
        try:
            element = int(input(f"Element {i+1}: "))
            arr.append(element)
            break
        except ValueError:
            print("Invalid input. Please enter an interger.")

print(f"\nArray:",{arr})

while True:
    try:
        index = int(input(f"Enter index (0 to {len(arr)}):")) 
        if index < 0 or index > len(arr):
            print(f"Idex out of bounds. Please enter index between 0 and {len(arr)}.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an interger.")

while True:
    try:
        element = int(input("Enter the element to insert: "))
        break
    except ValueError:
        print("Invalid input. Please enter valid integer.")

result = insert_element(arr,index,element)
print(f"\nArray afrer insertion:",{result})
