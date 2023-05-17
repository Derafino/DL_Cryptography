from Practical_Task_3.solution import Cipher


def test_s_box():
    input_data = '10101010'
    c1 = Cipher(input_data)
    input_table = {
        '0000': '1110', '0001': '1010', '0010': '0011', '0011': '1111',
        '0100': '1101', '0101': '0000', '0110': '1000', '0111': '0111',
        '1000': '0110', '1001': '1001', '1010': '1100', '1011': '0001',
        '1100': '1011', '1101': '0101', '1110': '0010', '1111': '0100'
    }

    output_data, output_table = c1.s_box(input_table)
    c2 = Cipher(output_data)
    reversed_data, reversed_table = c2.s_box(output_table)
    assert input_data == reversed_data and input_table == reversed_table


def test_p_box():
    input_data = '11101010'
    c1 = Cipher(input_data)
    input_table = [8, 2, 7, 1, 6, 5, 3, 4]
    output_data, output_table = c1.p_box(input_table)
    c2 = Cipher(output_data)
    reversed_data, reversed_table = c2.p_box(output_table)
    assert input_data == reversed_data and input_table == reversed_table
