resistor = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green': 5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
first = str(resistor[input()])
if first == 0:
    first = ''
second = str(resistor[input()])
if second == 0:
    second = ''

answer = int(first + second)

third = 10**resistor[input()]
if answer == '':
    print(0)
else:
    print(answer * third)

