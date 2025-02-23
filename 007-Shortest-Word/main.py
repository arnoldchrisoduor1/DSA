# Finding the shortest word within a given string of words.

def find_short(s):
    words = s.split()
    smallestLength = 1000
    for word in words:
        length = len(word)
        if length < smallestLength:
            smallestLength = length
            
    print(smallestLength)
    return smallestLength

    # return min(len(x) for x i s.split())


find_short("bitcoin take over the world maybe who knows perhaps")