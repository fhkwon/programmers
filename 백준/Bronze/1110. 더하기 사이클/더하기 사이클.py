a = int(input())

if 1 <= a < 10:
    a = '0'+str(a)
elif a == 0:
    a = '0'+str(a)
a = list(str(a))

b = 0
i = 0
while True:
    a.append(str((int(a[i])+int(a[i+1]))%10)) 
    b += 1
    i += 1
    if a[0]+a[1] == a[i]+a[i+1]:
        print(b)
        break