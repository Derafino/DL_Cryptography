import random


class Tests:
    def __init__(self, bit_sequence):
        self.bit_sequence = bit_sequence

    def monobit_test(self):
        return 9654 < self.bit_sequence.count('0') < 10346

    def max_length_series_test(self):
        prev_bit = None
        series = 0
        max_series = 0

        for bit in self.bit_sequence:
            if bit == prev_bit:
                series += 1
                max_series = max(max_series, series)
            else:
                series = 1
                prev_bit = bit
        return max_series <= 36

    def poker_test(self):
        m = 4
        k = len(self.bit_sequence) // m
        blocks = {}

        for i in range(k):
            block = self.bit_sequence[i * m: (i + 1) * m]
            if block in blocks:
                blocks[block] += 1
            else:
                blocks[block] = 1
        sum_ni = sum([n ** 2 for n in blocks.values()])
        X3 = (((2 ** m) / k) * sum_ni) - k
        return 1.03 < X3 < 57.4

    def series_lengths_test(self):
        series_lengths_0 = {6: 0}
        series_lengths_1 = {6: 0}
        prev_bit = None
        temp_length = 0

        for bit in self.bit_sequence:
            if bit == prev_bit:
                temp_length += 1
            else:
                if temp_length > 0:
                    if prev_bit == '0':
                        if temp_length in series_lengths_0:
                            series_lengths_0[temp_length] += 1
                        elif temp_length > 6:
                            series_lengths_0[6] += 1
                        else:
                            series_lengths_0[temp_length] = 1
                    else:
                        if temp_length in series_lengths_1:
                            series_lengths_1[temp_length] += 1
                        elif temp_length > 6:
                            series_lengths_1[6] += 1
                        else:
                            series_lengths_1[temp_length] = 1
                temp_length = 1
                prev_bit = bit

        if 2267 < series_lengths_0[1] < 2733 and \
                1079 < series_lengths_0[2] < 1421 and \
                502 < series_lengths_0[3] < 748 and \
                402 > series_lengths_0[4] > 223 > series_lengths_0[5] > 90 and \
                90 < series_lengths_0[6] < 223 and \
                2267 < series_lengths_1[1] < 2733 and \
                1079 < series_lengths_1[2] < 1421 and \
                502 < series_lengths_1[3] < 748 and \
                402 > series_lengths_1[4] > 223 > series_lengths_1[5] > 90 and \
                90 < series_lengths_1[6] < 223:
            return True
        else:
            return False


def main():
    bit_sequence = ''.join(str(random.choice([0, 1])) for _ in range(20000))

    t = Tests(bit_sequence)
    monobit_test_result = t.monobit_test()
    max_length_series_test_result = t.max_length_series_test()
    poker_test_result = t.poker_test()
    series_lengths_test_result = t.series_lengths_test()

    print("Monobit Test:", monobit_test_result)
    print("Max Length Series Test:", max_length_series_test_result)
    print("Poker Test:", poker_test_result)
    print("Series Length Test:", series_lengths_test_result)
    if monobit_test_result and max_length_series_test_result and poker_test_result and series_lengths_test_result:
        print('The sequence of bits is sufficiently random')
    else:
        print('The sequence of bits does not meet the criteria for randomness and should be rejected')


if __name__ == '__main__':
    main()
