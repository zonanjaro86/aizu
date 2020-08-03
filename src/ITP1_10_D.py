
def get_minkowski(n, x, y, p):
    sum = 0
    for i in range(n):
        sum += abs(x[i] - y[i]) ** p
    return sum ** (1/p)

def get_minkowski_inf(n, x, y):
    return max([abs(x[i] - y[i]) for i in range(n)])

def main():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    print(get_minkowski(n, x, y, 1))
    print(get_minkowski(n, x, y, 2))
    print(get_minkowski(n, x, y, 3))
    print(get_minkowski_inf(n, x, y))
    

if __name__ == "__main__":
    main()