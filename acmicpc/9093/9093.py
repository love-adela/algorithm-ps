N = int(input())

def palindrome(sentence):
    words = [param[::-1] for param in sentence.split(' ')] 
    return ' '.join(words)

while N:
    sentence = input()    
    print(palindrome(sentence)) 
    N -=1
