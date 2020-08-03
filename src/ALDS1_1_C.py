import math

def isPrime(k):
    # 2以外の偶数は素数ではない
    if k % 2 == 0 and k != 2:
        return False
    # 平方根までの範囲で約数をもつかどうか 
    for divisor in range(2, math.floor(math.sqrt(k))+1):
        if k % divisor == 0:
            return False
    return True

def main():
    n = int(input())
    cnt = 0
    for _ in range(n):
        if isPrime(int(input())):
            cnt += 1
    print(cnt)
    

if __name__ == "__main__":
    main()
