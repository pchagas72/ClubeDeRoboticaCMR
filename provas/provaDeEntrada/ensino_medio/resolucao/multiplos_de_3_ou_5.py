def solve(limit: int) -> int:
    soma = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            soma += i
    return soma

if __name__ == '__main__':
    print(solve(1000))
