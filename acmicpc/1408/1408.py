current = list(map(int, input().split(':')))
target = list(map(int, input().split(':')))

s = current[0]*3600+current[1]*60+current[2]
m = target[0]*3600+target[1]*60+target[2]
h = (m-s)%86400
print(h//36000, h//3600%10,':',h//600%6, h//60%10,':',h//10%6, h%10, sep='')
