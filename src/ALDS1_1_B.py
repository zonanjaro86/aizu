def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if x % y == 0:
        return y
    return gcd(y, x % y)

def main():
    x, y = map(int, input().split())
    print(gcd(x, y))
    

if __name__ == "__main__":
    main()