def sort_2d_array():
    # Read number of rows
    m = int(input("Enter the number of rows: ").strip())
    
    # Read number of columns
    n = int(input("Enter the number of columns: ").strip())
    
    # Initialize the array
    arr = []
    
    print("Enter the array elements:")
    for _ in range(m):
        row = list(map(int, input().strip().split()))
        arr.extend(row)
    
    # Sort the flattened array
    arr.sort()
    
    # Print the sorted 2D array
    index = 0
    for _ in range(m):
        print(" ".join(map(str, arr[index:index + n])))
        index += n

# Call the function
sort_2d_array()
