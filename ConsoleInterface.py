import DataTranslate


def quad_array(sequence):
    final = []
    for i in range(len(sequence)):
        if sequence[i] == "A":
            final.append(0)
        elif sequence[i] == "C":
            final.append(1)
        elif sequence[i] == "G":
            final.append(2)
        elif sequence[i] == "T" or i == "U":
            final.append(3)
        else:
            return "invalid"
    return final


def write_file(sequence, name, filename):
    f = open(filename, "a")
    f.write(">" + name + "\n")
    for i in range(0, len(sequence), 70):
        f.write(sequence[i:i+70] + "\n")
    f.close()


def quaternary_translator():
    nucleotide_header = ""
    seq = []
    while True:
        method = input("Select method of input, (f)ile (c)onsole: ")
        if method == "c" or method == "f":
            break
        if method == "e":
            quit()
    if method == "c":
        while True:
            nucleotide_header = input("Enter the nucleotide sequence's "
                                      "name: ")
            if nucleotide_header == "e":
                quit()
            seq = quad_array(input("Enter the nucleotide sequence: "))
            if seq == "e":
                quit()
            if seq != "invalid":
                break
    elif method == "f":
        seq_string = ""
        while True:
            filename = input("Enter filename: ")
            if filename == "e":
                quit()
            f = open(filename, "r")
            if f.mode == "r":
                break
        f1 = f.readlines()
        nucleotide_header = f1[0][1:-1]
        for i in range(1, len(f1)):
            seq_string = seq_string + f1[i][:-1]
        seq = quad_array(seq_string)
    while True:
        choice = input(
            "Enter the base translation: (q2d) quaternary to decimal, "
            "(q2b) quaternary to binary, (q2h) quaternary to hexadecimal ("
            "r)eturn array: ")
        if choice == "q2b":
            print(nucleotide_header + " Binary Form/Base 2")
            print(DataTranslate.q2b_translation(seq))
            write_input = input(
                "Would you like to write the results to a file? (y) or (n) ")
            if write_input == "e" or write_input == "n":
                quit()
            if write_input == "y":
                filename = input("Which file do you want to write to? ")
                write_file(DataTranslate.q2b_translation(seq),
                           nucleotide_header,  filename)
        elif choice == "q2d":
            print(nucleotide_header + " Decimal Form/Base 10 (value, "
                                      "sequence length)")
            print(DataTranslate.q2d_translation(seq))
            write_input = input(
                "Would you like to write the results to a file? (y) or (n) ")
            if write_input == "e" or write_input == "n":
                quit()
            elif write_input == "y":
                filename = input("Which file do you want to write to? ")
                write_file(DataTranslate.q2d_translation(seq),
                           nucleotide_header, filename)
        elif choice == "q2h":
            print(nucleotide_header + " Hexadecimal Form/Base 16(value, "
                                      "sequence length)")
            print(DataTranslate.q2h_translation(seq))
            write_input = input(
                "Would you like to write the results to a file? (y) or (n) ")
            if write_input == "e" or write_input == "n":
                quit()
            elif write_input == "y":
                filename = input("Which file do you want to write to? ")
                write_file(DataTranslate.q2h_translation(seq),
                           nucleotide_header, filename)
        elif choice == "r":
            print(nucleotide_header + " Quaternary Array/Base 4 Array")
            print(seq)
        elif choice == "e":
            quit()
        else:
            print("Invalid input")


def translate2quaternary():
    nucleotide_header = input("Enter the name of the nucleotide sequence: ")
    if nucleotide_header == "e":
        quit()
    base = input("Which base would you like to translate from (2), (10), "
                 "(16): ")
    if base == "e":
        quit()
    elif base == "10":
        seq = input("Please input the decimal string: ")
        length = input("Please input the sequence length: ")
        print(">" + nucleotide_header)
        print(DataTranslate.d2q_translation(int(seq), int(length)))
    elif base == "16":
        seq = input("Please input the hexadecimal string: ")
        length = input("Please input the sequence length: ")
        print(">" + nucleotide_header)
        print(DataTranslate.h2q_translation(int(seq), int(length)))
    elif base == "2":
        seq = input("Please input the binary string: ")
        print(">" + nucleotide_header)
        print(DataTranslate.b2q_translation(seq))


def main():
    print("Welcome to ProjectA!")
    print("Enter (e) at any time to exit")
    mode = input("Nucleotide sequence (t)ranslation or translation to ("
                 "q)uaternary nucleotide sequence: ")
    if mode == "t":
        print("File input should be in FASTA *.txt format, while console input "
              "will be in raw nucleotide sequence")
        quaternary_translator()
    elif mode == "q":
        translate2quaternary()


if __name__ == "__main__":
    main()
