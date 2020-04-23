import DataTranslate


def quad_array(sequence):
    final = []
    for i in range(len(sequence)):
        if sequence[i] == "A":
            final.append(0)
        elif sequence[i] == "C":
            final.append(1)
        elif sequence[i] == "T" or i == "U":
            final.append(2)
        elif sequence[i] == "G":
            final.append(3)
        else:
            return "invalid"
    return final


def main():
    nucleotide_header = ""
    seq = []
    print("Welcome to ProjectA!")
    print("Enter (e) at any time to exit")
    print("File input should be in FASTA *.txt format, while console input "
          "will be in raw nucleotide sequence")
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
            if seq != "invalid":
                break
            if seq == "e":
                quit()
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
        print(seq_string)
        seq = quad_array(seq_string)
    while True:
        choice = input(
            "Enter the base translation: (q2d) quaternary to decimal, "
            "(q2b) quaternary to binary, (r)eturn array: ")
        if choice == "q2b":
            print(nucleotide_header + " Binary Form (Base 2)")
            print(DataTranslate.q2b_translation(seq))
        elif choice == "q2d":
            print(nucleotide_header + " Decimal Form (Base 10)")
            print(DataTranslate.q2d_translation(seq))
        elif choice == "r":
            print(nucleotide_header + " Quaternary Array (Base 4)")
            print(seq)
        elif choice == "e":
            quit()
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()


