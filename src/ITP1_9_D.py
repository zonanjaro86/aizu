

def _print(s, a, b):
    print(s[a:b+1])

def _reverse(s, a, b):
    tmp = s[a:b+1]
    return s[:a] + tmp[::-1] + s[b+1:]

def _replace(s, a, b, p):
    return s[:a] + p + s[b+1:]

def str_operation(s, command, a, b, p=""):
    a = int(a)
    b = int(b)
    if command == "print":
        _print(s, a, b)
    elif command == "reverse":
        s = _reverse(s, a, b)
    elif command == "replace":
        s = _replace(s, a, b, p)
    return s


def main():
    s = input()
    n = int(input())
    for _ in range(n):
        s = str_operation(s, *input().split())

if __name__ == "__main__":
    main()
