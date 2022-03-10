s = input('Enter a text ')
s2= input('Enter a pattern ')
cnt=cnt2=match=0
for i in s:
    cnt+=1
for i in s2:
    cnt2+=1
    
for i in range (0,cnt):
    if s[i]==s2[0]:
        temp=s[i:i+cnt2]
        if temp==s2:
            match+=1
print('The Number of times = ',+match)
