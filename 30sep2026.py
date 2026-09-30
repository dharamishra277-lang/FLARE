t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    bad = [i for i in range(n) if p[i] != i + 1]

    if all(p[bad[i]] == bad[-1 - i] + 1 for i in range(len(bad))):
        print("YES")
    else:
        print("NO")