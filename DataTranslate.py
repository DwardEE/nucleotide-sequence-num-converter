def q2d_translation(sequence):
    seq = sequence[::-1]
    deci_final = 0
    for i in range(len(seq)):
        deci_final += seq[i] * 4 ** i
    return deci_final, len(sequence)


def q2b_translation(sequence):
    deci_intermediate = q2d_translation(sequence)
    return format(deci_intermediate[0], '0' + str(len(sequence) * 2) + 'b')


def q2h_translation(sequence):
    deci_intermediate = q2d_translation(sequence)
    hex_final = hex(deci_intermediate)
    return hex_final, len(sequence)


def d2q_translation(sequence, length):
    dividend = sequence
    if not isinstance(dividend, int):
        return "invalid"
    quart_intermediate = ""
    while dividend > 0:
        quart_intermediate = quart_intermediate + str(int(dividend % 4))
        dividend = dividend // 4
    reversed_quart = quart_intermediate[::-1]
    quart_final = ""
    for i in reversed_quart:
        if i == "0":
            quart_final += "A"
        elif i == "1":
            quart_final += "C"
        elif i == "2":
            quart_final += "G"
        elif i == "3":
            quart_final += "T"
        else:
            return "invalid"
    prefix = length - len(quart_final)
    for i in range(prefix):
        quart_final = "A" + quart_final
    return quart_final
