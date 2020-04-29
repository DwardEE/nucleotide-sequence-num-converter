from tkinter import *
import DataTranslate
import MainInterface

trans_type = [
    "q2b", "q2d", "q2h",
    "b2q", "d2q", "h2q"
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

input_sequence = Text(frame1, height=10, width=70, fg="grey")
input_sequence.grid(row=0, column=0, columnspan=3)
input_sequence.insert("end", "Insert sequence here...")

read_button = Button(frame1, text="Choose From Files")
read_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

output_sequence = Text(frame3, state="disabled", height=10, width=70)
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
    str_input = input_sequence.get("1.0", "end-1c")
    str_input = str_input.replace("\n", "")
    str_input = str_input.replace(" ", "")
    seq_array = MainInterface.quad_array(str_input)
    output_sequence.configure(state="normal")
    output_sequence.insert("end", DataTranslate.q2b_translation(seq_array))
    output_sequence.configure(state="disabled")


trans_execute_button = Button(frame1, text="Translate",
                              command=translate_execute)
trans_execute_button.grid(row=1, column=2, padx=5, pady=5, sticky="e")

input_sequence.bind("<FocusIn>", focus_in)
input_sequence.bind("<FocusOut>", focus_out)

root.mainloop()
