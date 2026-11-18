import sys


def solve():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(data)
    answers = []

    for _ in range(t):
        n = next(data)
        m = next(data)
        q = next(data)

        edges = []
        total = 0

        for _ in range(m):
            u = next(data) - 1
            v = next(data) - 1
            w = next(data)

            edges.append((w, u, v))
            total += w

        # Minimum spanning forest using Kruskal's algorithm.
        edges.sort()

        parent = list(range(n))
        size = [1] * n

        def find(v):
            while v != parent[v]:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        weights = []
        prefix = [0]

        for w, u, v in edges:
            ru = find(u)
            rv = find(v)

            if ru == rv:
                continue

            if size[ru] < size[rv]:
                ru, rv = rv, ru

            parent[rv] = ru
            size[ru] += size[rv]

            weights.append(w)
            prefix.append(prefix[-1] + w)

        r = len(weights)

        for _ in range(q):
            x = next(data)

            # Find how many existing cables are worth keeping.
            left, right = 0, r

            while left < right:
                mid = (left + right) // 2

                # Keeping this cable saves the cost of one new cable.
                if weights[mid] <= x * (n - mid - 1):
                    left = mid + 1
                else:
                    right = mid

            kept = left
            new_cables = n - kept - 1

            revenue = total - prefix[kept]
            cost = x * new_cables * (new_cables + 1) // 2

            answers.append(str(revenue - cost))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()