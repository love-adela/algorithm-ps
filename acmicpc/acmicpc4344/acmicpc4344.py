N = int(input())

def get_proportion(x):
    number = x[0]
    average = (sum(x[1:]) / number)
    upper = len([score for score in x[1:] if score > average])
    proportion = upper / number * 100
    print(f'{proportion:.3f}%')

for i in range(N):
    serial = list(map(int, input().split()))
    get_proportion(serial)
