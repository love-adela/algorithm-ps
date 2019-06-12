def nested_lists()->str:
    score_list = []
    for i in range(int(input())):
        name = input()
        grade = float(input())
        score_list.append([name, grade])
        
        second_lowest = sorted(score_list, key=lambda grade: grade[1])
    memo = second_lowest[0][1]

    lst = []
    for item in second_lowest:
        if item[1] == memo:
            continue
        else:
            lst.append(item)
    
    bucket = lst[0][1]
    item_list = []
    for item in lst:
        if item[1] == bucket:
            item_list.append(item[0])
        else:
            break
    print('\n'.join(sorted(item_list)))
nested_lists()
