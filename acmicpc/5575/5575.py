for _ in range(3):
    record = list(map(int, input().split()))
    opening = 3600 * record[0] + 60 * record[1] + record[2] 
    closing = 3600 * record[3] + 60 * record[4] + record[5]
    office_hour = closing - opening
    print(office_hour // 3600, office_hour % 3600 // 60, office_hour % 60)
