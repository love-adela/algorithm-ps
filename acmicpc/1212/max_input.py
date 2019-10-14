import random 
a = [str(random.randrange(1, 8))] + [str(random.randrange(0, 8)) for _ in range(333333)]
print(''.join(a))
