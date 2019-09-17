#! usr/bin/python

'''
Codeit 알고리즘 - Brute Force
3. 카드 뭉치 최대 조합
'''

def max_product(left_cards, right_cards):
    product = []
    for left_num in left_cards:
        for right_num in right_cards:
            product.append(left_num*right_num)
    return max(product)

# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
