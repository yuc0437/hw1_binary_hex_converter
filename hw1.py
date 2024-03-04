decimal_num = int(input("輸入介於0-255的10進位數字："))

def decimal_to_binary(decimal_num):
    binary_num = []
    power_7 = 128
    power_6 = 64
    power_5 = 32
    power_4 = 16
    power_3 = 8
    power_2 = 4
    power_1 = 2
    power_0 = 1
    
    powers = [power_7, power_6, power_5, power_4, power_3, power_2, power_1, power_0]
    
    for power in powers:
        if decimal_num >= power:
            binary_num.append(1)
            decimal_num -= power
        else:
            binary_num.append(0)
    
    return binary_num

def binary_to_hex(binary_num):
    hex_digits = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }
    
    grouped_binary = [binary_num[i:i+4] for i in range(0, 8, 4)]
    
    hex_num = ""
    for group in grouped_binary:
        hex_num += hex_digits["".join(map(str, group))]
    
    return hex_num

binary_num = decimal_to_binary(decimal_num)
hex_num = binary_to_hex(binary_num)

print("二進位數字：", binary_num)
print("16進位數字：", hex_num)
