import random
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend


class ECPoint:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


def BasePointGGet():
    curve = ec.SECP256R1()
    private_key = ec.generate_private_key(curve, default_backend())
    public_key = private_key.public_key()
    public_numbers = public_key.public_numbers()
    return ECPoint(public_numbers.x, public_numbers.y)


def ECPointGen(x: int, y: int) -> ECPoint:
    return ECPoint(x, y)


def IsOnCurveCheck(a: ECPoint) -> bool:
    curve = ec.SECP256R1()
    public_numbers = ec.EllipticCurvePublicNumbers(a.X, a.Y, curve)
    public_key = public_numbers.public_key(default_backend())

    return public_key.public_numbers().x is not None


def AddECPoints(a: ECPoint, b: ECPoint) -> ECPoint:
    if a.X == b.X and a.Y == b.Y:
        s = ((3 * a.X * a.X) / (2 * a.Y))
    else:
        s = (b.Y - a.Y) / (b.X - a.X)
    x3 = s * s - a.X - b.X
    y3 = s * (a.X - x3) - a.Y

    return ECPoint(x3, y3)


def DoubleECPoints(a: ECPoint) -> ECPoint:
    s = (3 * a.X * a.X) / (2 * a.Y)
    x3 = s * s - 2 * a.X
    y3 = s * (a.X - x3) - a.Y

    return ECPoint(x3, y3)


def ScalarMult(k: int, a: ECPoint) -> ECPoint:
    result = None
    while k > 0:
        if k % 2 == 1:
            result = AddECPoints(result, a)
        a = DoubleECPoints(a)
        k //= 2
    return result


def ECPointToString(point: ECPoint) -> str:
    return f"X:{point.X}, Y:{point.Y}"


def StringToECPoint(s: str) -> ECPoint:
    x, y = s.split(",")
    return ECPoint(int(x), int(y))


def PrintECPoint(point: ECPoint) -> None:
    print(ECPointToString(point))


def SetRandom(bits):
    return random.randint(2 ** (bits - 1), 2 ** bits - 1)


def main():
    G = BasePointGGet()
    print(G)
    k = SetRandom(256)
    d = SetRandom(256)

    H1 = ScalarMult(d, G)
    H2 = ScalarMult(k, H1)
    H3 = ScalarMult(k, G)
    H4 = ScalarMult(d, H3)


if __name__ == '__main__':
    main()
