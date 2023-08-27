from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters_and_symbols= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
          'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
          'y', 'z',"@", "#", "$", "%","!","*"]

new_password= []
random_num = random.randint(8,16)

def password_generator():
    for i in range (random_num):
        new_password.append(random.choice(letters_and_symbols))
    pass_word=(''.join(new_password))
    password_entry.insert(0,pass_word)
    pyperclip.copy(pass_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website= website_entry.get()
    email=email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
            "email": email,
            "password": password,
        }
    }
    if (len(website)==0 or len(password)==0):
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
                website_entry.delete(0, "end")
                password_entry.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20, bg="white")

canvas= Canvas(width=200,height=200, bg="white")
photo_img =PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo_img)
canvas.grid(column=1,row=0)

#labels
website_label = Label(text= "Website")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text= "Password:")
password_label.grid(column=0,row=3)

#entries
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"harinidonthula@gamil.com")
password_entry =Entry(width=21)
password_entry.grid(column=1,row=3)

#buttons
generate_pass_button= Button(text="Generate Password", command=password_generator)
generate_pass_button.grid(column=2,row=3)
add_button= Button(text="Add",width=36, command=save_password)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()
