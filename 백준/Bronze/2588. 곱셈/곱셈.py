a=int(input())

b=int(input())

print(a*(b%10), a*(((b-(b%10))%100)//10) , a*((b-(b%10))//100), a*b, sep='\n')