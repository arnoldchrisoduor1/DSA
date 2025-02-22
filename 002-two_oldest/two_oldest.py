def Solution(myArray):
    first = second = float('-inf')
    
    for num in myArray:
        if num > first:
            second = first
            first = num
            
        elif num > second and num != first:
            second = num
            
        return[ first, second ]
    
print(Solution([23, 67, 1, 23, 56]))