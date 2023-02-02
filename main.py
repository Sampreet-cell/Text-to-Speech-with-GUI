import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text --> Speech")
root.geometry("900x450+100+100")
root.resizable(False,False)
root.configure(bg="lime green")

engine=pyttsx3.init()

def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
        
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def download():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
       
image_icon=PhotoImage(file="speaker.png")
root.iconphoto(False,image_icon) 

Top_frame=Frame(root,bg="mint cream",width=450,height=450)
Top_frame.place(x=0,y=0)

Label(Top_frame,text='TEXT to SPEECH',font='Dotum 20 bold',bg='mint cream',fg='lime green').place(x=115,y=30)

text_area=Text(root,font="robote 20 ",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=90,width=430,height=350)

Label(root,text='VOICE',font='arial 15 bold',bg='lime green',fg='mint cream').place(x=580,y=160)
Label(root,text='SPEED',font='arial 15 bold',bg='lime green',fg='mint cream').place(x=760,y=160)

gender_combobox=Combobox(root,values=['Male','Female'],font='arial 14',state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

btn=Button(root,text='SPEAK',width=10,bg='lime green',font='arial 14 bold',command=speaknow)
btn.place(x=645,y=250)

btn2=Button(root,text='SAVE',width=10,bg='lime green',font='arial 14 bold',command=download)
btn2.place(x=645,y=310)


root.mainloop()
