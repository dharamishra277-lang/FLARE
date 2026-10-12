def can_divide(w: int) -> bool:
    return w % 2 == 0 and w > 2


def main():
    w = int(input())
    print("YES" if can_divide(w) else "NO")


if __name__ == "__main__":
    main()