import tkinter as tk
import sys
import subprocess
from tkinter import Label, Button


root = tk.Tk()
root.title("Menu")
root.geometry("800x600+520+200")
root.resizable(False,False)


phrase = 0
dialogue : list = []
def run_dialogue():
    global phrase

    phrase += 1
    change_buttons()


def get_dialogue(index:int, dialogue:bool):

    text = None

    with open("dialogues.txt", "r", encoding="utf-8") as text:
        text = text.read().split('\n')
        text = text[index]
        text = text.split(":")

    if dialogue:
        return text[1]
    else:
        return text[0]


def choosing(index:int):

    match index:

        case 1:

            clear()
            button_1.place(x=120, y= 220)
            button_1.config(text="На ліву лінію")
            button_2.place(x=420, y=220)
            button_2.config(text="На праву лінію")

        case 2:

            clear()
            button_3.place(x=120, y=220)
            button_3.config(text="Не давати")
            button_4.place(x=420, y=220)
            button_4.config(text="Дати йому")



def clear():
    name.config(text="")
    dialogue_text.config(text="")
    run_button.place(x=-500,y=0)


def change_buttons():

    if get_dialogue(phrase, False) != "Вибір" and get_dialogue(phrase, False) != "Кінець":
        run_button.place(x=0,
                         y=500)
        button_1.place(x=-500, y= 0)
        button_2.place(x=-500, y=0)
        button_3.place(x=-500, y=0)
        button_4.place(x=-500, y=0)
        name.config(text=get_dialogue(phrase, False))
        dialogue_text.config(text=get_dialogue(phrase, True))

    elif get_dialogue(phrase, False) == "Вибір":
        choosing(int(get_dialogue(phrase, True)))

    elif get_dialogue(phrase, False) == "Кінець":
        sys.exit()


def choose_button(phrase_pos):
    global phrase

    phrase = phrase_pos
    run_dialogue()


name : Label = Label(root,text="ім'я",
                    font=("Comic Sans MS",26))


dialogue_text : Label = Label(root,text="діалог",
                    font=("Comic Sans MS",26))


run_button : Button = Button(root,text = "Продовжити...",
                         bg="black",
                         fg="white",
                         width=10,
                         font=("Comic Sans MS",24),
                         command=run_dialogue)


button_1 : Button = Button(root,text = "Вибір 1",
                         bg="black",
                         fg="white",
                         width=10,
                         font=("Comic Sans MS",24),
                         command=lambda:choose_button(20))
button_2 : Button = Button(root,text = "Вибір 2",
                         bg="black",
                         fg="white",
                         width=12,
                         font=("Comic Sans MS",24),
                         command=lambda:choose_button(32))
button_3 : Button = Button(root,text = "Вибір 3",
                         bg="black",
                         fg="white",
                         width=10,
                         font=("Comic Sans MS",24),
                         command=lambda:choose_button(51))
button_4 : Button = Button(root,text = "Вибір 4",
                         bg="black",
                         fg="white",
                         width=10,
                         font=("Comic Sans MS",24),
                         command=lambda:choose_button(61))


name.place(x=0,
           y=400)
dialogue_text.place(x=0,
           y=450)
run_button.place(x=0,
           y=500)


change_buttons()
root.mainloop()