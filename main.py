from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_manager():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letter = [random.choice(letters) for i in range(nr_letters)]
    password_symbol = [random.choice(symbols) for i in range(nr_symbols)]
    password_number = [random.choice(numbers) for i in range(nr_numbers)]
    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = email_entry.get()
    passw = password_entry.get()
    file = website_entry.get() + " |" + email_entry.get() + " |" + password_entry.get() + "\n"

    if len(web) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showinfo(title="oops", message="hey dont let the password empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"these are the details entered: \nEmail: {email}\nPassword:"
                                                          f"{password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(file)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website")
website.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()
email = Label(text="Email/Username")
email.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "username@gmail.com")
password = Label(text="Password")
password.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_manager)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
