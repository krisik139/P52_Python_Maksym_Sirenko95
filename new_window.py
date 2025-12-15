import re
import tkinter as tk


login_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2.}$")
password_pattern = re.compile(r"^(?=.*\d)(?=.*[A-Z])(&=.*[!@#%^&*?]).{6,20}$")

root = tk.Tk()
root.geometry("400x250+700+350")
root.resizable(False,False)


def login():
    login = login_entry.get()
    password = password_entry.get()

    if login_pattern.search(login):
        if password_pattern.search(password):
            login_entry.config(bg="green")
            password_entry.config(bg="green")
        else:
            login_entry.config(bg="red")
            password_entry.config(bg="red")
    else:
        login_entry.config(bg="red")
        password_entry.config(bg="red")


login_label = tk.Label(root,text="Login:",
                       font=("Arial",14), padx=50)

password_label = tk.Label(root,text="Password:",
                       font=("Arial",14), padx=50)

login_entry = tk.Entry(root, font=("Arial",12),
                       width=20)

password_entry = tk.Entry(root, font=("Arial",12),
                       width=20, show="*")

login_button = tk.Button(root,text="Log-in",
                         font=("Arial",16), width=12,
                         command=login)

root.grid_columnconfigure(0,minsize=150)
root.grid_columnconfigure(1,minsize=250)

root.grid_rowconfigure(0,minsize=90)
root.grid_rowconfigure(1,minsize=90)

login_label.grid(column=0,row=0)
password_label.grid(column=0,row=1)

login_entry.grid(column=1,row=0)
password_entry.grid(column=1,row=1)

login_button.grid(columnspan=2, row=2)



root.mainloop()