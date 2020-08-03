def isPrime(k):
    # 2以外の偶数は素数ではない
    if k % 2 == 0 and k != 2:
        return False
    for divisor in range(2, k//2):
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
