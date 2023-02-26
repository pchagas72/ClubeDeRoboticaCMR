"""This is the python code for the 16th challange in projecteuler.com"""


def solve(base: int, power: int) -> int:
    """
    Very pythonic way of doing this, I like it (:
    """
    return sum(int(i) for i in list(str(base**power)))


if __name__ == '__main__':
    print(solve(2, 1000))
