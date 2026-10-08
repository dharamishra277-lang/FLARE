import sys

input = sys.stdin.buffer.readline
INF = 10**30


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.size[a] < self.size[b]:
            a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]

        return True


class Line:
    def __init__(self, slope, intercept):
        self.m = slope
        self.b = intercept

    def value(self, x):
        return self.m * x + self.b


def bad(l1, l2, l3):
    # Intersection(l1, l2) >= Intersection(l2, l3)
    # for the maximum hull with decreasing slopes.
    return (l2.b - l1.b) * (l2.m - l3.m) >= \
           (l3.b - l2.b) * (l1.m - l2.m)


def main():
    t = int(input())
    answers = []

    for _ in range(t):
        n, m, q = map(int, input().split())

        edges = []

        for _ in range(m):
            u, v, d = map(int, input().split())
            edges.append((d, u, v))

        queries = list(map(int, input().split()))

        # Maximum spanning Kruskal
        edges.sort(reverse=True)

        dsu = DSU(n)

        removed_total = 0
        components = n

        # Point (x = number of components, y = revenue)
        points = [(components, removed_total)]

        for d, u, v in edges:
            if dsu.union(u, v):
                components -= 1
                points.append((components, removed_total))
            else:
                removed_total += d

        # Build values from the Kruskal process.
        revenue = [0] * (n + 1)

        current_removed = 0
        dsu = DSU(n)
        components = n

        revenue[components] = 0

        for d, u, v in edges:
            if dsu.union(u, v):
                components -= 1
                revenue[components] = current_removed
            else:
                current_removed += d

        # All remaining discarded edges are included when k = 1.
        revenue[1] = current_removed
        for x in queries:
            best = 0

            for k in range(1, n + 1):
                if revenue[k] == 0 and k != n:
                    continue

                cost = k * (k - 1) // 2 * x
                best = max(best, revenue[k] - cost)

            answers.append(str(best))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()