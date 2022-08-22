science = sorted([int(input()) for param in range(4)], reverse=True)
society = sorted([int(input()) for param in range(2)], reverse=True)


print(sum(science[:3])+sum(society[:1]))
