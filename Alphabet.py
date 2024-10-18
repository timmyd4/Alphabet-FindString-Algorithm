alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findString(target, lyst):
    saved = ''
    for items in target.lower():
        if items in lyst:
            saved += items
    return saved
    

print(findString('HelloWorld', alpha))