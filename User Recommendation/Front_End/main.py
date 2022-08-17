from tkinter import *
from functools import partial
from tkinter import messagebox
import pandas as pd
import movieRec


#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - pythonexamples.org')
import pandas as pd

# Creating Empty DataFrame and Storing it in variable df
df = pd.DataFrame()
data = [1,2,3,4,5,6]
movies= ['Avengers','One Day','Apple','Iron Man','Love is One Day','Beast']
d = {'User ID':data,'Movies':movies}
f = pd.DataFrame(d)



def login():
    def recommand():
        print(input_movies.get())
        if input_movies.get() == "":
            info.config(text='No Movies Input')
        else:
            rec_movies_list=movieRec.main(str(input_movies.get()),int(user))
            output="\n".join(rec_movies_list)
            info.config(text=output)

    user=username.get()
    pasword=password.get()
    if pasword == '1212':
        global input_movies
        root=Toplevel(tkWindow)
        root.title('Recommendation')
        root.geometry('400x200')
        root.resizable(False,False)
        recommendationLabel = Label(root, text="Recommendation Base On").grid(row=0, column=0)
        input_movies = StringVar()
        inputEntry = Entry(root, textvariable=input_movies).grid(row=0, column=1)
        info = Label(root)
        info.grid(row=1, column=0)
        RecommandButton = Button(root, text="Recommand", command=recommand)
        RecommandButton.place(x=150, y=150)

    else:
        messagebox.showerror("Invalid","The User Not in Our Data Base")


def main_page():
    #username label and text entry box
    global username
    global password
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)


    #login button
    loginButton = Button(tkWindow, text="Login", command=login).grid(row=4, column=0)

def pre_processing():
    user_to_movies= pd.read_csv("rating_hat_svd.csv")

main_page()
tkWindow.mainloop()