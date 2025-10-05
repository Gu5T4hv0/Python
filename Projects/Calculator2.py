from tkinter import *
from tkinter import StringVar, messagebox

# Colors
color1 = "#FFFFFF"
color2 = "#000000"
color3 = "#383C41"
color4 = "#2E3339"
color5 = "#4CC2FF"
color6 = "#1C2127"

# Main window
window = Tk()
window.title("Calculator")
window.geometry("400x600")
window.configure(bg=color6)

# Allow resizing
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

# Variables
all_values = ""
text_value = StringVar()

# Functions
def enter_values(event):
    global all_values
    all_values += str(event)
    text_value.set(all_values)

def calculate():
    global all_values
    try:
        result = eval(all_values)
        text_value.set(str(result))
        all_values = str(result)
    except ZeroDivisionError:
        text_value.set("Erro")
        all_values = ""
    except Exception as e:
        messagebox.showerror("Erro", f"Expressão inválida: {e}")
        text_value.set("Erro")
        all_values = ""

def clear():
    global all_values
    all_values = ""
    text_value.set("")

# Frames
frame_head = Frame(window, bg=color6)
frame_head.grid(row=0, column=0, sticky="nsew")
frame_body = Frame(window, bg=color3)
frame_body.grid(row=1, column=0, sticky="nsew")

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=4)
window.columnconfigure(0, weight=1)

# Label
label = Label(frame_head, textvariable=text_value, anchor="e", font=("Poppins", 32), bg=color6, fg=color1, padx=10)
label.pack(expand=True, fill="both")

# Grid layout for buttons
buttons = [
    ["C", "%", "/",],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "-"],
    ["0", ".", "="]
]

# Expand frame body rows/columns
for i in range(len(buttons)):
    frame_body.rowconfigure(i, weight=1)
for j in range(4):
    frame_body.columnconfigure(j, weight=1)

# Button creation
for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == "":
            continue
        if char == "=":
            btn = Button(frame_body, text=char, bg=color5, fg=color1, font=("Poppins", 20), command=calculate)
        elif char == "C":
            btn = Button(frame_body, text=char, bg=color4, fg=color1, font=("Poppins", 20), command=clear)
        else:
            btn = Button(frame_body, text=char, bg=color3, fg=color1, font=("Poppins", 20),
                         command=lambda ch=char: enter_values(ch if ch != "x" else "*"))
        btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

# Add extra button for "=" if needed in column 3 of last row
if len(buttons[-1]) < 4:
    Button(frame_body, text="=", bg=color5, fg=color1, font=("Poppins", 20), command=calculate)\
        .grid(row=len(buttons)-1, column=3, sticky="nsew", padx=2, pady=2)

# Start
window.mainloop()
