number = int(input())
hanoi_array = []

def hanoi_solver(number, start, end):
    if number == 0:
        return
    if number == 1:
        hanoi_array.append(f"{start} {end}")
        return    

    via = 6 - start - end        
    hanoi_solver(number - 1, start, via)
    hanoi_array.append(f"{start} {end}")    
    hanoi_solver(number - 1, via, end)


if number <= 20:
    hanoi_solver(number, 1, 3)
    print(len(hanoi_array))
    for _ in hanoi_array:
        print(_)
else:
    print(2 ** number -1)