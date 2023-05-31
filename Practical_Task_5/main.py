import hashlib
import tracemalloc
import time

from functools import wraps


def resources(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()

        tracemalloc.start()

        result = func(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        tracemalloc.stop()
        memory_usage = sum(stat.size for stat in top_stats)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(f"Function '{func.__name__}' executed in {execution_time:.10f} seconds.")
        print(f"Memory usage: {memory_usage} bytes")

        return result

    return wrapper


@resources
def lib_sha1(data):
    h = hashlib.sha1(data)
    return h.hexdigest()


def rotate_left(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


@resources
def my_sha1(data):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    ml = len(data) * 8
    data += b'\x80'
    while (len(data) * 8) % 512 != 448:
        data += b'\x00'
    data += ml.to_bytes(8, byteorder='big')

    for i in range(0, len(data), 64):
        chunk = data[i:i + 64]

        w = [0] * 80
        for j in range(16):
            w[j] = int.from_bytes(chunk[j * 4:j * 4 + 4], byteorder='big')

        for j in range(16, 80):
            w[j] = rotate_left(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for k in range(80):
            if k <= 19:
                f = (b & c) | ((~b) & d)
                k_const = 0x5A827999
            elif 20 <= k <= 39:
                f = b ^ c ^ d
                k_const = 0x6ED9EBA1
            elif 40 <= k <= 59:
                f = (b & c) | (b & d) | (c & d)
                k_const = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k_const = 0xCA62C1D6

            temp = rotate_left(a, 5) + f + e + k_const + w[k] & 0xFFFFFFFF
            e = d
            d = c
            c = rotate_left(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
    digest = (h0.to_bytes(4, byteorder='big') +
              h1.to_bytes(4, byteorder='big') +
              h2.to_bytes(4, byteorder='big') +
              h3.to_bytes(4, byteorder='big') +
              h4.to_bytes(4, byteorder='big'))
    return ''.join(format(byte, '02x') for byte in digest)


def main():
    print()

    data = b'input data'

    my_hashed_data = my_sha1(data)
    print('Hashed data:', my_hashed_data)

    print()

    lib_hashed_data = lib_sha1(data)
    print('Hashed data:', lib_hashed_data)


if __name__ == '__main__':
    main()
