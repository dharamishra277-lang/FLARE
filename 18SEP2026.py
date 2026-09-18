import sys
input=sys.stdin.readline
for _ in range(int(input())):
    s = input().strip()
    n = len(s)

    groups=1+sum(s[i]!=s[i-1] for i in range (1,n))
    reduction = 0
    for i in range (1,n-1):
        if s[i]!=s[i-1] and s[i]!=s[i+1]:
            reduction=max(reduction,1+(s[i-1]==s[i+1]))
    if n >= 2 and s[0] != s[1]:
        reduction = max(reduction, 1)
    if n >= 2 and s[-1] != s[-2]:
        reduction = max(reduction, 1)
    print(max(1, groups - reduction))