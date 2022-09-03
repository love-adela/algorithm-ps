result = int(input()) 
while True:
    operator = input()
    if operator == '=':
        break
    operand = int(input())
    if operator == '+':
        result += operand
    if operator == '-':
        result -= operand
    if operator == '*':
        result *= operand
    if operator == '/':
        result //= operand
print(result)
