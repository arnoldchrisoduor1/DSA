# List all natural numbers that are mutiples of 3 or 5 and sum
def solution(number):
    sum = 0
    
    if (number < 0):
        return 0
    
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            
    return sum
    