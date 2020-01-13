from sys import stdin
def main():
    next(stdin)
    input = stdin.read()

    params = list(map(int, input.split()))
    print(min(params)* max(params))

    # 12의 약수: 2, 3, 4, 6

if __name__ == "__main__":
    main()

