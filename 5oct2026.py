import sys

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    answers = []

    for _ in range(t):
        n = int(input_data[index])
        c = input_data[index + 1]
        s = input_data[index + 2]
        index += 3

        left = 0
        right = n - 1
        coins = 0

        while left < right:
            if s[left] != s[right]:
             if s[left] == c or s[right] == c:
              coins += 1
            else:
             coins += 2
            left += 1
            right -= 1

        answers.append(str(coins))

    print("\n".join(answers))

if __name__ == "__main__":
    solve()