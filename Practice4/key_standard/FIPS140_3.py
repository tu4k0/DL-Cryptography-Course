def monobit_test(bits):
    bits_1 = 0
    for i in range(len(bits)):
        if bits[i] == '1':
            bits_1 += 1
    if 9654 < bits_1 < 10346:
        status = True
    else:
        status = False

    return status


def maximum_length_of_the_series_test(bits):
    counter = 1
    series = 1
    for i in range(len(bits)):
        if i == len(bits) - 1:
            break
        if bits[i] == bits[i+1]:
            counter += 1
        elif bits[i] != bits[i+1]:
            if series < counter:
                series = counter
            counter = 1
    if series > 36:
        status = False
    else:
        status = True

    return status


def pokker_test(bits):
    start = 0
    end = 4
    bits_block = []
    m = 4
    n = 0
    pokker_blocks = ['0000', '0001', '0011', '0111',
                     '1111', '0101', '1010', '1110',
                     '1100', '1000', '1101', '1001',
                     '1011', '0110', '0100', '0010']
    for i in range(len(bits) // m):
        bits_block.append(bits[start:end])
        start += 4
        end += 4
    k = len(bits_block)
    for pokker_block in pokker_blocks:
        n += bits_block.count(pokker_block) ** 2
    X_3 = (((2 ** m) / k) * (n)) - k
    if 1.03 < X_3 < 57.4:
        status = True
    else:
        status = False

    return status


def series_length_test(bits):
    counter = 0
    series_1_length = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    series_0_length = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    for i in range(len(bits)):
        if i == len(bits) - 1:
            break
        elif bits[i] == '0' and bits[i+1] == '1':
            while bits[i+1] != '0':
                counter += 1
                i += 1
                if i + 1 == len(bits):
                    break
            if counter > 6:
                series_1_length['6'] += 1
            else:
                series_1_length[str(counter)] += 1
            counter = 0
        else:
            pass
    for i in range(len(bits)):
        if i == len(bits) - 1:
            break
        elif bits[i] == '1' and bits[i+1] == '0':
            while bits[i+1] != '1':
                counter += 1
                i += 1
                if i + 1 == len(bits):
                    break
            if counter > 6:
                series_0_length['6'] += 1
            else:
                series_0_length[str(counter)] += 1
            counter = 0
        else:
            pass
    if 2267 < series_1_length['1'] < 2733 and 1079 < series_1_length['2'] < 1421 and 502 < series_1_length['3'] < 748 and 223 < series_1_length['4'] < 402 and 90 < series_1_length['5'] < 223 and 90 < series_1_length['6'] < 223:
        if 2267 < series_0_length['1'] < 2733 and 1079 < series_0_length['2'] < 1421 and 502 < series_0_length['3'] < 748 and 223 < series_0_length['4'] < 402 and 90 < series_0_length['5'] < 223 and 90 < series_0_length['6'] < 223:
            status = True
        else:
            status = False
    else:
        status = False

    return status
