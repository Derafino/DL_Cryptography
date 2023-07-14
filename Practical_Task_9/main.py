import secrets
from typing import Tuple

from ecpy.curves import Curve
from Practical_Task_8.main import get_base_point, scalar_mult, ECPoint

curve = Curve.get_curve('secp256r1')



def generate_keys(base_point) -> Tuple[int, ECPoint]:
    n = curve.order
    privKey = secrets.randbelow(n - 1) + 1
    pubKey = scalar_mult(privKey, base_point)
    return privKey, pubKey


def get_shared_secret(my_private_key: int, their_public_key: ECPoint) -> int:
    shared_point = scalar_mult(my_private_key, their_public_key)
    return shared_point.X


def ecdh_protocol(base_point) -> int:
    privKey1, pubKey1 = generate_keys(base_point)
    privKey2, pubKey2 = generate_keys(base_point)

    shared_secret_1 = get_shared_secret(privKey1, pubKey2)
    shared_secret_2 = get_shared_secret(privKey2, pubKey1)
    print('privKey1:', privKey1)
    print('pubKey1:', pubKey1)
    print('privKey2:', privKey2)
    print('pubKey2:', pubKey2)
    print('shared_secret_1:', shared_secret_1)
    print('shared_secret_2:', shared_secret_2)
    assert shared_secret_1 == shared_secret_2
    return shared_secret_1


def main():
    base_point = get_base_point()
    shared_secret_res = ecdh_protocol(base_point)
    print(f'Shared secret: {shared_secret_res}')


if __name__ == '__main__':
    main()
