def find_subsequences(index, current, s):
    print(f"Called with index={index}, current='{current}'")

    if index == len(s):
        print(f"  ➤ Reached end: '{current}'")
        return

    # Include current character
    find_subsequences(index + 1, current + s[index], s)
    
    # Exclude current character
    find_subsequences(index + 1, current, s)
find_subsequences(0,'','abc')