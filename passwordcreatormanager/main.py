from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    pass_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if len(web_entry.get()==0) or len(pass_entry.get()==0):
        messagebox.showinfo(title="oops",message="please amke sure the fields are not empty ")
    is_ok=messagebox.askokcancel(title=web_entry.get(),message=f"detial are: \nEmail: {email_entry.get()}"
                                                         f"\n password:{pass_entry.get()}\n is it ok to be save?")
    if is_ok:
        file = open("data.txt", "a")
        file.write(f"{web_entry.get()} || {email_entry.get()} || {pass_entry.get()}")
        web_entry.delete(0, END)
        pass_entry.delete(0, END)
        file.close()


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("password manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="C:/Users/Asus/OneDrive/Desktop/PYTHONNOTES/passwordcreatormanager/logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

web_label=Label(text="Website")
web_label.grid(row=1,column=0)
web_entry=Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()

email_label=Label(text="email")
email_label.grid(row=2,column=0)
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"adi@123gmail.com")

pass_label=Label(text="password")
pass_label.grid(row=3,column=0)
pass_entry=Entry(width=21)
pass_entry.grid(row=3,column=1)


gene_button=Button(text="Generate pass",command=password_generator )
gene_button.grid(row=3,column=2)


add_button=Button(text="add",width=30,command=save)
add_button.grid(row=4,column=1,columnspan=2)









window.mainloop()