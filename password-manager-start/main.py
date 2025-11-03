from tkinter import *
from tkinter import messagebox
import pyperclip
FONT_NAME = "Courier"
entries={"website":"default", "email":"default", "password":"yesitsme"}
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list+=[random.choice(letters) for char in range(nr_letters)]

    password_list+=[random.choice(symbols) for char in range(nr_symbols)]

    password_list+=[random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password=''.join(password_list)
    password_entry.insert(0,password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def write(entries):
    website= website_entry.get()
    email= email_entry.get()
    password= password_entry.get()
    entries["website"]=website
    entries["email"]=email
    entries["password"]=password
    if (len(website)==0 or len(password)==0):
        messagebox.showinfo(title="oops",message="Please don't leave any fields empty!")
    else:
        is_ok= messagebox.askokcancel(title=website, message=f"These are the details you entered:\nemail: {email},\n password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as f:
                f.write(f'{entries["website"]} | {entries["email"]} | {entries["password"]}\n')
            print("added to file: ",entries)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
lock_img= PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

website_label= Label(text="Website:")
website_label.grid(row=1,column=0)

email_label= Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label= Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry= Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
website_entry.focus() #to put the cursor to this entry as soon as program is run
def clear_website_entry():
    website_entry.delete(0,END)

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"akshath55.t@gmail.com")

password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)
def clear_password_entry():
    password_entry.delete(0,END)

gen_password_button=Button(text="Generate Password",command=pass_gen)
gen_password_button.grid(row=3,column=3,padx=5)

def clear_entries(): 
    clear_website_entry()
    clear_password_entry()
    
add_button=Button(text="Add",width=36,command= lambda: (write(entries),clear_entries())) #experimenting with lambda
add_button.grid(row=4,column=1,columnspan=2,pady=3)

window.mainloop()


