n = int(input())

def go(index:int):
    # 손에 Index 계란에 계란을 쥐고 있다.
    if index == n:
        pass

    if index == n:
        # 깨진 계란의 개수를 구해줘야 함
        count = 0 
        for i in range(n):
            if s[i] <0: count += 1
        return count

    # 어떤 계란을 칠지 모르기 때문에 다 해봐야 함 index -> i 
    if s[index]<=0: return go(index+1) # 손에 든 계란이 깨진 경우
    answer = 0
    for i in range(n):
        if index == i:
            continue

        if s[i] <= 0: continue # 깨지지 않은 다른 계란 중 하나를 친다.
        ok = True
        s[index] -= w[i] # i번째 무게 만큼 감소
        s[i] -= w[index]

        temp = go(index +1)
        if ans<temp: ans=temp
        s[index] += w[i]
        s[i] += w[index]
        
        if ok == False: return go(index+1)
        return answer

def main():
    for i in range(n): # 현재 몇 번 계란에 대해서?
        input(s[i])
        input(w[i])

    print(go(0))
    return 0
