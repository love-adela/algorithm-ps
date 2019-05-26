fibo_element = [0, 1]

def count_numbers(num:int):
    if num == 0:
        print('1 0')
    elif num == 1:
        print('0 1')
    else:
        length = len(fibo_element)
        if length < num + 1:
            for i in range(length, num +1):
                fibo_element.append(fibo_element[i-1] + fibo_element[i-2])
        print(f'{fibo_element[num-1]} {fibo_element[num]}')

for _ in range(int(input())):
    n = int(input())
    count_numbers(n)
