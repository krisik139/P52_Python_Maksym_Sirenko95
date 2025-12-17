import tkinter as tk
import sys
import subprocess
from tkinter import Label, Button

root = tk.Tk()
root.title("Menu")
root.geometry("800x600+520+200")
root.resizable(False,False)


def play():

    subprocess.run(['python', "main.py"])


def go_out():

    sys.exit()


main_label : Label = Label(root,text="\nІмбова гра",
                           font=("Comic Sans MS",36))

button_play : Button = Button(root,text = "Грати",
                         bg="black",
                         fg="white",
                         width=10,
                         font=("Comic Sans MS",24),
                         command=play)

button_exit : Button = Button(root,text = "Вийти",
                         bg="black",
                         fg="white",
                         width=10,
                         font=("Comic Sans MS",24),
                         command=exit)

main_label.pack()

button_play.place(x=45,
             y=450)
button_exit.place(x=535,
             y=450)


root.mainloop()