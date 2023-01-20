H, M=map(int,input().split())
mm=M-45
if mm<0:
    H=H-1
    mm=M+15
    if H<0:
        H=23
            
print(H, mm)
    