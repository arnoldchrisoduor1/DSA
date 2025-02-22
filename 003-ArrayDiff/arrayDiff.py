def array_diff(a, b):
    
    filtered_array = [element for element in a if element not in b]
    
    # using dictionary to preserve order and remove duplicates.
    return list(dict.fromkeys(filtered_array))

# test cases
print(array_diff([1, 2, 2, 3], [1]))