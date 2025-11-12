from tkinter import * #importa o modulo todo
from tkinter import ttk #importa widgets stylized
from tkinter import StringVar, messagebox #1 atribui uma variavel ao widget

#colores
color1 = "#FFFFFF" #white
color2 = "#000000" #black
color3 = "#383C41" #bluegray
color4 = "#2E3339" #darkbluegray
color5 = "#4CC2FF" #blue
color6 = "#1C2127" #almostblack

#Window settings
window = Tk()
window.title("Calculator")
window.geometry("345x533")


#Frames settings
frame_head = Frame(window, width=345, height=110, bg=color6)
frame_head.grid(row=0, column=0)

frame_body = Frame(window, width=345, height=500, bg=color3)
frame_body.grid(row=1, column=0)

#all values variable
all_values = ""

#Function label
text_value = StringVar()

#Function that shows the text on the screen
def enter_values(event):
    global all_values
    all_values += str(event)
    text_value.set(all_values)

#Calculate
def calculate():
    global all_values
    try:
        result = eval(all_values)
        text_value.set(str(result))
    except ZeroDivisionError:
        text_value.set("Error")
    except Exception as e:
        messagebox.showerror("Error", f"Error in the expression: {e}")
        text_value.set("Error")
    


#Clear function
def clear():
    global all_values
    all_values = ""
    text_value.set("")

#Label settings
app_label = Label(frame_head, textvariable=text_value, width=19, height=2, padx=14, relief=FLAT, anchor="e", justify=RIGHT, font=("Poppins 20 bold"), bg=color6, fg=color1)
app_label.place(x=0, y=0)

#Button settings
#First line
button1 = Button(frame_body, command= clear, text="C", width=9, height=1, bg=color4, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button1.place(x=0, y=0)

button2 = Button(frame_body, command= lambda: enter_values("%"), text="%", width=5, height=1, bg=color4, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button2.place(x=160, y=0)

button3 = Button(frame_body, command= lambda: enter_values("/"), text="/", width=5, height=1, bg=color4, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button3.place(x=250, y=0)

#Second line
button4 = Button(frame_body, command= lambda: enter_values("7"), text="7", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button4.place(x=0, y=84)

button5 = Button(frame_body, command= lambda: enter_values("8"), text="8", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button5.place(x=79, y=84)

button6 = Button(frame_body, command= lambda: enter_values("9"), text="9", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button6.place(x=158, y=84)

button7 = Button(frame_body, command= lambda: enter_values("*"), text="x", width=6, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button7.place(x=237, y=84)

#Third line
button8 = Button(frame_body, command= lambda: enter_values("4"), text="4", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button8.place(x=0, y=169)

button9 = Button(frame_body, command= lambda: enter_values("5"), text="5", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button9.place(x=79, y=169)

button10 = Button(frame_body, command= lambda: enter_values("6"), text="6", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button10.place(x=158, y=169)

button11 = Button(frame_body, command= lambda: enter_values("+"), text="+", width=6, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button11.place(x=237, y=169)

#Third line
button12 = Button(frame_body, command= lambda: enter_values("1"), text="1", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button12.place(x=0, y=254)

button13 = Button(frame_body, command= lambda: enter_values("2"), text="2", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button13.place(x=79, y=254)

button14 = Button(frame_body, command= lambda: enter_values("3"), text="3", width=4, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button14.place(x=158, y=254)

button15 = Button(frame_body, command= lambda: enter_values("-"), text="-", width=6, height=1, bg=color3, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button15.place(x=237, y=254)

#Forth line
button16 = Button(frame_body, command= lambda: enter_values("0"), text="0", width=9, height=1, bg=color4, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button16.place(x=0, y=339)

button17 = Button(frame_body, command= lambda: enter_values("."), text=".", width=5, height=1, bg=color4, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button17.place(x=160, y=339)

button18 = Button(frame_body, command= calculate, text="=", width=5, height=1, bg=color5, fg=color1, font=("Poppins 20 bold"), relief=RAISED, overrelief=RIDGE)
button18.place(x=250, y=339)


window.mainloop()