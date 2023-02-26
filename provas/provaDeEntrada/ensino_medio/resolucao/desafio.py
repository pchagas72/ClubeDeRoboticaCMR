"""
Essa é uma maneira bem "pythonica" de resolver este problema, se você não entender, está tudo bem!
Pode falar comigo (chagas) se quiser que eu explique.
"""


def solve(base: int, power: int) -> int:
    return sum(int(i) for i in list(str(base**power)))


if __name__ == '__main__':
    print(solve(2, 1000))
