params = [int(x) for x in input().split()]
point = params[-1]
card_numbers = sorted([int(i) for i in input().split()])
max_sum = 0

for i in range(len(card_numbers)):
    for j in range(i+1, len(card_numbers)):
        for k in range(j+1, len(card_numbers)):
            if card_numbers[i] + card_numbers[j] + card_numbers[k] > point:
                break
            if card_numbers[i] + card_numbers[j] + card_numbers[k] <= point \
            and point - (card_numbers[i] + card_numbers[j] + card_numbers[k]) < point - max_sum:
                    max_sum = card_numbers[i] + card_numbers[j] + card_numbers[k]
print(max_sum)

