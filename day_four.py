len(pass)==6
range(240298, 784956)

def is_valid(numb):
    has_dubble=False
    prev = 0
    if len(str(numb))!=6:
        print("too short")
        return False
    for i in str(numb):
        if i < str(prev):
            print(f"{i} too small")
            return False
        if i==str(prev):
            has_dubble = True
        prev = i
    return has_dubble
