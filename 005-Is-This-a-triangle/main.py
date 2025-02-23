def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c
    
print(is_triangle(1, 2, 2))