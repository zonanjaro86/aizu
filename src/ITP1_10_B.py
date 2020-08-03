import math

def main():
    a, b, C = map(int, input().split())
    
    S = a * b * 0.5 * math.sin(math.radians(C))
    L = (a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))**0.5 + a + b
    h = S / a * 2
    
    print(S)
    print(L)
    print(h)

if __name__ == "__main__":
    main()