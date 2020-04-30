def q2d_translation(sequence):
    seq = sequence[::-1]
    deci_final = 0
    for i in range(len(seq)):
        deci_final += seq[i] * 4 ** i
    return deci_final, len(sequence)


def q2b_seg_translation(sequence):
    intermediate = q2b_translation(sequence)
    final = ""
    for i in range(0, len(intermediate), 2):
        final = final + intermediate[i: i+2] + " "
    return final.rstrip()


def q2b_translation(sequence):
    deci_intermediate = q2d_translation(sequence)
    return format(deci_intermediate[0], '0' + str(len(sequence) * 2) + 'b')


def q2h_translation(sequence):
    deci_intermediate = q2d_translation(sequence)[0]
    hex_final = hex(deci_intermediate)
    return hex_final[2:], len(sequence)


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


def h2q_translation(sequence, length):
    deci_intermediate = int(sequence, 16)
    return d2q_translation(deci_intermediate, length)


def b2q_translation(sequence):
    seq = "0" + sequence if len(sequence) % 2 != 0 else sequence
    final = ""
    for i in range(0, len(seq), 2):
        if seq[i] + seq[i + 1] == "00":
            final += "A"
        elif seq[i] + seq[i + 1] == "01":
            final += "C"
        elif seq[i] + seq[i + 1] == "10":
            final += "G"
        elif seq[i] + seq[i + 1] == "11":
            final += "T"
        else:
            return "invalid"
    return final
