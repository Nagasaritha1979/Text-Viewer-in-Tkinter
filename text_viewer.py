from tkinter import *

root = Tk()
root.geometry("400x240")
i=0

def setTextInput(text):
    global i
    textExample.delete(1.0,"end")
    
    textExample.insert(1.0, text)
    i=i+1
    if (i==len(list1)-1):
        btnSet.config(state=DISABLED)
    else:
        btnSet2.config(state=NORMAL)
    
    
    
def set2TextInput(text2):
    global i
    
    textExample.delete(1.0,"end")
    
    textExample.insert(1.0, text2)
    i=i-1
    if i==0:
       btnSet2.config(state=DISABLED)
    else:
        btnSet.config(state=NORMAL)
    

list1=["An apple a day keeps the doctor away",
       "A stich in time saves nine.",
       "Failure is the stepping stone for success.",
       "Make hay while the sun shines."]

textExample = Text(root, height=10)
textExample.pack()
textExample.insert(1.0,list1[0])

btnSet = Button(root, 
                   height=1, 
                   width=10, 
                   text=">>", 
                   command=lambda:setTextInput(list1[i+1]))

btnSet2 = Button(root, 
                   height=1, 
                   width=10, 
                   text="<<", 
                   command=lambda:set2TextInput(list1[i-1]),state=DISABLED)

btnSet.pack()
btnSet2.pack()

root.mainloop()
