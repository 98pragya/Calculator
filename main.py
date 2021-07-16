from tkinter import *
root = Tk()

root.title('simple Calculator')


root.iconbitmap('C:/Users/Hp/Desktop/calculator.ico')
e = Entry(root, width=20, borderwidth=10, font=('Gungsuh', 30))
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15, ipadx=5, ipady=5, )

# function to display values that have been clicked
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Function for equals to
def button_eq():
    try:
        val = str(e.get())  # converts the value of entry to string and stores it
        ans = eval(val)  # evaluates the answer of value stored in val
    except:
        ans = "Error"
    finally:
        e.delete(0, END)  # deletes the value in entry
        e.insert(0, ans)  # inserts the value of ans in entry


# function to clear the screen
def button_clear():
    e.delete(0, END)  # clears the entry in the screen


# Defining the buttons
button_0 = Button(root, text='0', command=lambda: button_click(0), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_1 = Button(root, text='1', command=lambda: button_click(1), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_2 = Button(root, text='2', command=lambda: button_click(2), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_3 = Button(root, text='3', command=lambda: button_click(3), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_4 = Button(root, text='4', command=lambda: button_click(4), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_5 = Button(root, text='5', command=lambda: button_click(5), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_6 = Button(root, text='6', command=lambda: button_click(6), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_7 = Button(root, text='7', command=lambda: button_click(7), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_8 = Button(root, text='8', command=lambda: button_click(8), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_9 = Button(root, text='9', command=lambda: button_click(9), font=('Gungsuh', 20), fg='black', bg='white',
                  activeforeground='white', activebackground='black')
button_dec = Button(root, text='.', command=lambda: button_click('.'), font=('Gungsuh', 20), fg='black', bg= 'white',)
button_add = Button(root, text='+', command=lambda: button_click('+'), font=('Gungsuh', 20), fg='black', bg='white', )
button_sub = Button(root, text='-', command=lambda: button_click('-'), font=('Gungsuh', 20), fg='black', bg= 'white',)
button_mul = Button(root, text='x', command=lambda: button_click('*'), font=('Gungsuh', 20), fg='black', bg= 'white',)
button_div = Button(root, text='/', command=lambda: button_click('/'), font=('Gungsuh', 20), fg='black', bg='white', )
button_exp = Button(root, text='^', command=lambda: button_click('**'), font=('Gungsuh', 20), fg='black', bg='white', )
button_mod = Button(root, text='mod', command=lambda: button_click('%'), font=('Gungsuh', 20), fg='black', bg= 'white',)
button_equ = Button(root, text='=', command=button_eq, font=('Gungsuh', 20), fg='black', bg='white', )
button_clear = Button(root, text='Clear', command=button_clear, font=('Gungsuh', 20), fg='black', bg='white', )

# Arranging the buttons on the screen
button_9.grid(row=1, column=2, ipadx=40, ipady=20)
button_8.grid(row=1, column=1, ipadx=40, ipady=20)
button_7.grid(row=1, column=0, ipadx=40, ipady=20)
button_clear.grid(row=5, column=1, ipadx=19, ipady=31)
button_6.grid(row=2, column=2, ipadx=40, ipady=20)
button_5.grid(row=2, column=1, ipadx=40, ipady=20)
button_4.grid(row=2, column=0, ipadx=40, ipady=20)
button_mul.grid(row=2, column=3, ipadx=40, ipady=20)
button_3.grid(row=3, column=2, ipadx=40, ipady=20)
button_2.grid(row=3, column=1, ipadx=40, ipady=20)
button_1.grid(row=3, column=0, ipadx=40, ipady=20)
button_div.grid(row=3, column=3, ipadx=40, ipady=20)
button_0.grid(row=4, column=0, ipadx=40, ipady=20)
button_dec.grid(row=4, column=1, ipadx=46, ipady=20)
button_add.grid(row=4, column=2, ipadx=40, ipady=20)
button_sub.grid(row=4, column=3, ipadx=37, ipady=20)
button_mod.grid(row=5, column=0, ipadx=29, ipady=30)
button_exp.grid(row=1, column=3, ipadx=41, ipady=20)
button_equ.grid(row=5, column=2, columnspan=2, ipadx=112, ipady=20)

root.mainloop()