



import tkinter as tk
from tkinter import (Tk,StringVar,LabelFrame,Entry,Button,Text)
from tkinter import ttk 
from tkinter import filedialog
import tkinter.messagebox


# In[9]:


import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r'Here write down path where you install Tesseract'
import os

root =Tk()
root.configure(background='Powder Blue') 
root.title("Image Document Reader")
root.resizable(False,False)
root.geometry("1300x600")

# In[10]:


def readTxt1():
    fln =filedialog.askopenfilename(initialdir=os.getcwd(),title="select Image File ",filetypes=(("PNG File","*.png"),("JPEG File","*.jpg")))
    t1.set(fln)
    txt2.delete("1.0","end")
    txt2.insert("insert",pytesseract.image_to_string(Image.open(fln)))
def iExit():
        iExit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
        if iExit>0:
            root.destroy()
            return


# In[11]:



t1= StringVar()


# In[12]:


Title1 =LabelFrame(root, text='Choose  File',bg='Powder Blue')
Title1.pack(fill="both",expand="yes",padx=10,pady=10)

Title2 =LabelFrame(root, text='Text In Image',bg='Powder Blue')
Title2.pack(fill="both",expand="yes",padx=10,pady=10)

txt= Entry(Title1,textvariable=t1,width=20)
txt.pack(side=tk.LEFT,padx=5)

# In[13]:


btnabrows=Button(Title1, bd=7, fg='black',width=8, text="Browse", command=readTxt1,bg="Powder Blue")
btnabrows.pack(side=tk.LEFT,padx=10)
Button(Title2,text="Exit",bd=7, fg='black',width=9,command=iExit ).pack(side=tk.BOTTOM,padx=10,pady=10)


# In[14]:


txt2= Text(Title2)
txt2.pack(padx=20,pady=0)

root.configure(background='Powder Blue') 
root.title("Image Document Reader")
root.resizable(False,False)
root.geometry("1300x600")

root.mainloop()





