from random import randint

def indescending_bubble():
    example = [integer for in input().split('\n')]
    for i in range(len(example)):
        iteration = 0
        for iteration in range(len(example) - (1 + i)):
            if example[iteration] > example[iteration + 1]:
                example[iteration], example[iteration +1] = example[iteration +1], example[iteration]
        
    return example

a = sorted(example)
b = indescending_bubble()
print(a)
print(b)
print(a == b)