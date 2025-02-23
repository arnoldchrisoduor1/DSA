def get_middle(s):
    length = len(s)
    
    if length % 2 !=0:
        value = (length - 1) / 2
        text = s[int(value)]
        
    if length % 2 == 0:
        value = (length) / 2
        text = s[int(value)-1] + s[int(value)]
    
    print(text)
    return text
    
get_middle("textin")