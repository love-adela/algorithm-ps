import sys

num_list = list(map(int, sys.stdin.read().splitlines()[1:]))
num_list.sort()
sys.stdout.write('\n'.join(str(num) for num in num_list)+'\n')

