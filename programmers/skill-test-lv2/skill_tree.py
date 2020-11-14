# https://programmers.co.kr/learn/courses/30/lessons/49993
# 스킬트리

def is_validate(item:str, string:str)->bool:
    chr_list = [c for c in item if c in string]
    check_list = []
    for i in range(len(chr_list)):
        if string[0] in chr_list and chr_list[i] == string[i]:
            check_list.append(chr_list[i])
        else:
            return False
    if check_list in chr_list or check_list == chr_list:
        return True
    else:
        return False

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
cnt = 0
for tree in skill_trees:
    if is_validate(tree, skill) == True:
        cnt += 1

print(cnt)