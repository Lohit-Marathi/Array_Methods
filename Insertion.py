def insert_element(arr,index,element):
    if index < 0 or index > len(arr):
        raise IndexError("Index out of bounds")
    return arr[:index] + [element] + arr[index:]
n = int(input("Enter number of elements in the array: "))
print("Enter the elemens of the array:")
arr = []
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)
index = int(input("Enter the index where you want to insert the element: "))

print(insert_element(arr,index,element))


