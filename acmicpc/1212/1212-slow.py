import sys
read = lambda: sys.stdin.readline().rstrip('\n')
octal = [int(param) for param in read()]
for i in range(len(octal), 0, -1):
    octal[i-1] *= (8 ** (len(octal)-i))
decimal = sum(octal) 
print(bin(decimal)[2:])
