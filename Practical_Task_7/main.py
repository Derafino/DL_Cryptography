import random
import hashlib


def generate_keys(p, g):
    a = random.randint(1, p - 2)
    b = pow(g, a, p)
    return a, b


def sign(message, p, g, a):
    k = random.randint(1, p - 2)
    r = pow(g, k, p)
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    s = ((h - a * r) * 1 // k) % (p - 1)
    return r, s


def verify(message, r, s, p, g, b):
    m = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    y = (1 // b) % p
    u1 = (m * 1 // s) % (p - 1)
    u2 = (r * 1 // s) % (p - 1)
    v = (pow(g, u1, p) * pow(y, u2, p)) % p
    return v == r


def main():
    bit_sequence = ''.join(str(random.choice([0, 1])) for _ in range(2048, 4096))
    p = int(bit_sequence, 2)

    g = random.randint(1, p - 1)
    a, b = generate_keys(p, g)

    message = input("message:")
    r, s = sign(message, p, g, a)

    valid = verify(message, r, s, p, g, b)

    print("message:", message)
    print("signature:", (r, s))
    print("verified:", valid)


if __name__ == '__main__':
    main()
