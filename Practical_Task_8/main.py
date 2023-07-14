import os
from typing import Tuple

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from ecpy.curves import Curve, Point

curve = Curve.get_curve('secp256r1')


class ECPoint:
    def __init__(self, x: int, y: int) -> None:
        self.X = x
        self.Y = y


def generate_private_key() -> ec.EllipticCurvePrivateKey:
    return ec.generate_private_key(ec.SECP256R1(), default_backend())


def get_public_key(private_key: ec.EllipticCurvePrivateKey) -> ec.EllipticCurvePublicKey:
    return private_key.public_key()


def get_public_numbers(public_key: ec.EllipticCurvePublicKey) -> ec.EllipticCurvePublicNumbers:
    return public_key.public_numbers()


def get_base_point() -> ECPoint:
    private_key = generate_private_key()
    public_key = get_public_key(private_key)
    numbers = get_public_numbers(public_key)
    return ECPoint(numbers.x, numbers.y)


def generate_ECPoint(x: int, y: int) -> ECPoint:
    numbers = ec.EllipticCurvePublicNumbers(x, y, ec.SECP256R1())
    return ECPoint(numbers.x, numbers.y)


def is_on_curve(point: ECPoint) -> bool:
    try:
        generate_ECPoint(point.X, point.Y)
        return True
    except:
        return False


def add_ECPoints(a: ECPoint, b: ECPoint) -> ECPoint | None:
    point_a = Point(a.X, a.Y, curve)
    point_b = Point(b.X, b.Y, curve)
    result = curve.add_point(point_a, point_b)
    return ECPoint(result.x, result.y)


def double_ECPoint(a: ECPoint) -> ECPoint:
    point_a = Point(a.X, a.Y, curve)
    result = point_a + point_a
    return ECPoint(result.x, result.y)


def scalar_mult(k: int, a: ECPoint) -> ECPoint:
    point_a = Point(a.X, a.Y, curve)
    result = k * point_a
    return ECPoint(result.x, result.y)


def ECPoint_to_string(point: ECPoint) -> str:
    numbers = ec.EllipticCurvePublicNumbers(point.X, point.Y, ec.SECP256R1())
    public_key = numbers.public_key(default_backend())
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem.decode('utf-8')


def string_to_ECPoint(s: str) -> ECPoint:
    pem = s.encode('utf-8')
    public_key = serialization.load_pem_public_key(pem, default_backend())
    numbers = public_key.public_numbers()
    return ECPoint(numbers.x, numbers.y)


def print_ECPoint(point: ECPoint) -> None:
    print(f'point: ({point.X}, {point.Y})')


def get_valid_point() -> Tuple[int, int]:
    private_key = generate_private_key()
    public_key = get_public_key(private_key)
    numbers = get_public_numbers(public_key)
    return numbers.x, numbers.y


def set_random(bit_length: int) -> int:
    return int.from_bytes(os.urandom(bit_length // 8), 'big')


def is_equal(a: ECPoint, b: ECPoint) -> bool:
    return a.X == b.X and a.Y == b.Y


def main():
    G = get_base_point()
    print_ECPoint(G)

    x, y = get_valid_point()
    point = generate_ECPoint(x, y)
    print_ECPoint(point)

    print(is_on_curve(point))

    s = ECPoint_to_string(point)
    print(s)

    point2 = string_to_ECPoint(s)
    print_ECPoint(point2)
    k = set_random(256)
    d = set_random(256)

    H1 = scalar_mult(d, G)
    H2 = scalar_mult(k, H1)
    H3 = scalar_mult(k, G)
    H4 = scalar_mult(d, H3)

    result = is_equal(H2, H4)
    print(f'Equation result: {result}')


if __name__ == '__main__':
    main()
