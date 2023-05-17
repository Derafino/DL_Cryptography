class Cipher:
    def __init__(self, num=str):
        self.num = num

    def s_box(self, table):
        # Розділ вхіднохо значення на дві частини по 4 біта
        left_val = self.num[:4]
        right_val = self.num[4:]

        # Пошук відповідних значень з table
        new_left_val = table[left_val]
        new_right_val = table[right_val]

        # Створення таблиці для зворотного перетворення
        reversed_table = {value: key for key, value in table.items()}

        return new_left_val + new_right_val, reversed_table

    def p_box(self, table):
        # Перестановка бітів згідно table
        result = [self.num[i - 1] for i in table]
        result = ''.join(result)

        # Створення таблиці для зворотного перетворення
        reversed_table = [0] * 8
        for i, j in enumerate(table):
            reversed_table[j - 1] = i + 1

        return result, reversed_table
