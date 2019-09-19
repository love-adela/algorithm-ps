# def move_disk(disk_num, start_peg, end_peg):
#     print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

# def hanoi(num_disks, start_peg = 1, end_peg = 3):
#     if num_disks == 0:
#         return
#     else:
#         other_peg = 6 - start_peg - end_peg
#         hanoi(num_disks - 1, start_peg, other_peg)
#         move_disk(num_disks, start_peg, end_peg)
#         hanoi(num_disks - 1, other_peg, end_peg)

# hanoi(3, 1, 3)

def move_disk(disk_num, start_peg, end_peg):
    if disk_num == 0:
        return
    if disk_num == 1:
        print(f"{start_peg} {end_peg}")
        return
    third_peg = 6 - start_peg - end_peg    
    move_disk(disk_num - 1, start_peg, third_peg)
    print(f"{start_peg} {end_peg}")
    move_disk(disk_num - 1, third_peg, end_peg)

move_disk(5, 1, 3)