import random


class ECPoint:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


def BasePointGGet():
    pass


def ECPointGen():
    pass


def ECPointGen():
    pass


def IsOnCurveCheck():
    pass


def AddECPoints():
    pass


def DoubleECPoints():
    pass


def ScalarMult():
    pass


def ECPointToString():
    pass


def StringToECPoint():
    pass


def PrintECPoint():
    pass


def SetRandom(bits):
    return random.randint(2 ** (bits - 1), 2 ** bits - 1)


def main():

    G = BasePointGGet()

    k = SetRandom(256)
    d = SetRandom(256)

    H1 = ScalarMult(d, G)
    H2 = ScalarMult(k, H1)
    H3 = ScalarMult(k, G)
    H4 = ScalarMult(d, H3)


if __name__ == '__main__':
    main()
