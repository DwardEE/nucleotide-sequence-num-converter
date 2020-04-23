def q2d_translation(sequence):
    deci_final = 0
    for i in reversed(range(len(sequence))):
        deci_final += sequence[i] * 4 ** i
    return deci_final


def q2b_translation(sequence):
    deci_intermediate = q2d_translation(sequence)
    bin_final = bin(deci_intermediate)
    return bin_final