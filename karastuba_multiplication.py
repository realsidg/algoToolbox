import sys

def karatsuba(x,y):
    if len(x) == 1 or len(y) == 1:
        return str(int(x)*int(y))

    if len(x) < len(y):
        n = len(y)
        x = '0'*(len(y)-len(x)) + x
    
    elif len(y) < len(x):
        n = len(x)
        y = '0'*(len(x)-len(y)) + y
    
    else:
        n = len(x)

    if n % 2:
        mid = n//2 +1
    else:
        mid = n//2

    a = x[:mid]
    b = x[mid:]
    c = y[:mid]
    d = y[mid:]

    ac = int(karatsuba(a,c))
    bd = int(karatsuba(b,d))
    abcd = int(karatsuba(str(int(a)+int(b)), str(int(c)+int(d))))

    return str(10**(2*(n//2)) * ac + 10**(n//2) * (abcd - ac - bd)  + bd)  

def main():
    x,y = sys.argv[1:]
    print(karatsuba(x,y))

if __name__ == "__main__":
    main()