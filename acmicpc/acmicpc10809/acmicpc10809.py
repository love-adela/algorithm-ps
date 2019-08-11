string = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_index(string, alphabet):
    for i in range(len(string)):
        for j in range(len(alphabet)):
            if i == j:
                return string[i]
            else:
                return -1


print(get_index(string, alphabet))

