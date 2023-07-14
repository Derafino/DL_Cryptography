import secrets

from typing import Tuple
from ecpy.curves import Curve
from Practical_Task_5.main import my_sha1
from Practical_Task_8.main import add_ECPoints, get_base_point, scalar_mult, ECPoint
from Practical_Task_9.main import generate_keys

curve = Curve.get_curve('secp256r1')


def hash_message(message: str) -> int:
    return int(my_sha1(message.encode()), 16)


def generate_signature(private_key: int, message: str, base_point) -> Tuple[int, int]:
    z = hash_message(message)
    n = curve.order
    r = 0
    s = 0
    while not r or not s:
        k = secrets.randbelow(n - 1) + 1
        point = scalar_mult(k, base_point)
        r = point.X % n
        if r == 0:
            continue
        s = ((z + r * private_key) * pow(k, -1, n)) % n
    return r, s


def verify_signature(public_key: ECPoint, message: str, signature: Tuple[int, int], base_point) -> bool:
    z = hash_message(message)
    n = curve.order
    r, s = signature
    s_inv = pow(s, -1, n)
    u1 = (z * s_inv) % n
    u2 = (r * s_inv) % n
    point = add_ECPoints(scalar_mult(u1, base_point), scalar_mult(u2, public_key))
    if point.X == r:
        return True
    else:
        return False


def main():
    base_point = get_base_point()
    private_key, public_key = generate_keys(base_point)
    print("Generated Public Key:", public_key.X, public_key.Y)
    message = "test message"
    signature = generate_signature(private_key, message, base_point)
    print('Signature:', signature)
    is_valid = verify_signature(public_key, message, signature, base_point)
    print("Valid:", is_valid)


if __name__ == "__main__":
    main()
