from tkinter import *

root=Tk()
root.title("Dictionary")
root.geometry("600x400")

label_of_mutable = Label(root)
label_of_immutable = Label(root)
label_of_tkinter = Label(root)


dictonary = {'Mutable':'Values can be changed just like a List',
             'Immutable':'Values cannot be changed just like a touple',
             'Tkinter':'It is the GUI lbrary for python'
             }

def mutable():
    label_of_mutable["text"] = dictonary['Mutable']
    
def immutable():
    label_of_mutable["text"] = dictonary['Immutable']

def tkinter():
    label_of_mutable["text"] = dictonary['Tkinter']

    

root.mainloop()
 
