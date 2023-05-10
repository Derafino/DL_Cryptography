class LargeNumber:
    def __init__(self, number=None):
        if number is None:
            number = list()
        self.number = number

    def set_hex(self, hex_string):
        binary_string = ''.join([bin(int(x, 16))[2:].zfill(4) for x in hex_string])
        self.number = [int(x) for x in binary_string]

    def get_hex(self):
        binary_string = ''.join(str(bit) for bit in self.number)
        decimal_value = int(binary_string, 2)
        hex_string = hex(decimal_value)[2:]
        return hex_string

    def INV(self):
        self.number = [int(not i) for i in self.number]

    @staticmethod
    def XOR(a, b):
        result = list()
        for i in range(len(a.number)):
            if a.number[i] == b.number[i]:
                result.append(0)
            else:
                result.append(1)
        return LargeNumber(result)

    @staticmethod
    def OR(a, b):
        return LargeNumber([1 if i or j else 0 for i, j in zip(a.number, b.number)])

    @staticmethod
    def AND(a, b):
        return LargeNumber([1 if i and j else 0 for i, j in zip(a.number, b.number)])

    def shiftR(self, bits):
        self.number = self.number[-bits:] + self.number[:-bits]

    def shiftL(self, bits):
        self.number = self.number[bits:] + self.number[:bits]

    @staticmethod
    def ADD(a, b):
        temp = 0
        result = []
        for i in range(len(a.number) - 1, -1, -1):
            sum_val = a.number[i] + b.number[i] + temp
            result.insert(0, sum_val % 2)
            temp = sum_val // 2
        if temp:
            result.insert(0, 1)
        return LargeNumber(result)

    @staticmethod
    def SUB(a, b):
        result = []
        temp = 0
        for i in range(len(a.number) - 1, -1, -1):
            diff = a.number[i] - b.number[i] - temp
            if diff < 0:
                result.insert(0, diff + 2)
                temp = 1
            else:
                result.insert(0, diff)
                temp = 0
        while result[0] == 0 and len(result) > 1:
            del result[0]
        return LargeNumber(result)
