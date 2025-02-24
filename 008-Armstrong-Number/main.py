# finding narcisistic value and non-narcisistic values.

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
    
result = narcissistic(153)
print(result)