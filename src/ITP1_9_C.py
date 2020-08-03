n = int(input())
pt_taro, pt_hanako = 0, 0
for _ in range(n):
    taro, hanako = input().split()
    if taro > hanako:
        pt_taro += 3
    elif taro < hanako:
        pt_hanako += 3
    else:
        pt_taro += 1
        pt_hanako += 1
print("{} {}".format(pt_taro, pt_hanako))
