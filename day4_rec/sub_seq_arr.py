def find_subsequences(index, current, arr, result):
    print(f"Called with index={index}, current={current}")
    
    if index == len(arr):
        print(f"  ➤ Decision reached: {current}")
        result.append(current[:])  # Add a copy of the current subsequence
        return

    # Include current element
    print(f"  ➕ Including {arr[index]}")
    current.append(arr[index])
    find_subsequences(index + 1, current, arr, result)

    # Exclude current element (backtrack)
    print(f"  ➖ Excluding {arr[index]} (Backtrack)")
    current.pop()
    find_subsequences(index + 1, current, arr, result)
find_subsequences(0,[],[1,2,3],[])
