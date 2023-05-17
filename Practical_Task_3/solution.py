class Cipher:
    def __init__(self, num=str):
        self.num = num

    def s_box(self, table):
        # Extract the left and right halves of the input
        left_val = self.num[:4]
        right_val = self.num[4:]

        # Look up the corresponding values in the S-box table
        new_left_val = table[left_val]
        new_right_val = table[right_val]

        # Create a reversed table for decryption
        reversed_table = {value: key for key, value in table.items()}

        # Return the new values and the reversed table
        return new_left_val + new_right_val, reversed_table

    def p_box(self, table):
        # Rearrange the bits based on the P-box table
        result = [self.num[i - 1] for i in table]
        result = ''.join(result)

        # Create a reversed table for decryption
        reversed_table = [0] * 8
        for i, j in enumerate(table):
            reversed_table[j - 1] = i + 1

        # Return the rearranged bits and the reversed table
        return result, reversed_table
