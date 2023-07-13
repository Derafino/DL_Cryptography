import hashlib
import secrets
from typing import Tuple

from ecpy.curves import Curve
from Practical_Task_8.main import get_base_point, ECPoint, scalar_mult, add_ECPoints
from Practical_Task_9.main import generate_keys

curve = Curve.get_curve('secp256r1')
base_point = get_base_point()
print('base_point', base_point.X, base_point.Y)


def hash_message(message: str) -> int:
    hashed_message = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    return hashed_message


def generate_signature(private_key: int, message: str) -> Tuple[int, int]:
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


def verify_signature(public_key: ECPoint, message: str, signature: Tuple[int, int]) -> bool:
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
    private_key, public_key = generate_keys()
    message = "test message"
    signature = generate_signature(private_key, message)
    print('Signature:', signature)
    is_valid = verify_signature(public_key, message, signature)
    print("Valid:", is_valid)


if __name__ == "__main__":
    main()
