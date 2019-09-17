def fib_tab(n):
    fib_table = [0, 1, 1]
     
    for i in range(len(fib_table)+1):
        if i > 2:
            fib_table[i] = fib_table[i-1] + fib_table[i-2]
            fib_table.append(fib_table[i])
        print(fib_table)
    return fib_table[n]1

print(fib_tab(1))
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

