# Practical_Task_3


Власна програмна реалізація алгоритмів S-блоку та P-блоку(пряме та зворотне перетворення).

## Приклади роботи:

S-блок:
```python
input_data = '10101010'
print('input_data:', input_data) # input_data: 10101010
c1 = Cipher(input_data)
input_table = {
    '0000': '1110', '0001': '1010', '0010': '0011', '0011': '1111',
    '0100': '1101', '0101': '0000', '0110': '1000', '0111': '0111',
    '1000': '0110', '1001': '1001', '1010': '1100', '1011': '0001',
    '1100': '1011', '1101': '0101', '1110': '0010', '1111': '0100'
}

output_data, output_table = c1.s_box(input_table)
print('output_data:', output_data) # output_data: 11001100
print('output_table:', output_table) # output_table: {'1110': '0000', '1010': '0001', '0011': '0010', '1111': '0011', '1101': '0100', '0000': '0101', '1000': '0110', '0111': '0111', '0110': '1000', '1001': '1001', '1100': '1010', '0001': '1011', '1011': '1100', '0101': '1101', '0010': '1110', '0100': '1111'}

c2 = Cipher(output_data)
reversed_data, reversed_table = c2.s_box(output_table)
print('reversed_data:', reversed_data) # reversed_data: 10101010
print('reversed_table:', reversed_table) # reversed_table: {'0000': '1110', '0001': '1010', '0010': '0011', '0011': '1111', '0100': '1101', '0101': '0000', '0110': '1000', '0111': '0111', '1000': '0110', '1001': '1001', '1010': '1100', '1011': '0001', '1100': '1011', '1101': '0101', '1110': '0010', '1111': '0100'}
```



P-блок:
```python
input_data = '11101010'
print('input_data:', input_data) # input_data: 11101010
c1 = Cipher(input_data)
input_table = [8, 2, 7, 1, 6, 5, 3, 4]
output_data, output_table = c1.p_box(input_table)
print('output_data:', output_data) # output_data: 01110110
print('output_table:', output_table) # output_table: [4, 2, 7, 8, 6, 5, 3, 1]
c2 = Cipher(output_data)
reversed_data, reversed_table = c2.p_box(output_table)
print('reversed_data:', reversed_data) # reversed_data: 11101010
print('reversed_table:', reversed_table) # reversed_table: [8, 2, 7, 1, 6, 5, 3, 4]
```
