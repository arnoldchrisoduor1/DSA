def count_bits(n):
    count = 0
    if (n >= 0):
        bit_version = bin(n)[2:]
        
    for x in str(bit_version):
        if x == '1':
            count += 1
    return count

result = count_bits(1234)
print("The number of 1s is: ", result)