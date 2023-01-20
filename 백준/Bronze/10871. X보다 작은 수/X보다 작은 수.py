import sys
n, x = map(int,sys.stdin.readline().split())
a = list(input().split())

for i in range(n):
    if int(a[i]) < x:
        print(a[i], end=" ")