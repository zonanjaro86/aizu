def get_sd(n, s):
    m = sum(s)/n
    sd2 = 0
    for i in range(n):
        sd2 += (s[i] - m)**2
    return (sd2/n)**0.5
        

def main():
    while(True):
        n = int(input())
        if n == 0: break

        print(get_sd(n, list(map(int, input().split()))))

if __name__ == "__main__":
    main()