import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    it = iter(data)
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]

        pref = 0
        possible = True

        for i in range(1, n + 1):          # <-- this defines i
            pref += a[i - 1]
            need = i * (i + 1) // 2
            if pref < need:
                possible = False
                break

        out.append("YES" if possible else "NO")

    print("\n".join(out))

if __name__ == "__main__":
    solve()