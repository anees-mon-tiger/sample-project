
def calculate():
    a, b = 2, 3
    return add(a,b), substact(a,b)

def add(a, b):
    return a+b

def substact(a, b):
    return a-b

if "__name__" == "__main__":
    result = calculate()
    print(result)