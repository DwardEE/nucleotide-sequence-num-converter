from tkinter import *
import DataTranslate

trans_type = [
    "q2b", "q2d", "q2h",
    "b2q", "d2q", "h2q"
]
sequence_type = "Sequence"

root = Tk()
root.title("Nucleotide Sequence Translator")

seq_trans = StringVar()
seq_trans.set("q2b")

frame1 = LabelFrame(root, text=sequence_type, padx=5, pady=5)
frame1.pack(padx=15, pady=(15, 5))

frame2 = LabelFrame(root, text="Settings", padx=5, pady=5)
frame2.pack(padx=15, pady=5, anchor="w")

frame3 = LabelFrame(root, text="Translation", padx=5, pady=5)
frame3.pack(padx=15, pady=(5, 15))

input_sequence = Text(frame1, height=10, width=70)
input_sequence.grid(row=0, column=0, columnspan=3)
input_sequence.insert(END, "Insert sequence here...")

read_button = Button(frame1, text="Browse Files")
read_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

output_sequence = Text(frame3, height=10, width=70)
output_sequence.grid(row=0, column=0, columnspan=3)

write_button = Button(frame3, text="Write Results to File")
write_button.grid(row=1, column=2, padx=5, pady=5, sticky="e")

type_label = Label(frame2, text="Translation Type")
q2b_button = Radiobutton(frame2, text="Quaternary to Binary",
                         variable=seq_trans, value=trans_type[0])
q2d_button = Radiobutton(frame2, text="Quaternary to Decimal",
                         variable=seq_trans, value=trans_type[1])
q2h_button = Radiobutton(frame2, text="Quaternary to Hexadecimal",
                         variable=seq_trans, value=trans_type[2])
b2q_button = Radiobutton(frame2, text="Binary to Quaternary",
                         variable=seq_trans, value=trans_type[3])
d2q_button = Radiobutton(frame2, text="Decimal to Quaternary",
                         variable=seq_trans, value=trans_type[4])
h2q_button = Radiobutton(frame2, text="Hexadecimal to Quaternary",
                         variable=seq_trans, value=trans_type[5])
type_label.grid(row=0, column=0, sticky="w")
q2b_button.grid(row=1, column=0, sticky="w")
q2d_button.grid(row=2, column=0, sticky="w")
q2h_button.grid(row=3, column=0, sticky="w")
b2q_button.grid(row=1, column=1, sticky="w")
d2q_button.grid(row=2, column=1, sticky="w")
h2q_button.grid(row=3, column=1, sticky="w")


def translate_execute():
    if trans_type == "q2b":
        my_label = Label(root, text="q2b")
        my_label.pack()
    elif trans_type == "q2d":
        my_label = Label(root, text="q2d")
        my_label.pack()


trans_execute_button = Button(frame1, text="Translate",
                              command=translate_execute)
trans_execute_button.grid(row=1, column=2, padx=5, pady=5, sticky="e")

root.mainloop()
