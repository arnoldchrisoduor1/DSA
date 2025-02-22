# Returns true of the number given in the first arguement ends with the 2nd arguement.
def solution(text, ending):
    return text.endswith(ending)

    # return text[-len(ending):] == ending if ending else True
        
result = solution("abc", "bc")
print("Result", result)