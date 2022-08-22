total = int(input())
total_prize = int(total * 0.78)
print(total_prize, end=' ')

rest_prize = int((total * 0.2 * 0.78) + total * 0.8)
print(rest_prize)

