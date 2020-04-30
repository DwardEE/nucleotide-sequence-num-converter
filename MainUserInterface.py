from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tks
import DataTranslate
import ConsoleInterface
from ttkthemes import ThemedTk

trans_type = [
    "q2b", "q2d", "q2h",
    "b2q", "d2q", "h2q"
]

R_or_DNA = [
    "DNA", "RNA"
]

sequence_type = "Sequence"


def focus_in(_):
    if input_sequence.cget("fg") == "grey":
        input_sequence.delete('1.0', "end")
        input_sequence.config(fg='black')


def focus_out(_):
    if input_sequence.compare("end-1c", "==", "1.0"):
        input_sequence.config(fg='grey')
        input_sequence.insert("end", "Insert sequence here...")


root = ThemedTk(theme="plastik")
root.title("Nucleotide Sequence Base Converter")

style = ttk.Style()
style.theme_use()

seq_trans = StringVar()
seq_trans.set(0)

nuc_type = StringVar()
nuc_type.set(R_or_DNA[0])

segmented_binary = IntVar()
segmented_binary.set(0)

frame0 = LabelFrame(root, text="Sequence Details", padx=5, pady=5)
frame0.pack(padx=15, pady=(15, 5))

frame1 = LabelFrame(root, text=sequence_type, padx=5, pady=5)
frame1.pack(padx=15, pady=5)

frame2 = LabelFrame(root, text="Conversion Options", padx=5, pady=5)
frame2.pack(padx=15, pady=5)

frame3 = LabelFrame(root, text="Conversion", padx=5, pady=5)
frame3.pack(padx=15, pady=(5, 15))

input_sequence = tks.ScrolledText(frame1, height=10, width=72, fg="grey")
input_sequence.grid(row=0, column=0, columnspan=3)
input_sequence.insert("end", "Insert sequence here...")

read_button = ttk.Button(frame1, text="Choose From Files")
read_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

output_sequence = tks.ScrolledText(frame3, state="disabled", height=10,
                                   width=72)
output_sequence.grid(row=0, column=0, columnspan=3)

write_button = ttk.Button(frame3, text="Write Results to File")
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

Label(frame2, text='Additional Options').grid(row=0, column=2, sticky="w")
seg_binary_button = Checkbutton(frame2, text="Segmented Binary",
                                variable=segmented_binary)
seg_binary_button.grid(row=1, column=2)

length_label = Label(frame0, text="Sequence Length (Base 4):")
length_label.grid(row=0, column=0, sticky="w", padx=(0, 3))

seq_length = Text(frame0, height=1, width=10)
seq_length.grid(row=0, column=1, sticky="w", padx=(0, 154))

nucleotide_seq_type = ttk.Combobox(frame0, values=R_or_DNA, width=5)
nucleotide_seq_type.set(nuc_type.get())
nucleotide_seq_type.grid(row=0, column=4, sticky="w", padx=(0, 5))
seq_type_label = Label(frame0, text="Nucleotide Sequence Type")
seq_type_label.grid(row=0, column=3, padx=(0, 3))


def translate_execute():
    output_sequence.configure(state="normal")
    str_input = input_sequence.get("1.0", "end-1c")
    str_input = str_input.replace("\n", "")
    str_input = str_input.replace(" ", "")
    output_sequence.delete('1.0', "end")
    if seq_trans.get()[0] == "q":
        seq_array = ConsoleInterface.quad_array(str_input)
        seq_length.delete('1.0', "end")
        seq_length.insert("end", len(seq_array))
        if seq_trans.get() == "q2b":
            if segmented_binary.get() == 1:
                output_sequence.insert("end", DataTranslate.q2b_seg_translation(
                    seq_array))
            else:
                output_sequence.insert("end", DataTranslate.q2b_translation(
                    seq_array))
        elif seq_trans.get() == "q2d":
            output_sequence.insert("end", DataTranslate.q2d_translation(
                seq_array)[0])
        elif seq_trans.get() == "q2h":
            output_sequence.insert("end", DataTranslate.q2h_translation(
                seq_array)[0])
    else:
        if seq_trans.get() == "b2q":
            output_sequence.insert("end", DataTranslate.b2q_translation(
                str_input))
        elif seq_trans.get() == "d2q":
            output_sequence.insert("end", DataTranslate.d2q_translation(
                int(str_input), int(seq_length.get('1.0', "end"))))
        elif seq_trans.get() == "h2q":
            output_sequence.insert("end", DataTranslate.h2q_translation(
                str_input, int(seq_length.get('1.0', "end"))))

    output_sequence.configure(state="disabled")


trans_execute_button = ttk.Button(frame1, text="Convert",
                                  command=translate_execute)
trans_execute_button.grid(row=1, column=2, padx=5, pady=5, sticky="e")

input_sequence.bind("<FocusIn>", focus_in)
input_sequence.bind("<FocusOut>", focus_out)

root.mainloop()
