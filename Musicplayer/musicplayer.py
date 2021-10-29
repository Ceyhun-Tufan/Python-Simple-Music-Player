
'''
Making games with python chapter 2 program 5
'''
import pygame, sys, time
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
import os
from tkinter.filedialog import askdirectory, askopenfilename

# INITIALISING 

pygame.init()

filename = ""
tk_list = []

# OPEN POP UP

def popup():
   top= Toplevel(ws)
   top.title("Error")
   Label(top, text= "You probably forgot to open file first!",
    font=('Mistral 13 bold')).pack()

# FUNCTIONS

def openfile():
    global filename,tk_list
    filename = askdirectory()
    tk_list = os.listdir(filename)
    lb.delete(0,END)
    task_list = []
    for i in tk_list:
        i = i.replace(".mp3","")
        task_list.append(i)
    for item in task_list:
        lb.insert(END, item)

def startMusic():
    global song
    try:
        song = lb.get(ACTIVE)
        song = f'{filename}/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=-1)
    except Exception:
        popup()

paused = False

def pauseMusic():
    global paused
    if paused == False:
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False


def stopMusic():
    pygame.mixer.music.stop()
    lb.selection_clear(ACTIVE)

def deleteTask():
    lb.delete(ANCHOR)

#TKINTER CONFIGURATION

ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)
lb.insert(ANCHOR,"You need to open a file")
lb.insert(ANCHOR,"from File button")


sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

button_frame = Frame(ws)
button_frame.pack(pady=20)

start = Button(
    button_frame,
    text='Start',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=startMusic
)
start.pack(fill=BOTH, expand=True, side=LEFT)

stop = Button(
    button_frame,
    text='Stop',
    font=('times 14'),
    bg='red',
    padx=20,
    pady=10,
    command=stopMusic
)
stop.pack(fill=BOTH, expand=True, side=LEFT)

pause = Button(
    button_frame,
    text='Pause',
    font=('times 14'),
    bg='yellow',
    padx=20,
    pady=10,
    command=pauseMusic
)
pause.pack(fill=BOTH, expand=True, side=LEFT)



askbtn = Button(
    button_frame,
    text='File',
    font=('times 14'),
    bg='green',
    padx=20,
    pady=10,
    command=openfile
)
askbtn.pack(fill=BOTH, expand=True, side=LEFT)









ws.mainloop()