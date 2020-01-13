from sys import stdin
def main():
    next(stdin)
    input = stdin.read()

    params = sorted(list(map(int, input.split())))
    print(params[0]* params[-1])

    # 12의 약수: 2, 3, 4, 6

if __name__ == "__main__":
    main()

