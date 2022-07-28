
#tk import
import tkinter as tk
from tkinter import messagebox as mb
#GUI
snt = tk.Tk()

##program
def check ():
    sccheck = e1.get()
    so=int(sccheck)
    ##checking prime numbers
    isPrime = True
    if (so < 2):
        isPrime = False
    for p in range(2, so):
        if so % p == 0:
            isPrime = False
    ###result

    if isPrime==False:
        hl = tk.Label(snt, text='This is not a prime number')
        main.create_window(175, 75, window=hl)
    else:
        hl = tk.Label(snt, text='This is a prime number')
        main.create_window(175, 75, window=hl)

##creating canvas
main = tk.Canvas (snt, width=350, height=120)
main.pack()

##labeling
l1= tk.Label(snt, text='A simple GUI to check if a number is a prime number')
cal = tk.Button (snt, text = 'CHECK', command=check)

#Entry input
e1=tk.Entry(snt,bd=5, width=57)
e1.pack()
e1.place(x=0,y=25, bordermode='inside')
##insert label into canvas
main.create_window(175, 15, window=l1)
main.create_window(175, 110, window=cal)

snt.mainloop()