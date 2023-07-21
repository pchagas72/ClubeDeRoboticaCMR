def reverse_string(produto) -> str:
    return str(produto)[::-1]


def check_palindrom(produto) -> bool:
    return str(produto) == reverse_string(produto)


def update_largest_palindrom(produto, largest) -> int:
    if not check_palindrom(produto) or produto <= largest:
        return largest
    return produto


def solve() -> None:
    largest_palindrom: int = 0
    for first_product in range(100, 1000):
        for second_product in range(100, 1000):
            produto: int = first_product * second_product
            largest_palindrom = update_largest_palindrom(
                produto, largest_palindrom
            )

    print(largest_palindrom)


if __name__ == '__main__':
    solve()
