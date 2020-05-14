'''
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''

node = [[(param + (3*i))+1 for param in range(3)] for i in range(3)]
print(node)
