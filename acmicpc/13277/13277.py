from decimal import Decimal,getcontext;getcontext().prec=10**6
import sys
read = lambda: sys.stdin.readline()
A,B=map(Decimal,read().split())
print(format(A*B,'f'))
