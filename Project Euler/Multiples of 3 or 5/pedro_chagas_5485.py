"""Resolução do primeiro problema do site projecteuler.net"""


def solve(limit: int) -> int:
    """
    Função principal para resolver o problema, recebe o limite
    como input e entrega a quantidade de múltiplos de 3 ou 5.
    """

    multiples_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            multiples_sum += 1
    return multiples_sum


if __name__ == "__main__":
    solution = solve(1000)
    print(solution)
