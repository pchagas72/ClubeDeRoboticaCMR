def solve(limit: int) -> int:
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

if __name__ == '__main__':
    solve(1000)
