word = input()
ans, forbidden = '', 'CAMBRIDGE'
for i in word:
    if i not in forbidden:
        ans += i
print(ans)
