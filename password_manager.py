from random import choice, randint, shuffle
from tkinter import messagebox
import tkinter


def save_data():
    data_website = website_entry.get()
    data_email = entry_email.get()
    data_password = entry_password.get()
    if len(data_email) == 0 or len(data_password) == 0:
        messagebox.showinfo(title='Ooops', message="Please, don't leave any fields empty!")
        website_entry.focus()
    else:
        is_ok = messagebox.askokcancel(title=data_website, message=f'Details entered:\n'
                                                                   f'\tE-mail: {data_email}\n'
                                                                   f'\tPassword: {data_password}\n'
                                                                   f'OK?')
        if is_ok:
            with open('pass_data.txt', 'a') as data:
                data.write(f'{data_website} | {data_email}| {data_password}\n')
                website_entry.delete(0, len(data_website))
                entry_email.delete(0, len(data_email))
                entry_password.delete(0, len(data_password))
                website_entry.focus()


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(numbers) for _ in range(randint(2, 4))]
    numbers_list = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)
    password = ''.join(password_list)
    entry_password.insert(0, password)


window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file='/Users/edi/PycharmProjects/password_manager/logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

title_label = tkinter.Label(text='PASWORD MANAGER')
title_label.grid(row=1, column=1, columnspan=2)
website_label = tkinter.Label(text='Website: ')
website_label.grid(row=2, column=0)
email_label = tkinter.Label(text='Input your e-mail: ')
email_label.grid(row=3, column=0)
password_label = tkinter.Label(text='Input your password: ')
password_label.grid(row=4, column=0)

website_entry = tkinter.Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()
entry_email = tkinter.Entry(width=35)
entry_email.grid(row=3, column=1, columnspan=2)
entry_password = tkinter.Entry(width=20)
entry_password.grid(row=4, column=1)
password = entry_password.get()

add_button = tkinter.Button(text='Add', width=36, command=save_data)
add_button.grid(row=5, column=1, columnspan=2)
generate_password = tkinter.Button(text='Generate Password', command=generate)
generate_password.grid(row=4, column=2)

window.mainloop()
