divisors_test_list: list[int] = list(range(1, 11))
divisors_final_list: list[int] = list(range(10, 21))

def solve(divisors_list: list[int]) -> int:
    step = divisor = max(divisors_list)
    searching = True
    while searching:
        if all(divisor % i == 0 for i in divisors_list):
            return divisor
        divisor += step

    return 0


def get_answers() -> tuple[int, int]:
    test_answer = solve(divisors_test_list)
    final_answer = solve(divisors_final_list)
    print(f'The test answer is {test_answer}')
    print(f'The final answer is {final_answer}')
    return (test_answer, final_answer)


if __name__ == '__main__':
    get_answers()
