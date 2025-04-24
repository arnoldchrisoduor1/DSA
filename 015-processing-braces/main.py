def is_valid_braces(string):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    
    for char in string:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
            
    return not stack 


print(is_valid_braces("(){}[]"))
print(is_valid_braces("(}"))   