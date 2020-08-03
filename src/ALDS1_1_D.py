def maximize_profit(n, r):
    r_min = r[0]
    profit_max = r[1] - r[0]
    for i in range(1, n):
        if profit_max < r[i] - r_min:
            profit_max = r[i] - r_min
        if r_min > r[i]:
            r_min = r[i]
    print(profit_max)
    return


def main():
    n = int(input())
    r = [int(input()) for i in range(n)]
    maximize_profit(n, r)

if __name__ == "__main__":
    main()