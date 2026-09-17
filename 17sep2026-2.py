import sys
input=sys.stdin.readline
t=int(input())
answers=[]
for i in range(t):
        a,b,c=sorted(map(int,input().split()))
        rounds=0
        while a!=b and b!=c:
            a+=1
            c-=1
            rounds+=1
            a,b,c=sorted((a,b,c))
        answers.append(str(rounds))
print("\n".join(answers))        