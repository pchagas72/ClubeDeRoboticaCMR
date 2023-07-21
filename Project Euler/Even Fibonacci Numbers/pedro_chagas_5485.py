def fibonacci(x: int) -> int:
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


def solve(limit: int) -> int:
    sum: int = 0
    value: int = 0
    counter: int = 0
    while value < limit:
        value = fibonacci(counter)
        if value % 2 == 0:
            sum += value
        counter += 1
    return sum


def main() -> None:
    limit = 4000000
    solve(limit)


if __name__ == '__main__':
    main()
