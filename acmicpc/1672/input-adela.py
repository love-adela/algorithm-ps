import random 
import string

N = 1000000
letters = 'ACGT' 
random_letters = ''.join(random.choice(letters) for _ in range(N))

print(N)
print(random_letters)
