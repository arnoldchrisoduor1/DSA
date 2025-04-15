def roman_to_decimal(roman):
    roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    
    result = 0
    
    for i in range(len(roman)):
        # the current symbol value.
        current_value = roman_values[roman[i]]
        
        #nect symbol if it exists.
        next_value = roman_values[roman[i + 1]] if i + 1 < len(roman) else 0
        
        # if current value is less than the next value, subtract it.
        if current_value < next_value:
            result -= current_value
        else:
            # otherwise add it.
            result += current_value
            
    return result

# Test cases
print(roman_to_decimal("MM")) 
print(roman_to_decimal("MDCLXVI"))
print(roman_to_decimal("M"))      
print(roman_to_decimal("CD"))     
print(roman_to_decimal("XC"))     
print(roman_to_decimal("XL"))   
print(roman_to_decimal("I"))   