def solve(n: float) -> float:
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n = n / i
    return n


def main() -> None:
    inp = 600851475143
    solve(inp)


if __name__ == '__main__':
    main()
