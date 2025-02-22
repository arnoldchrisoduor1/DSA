def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]

# return sum(sorted(numbers)[:2])
    
result = sum_two_smallest_numbers([19, 5, 42, 2, 77])
print(result)