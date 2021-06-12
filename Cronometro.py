# -*- coding: utf-8 -*-
"""
Created : on Wed May  6 14:16:44 2020
Updated and improved : 28/01/2020

@author: jdros
Updated and improved by: Woomker
"""

from tkinter import *
from tkinter.font import Font

run = False 
initialized = True

class interface:
    def startstopwatch(self):
        global run
        global initialized
        if run == False:
            run = True
            initialized = False
            self.tick()
    def stopstopwatch(self):
        global run
        global initialized
        run = False
        initialized = False
    def resetstopwatch(self):
        global run
        global initialized
        run= False
        initialized = True
        self.hour=0
        self.minute=0
        self.second=0
        self.millisecond=0
        self.text.set("00:00:00:000")

    def tick(self):
        self.millisecond=self.passofthetime(self.millisecond)
        if(self.millisecond == 1000):
            self.millisecond = 0
            self.second=self.passofthetime(self.second)
        if(self.second == 60):
            self.second = 0
            self.minute=self.passofthetime(self.minute)
        if(self.minute == 60):
            self.minute = 0
            self.hour=self.passofthetime(self.hour)
        result=self.getvalue(self.hour,False)+":"+self.getvalue(self.minute,False)+":"+self.getvalue(self.second,False)+":"+self.getvalue(self.millisecond,True)
        self.text.set(result)
        if run:
            self.root.after(1,self.tick)
        elif initialized:
            self.text.set("00:00:00:000")

                    
    def  __init__(self):
        self.hour=0
        self.minute=0
        self.second=0
        self.millisecond=0
        self.root=Tk()
        self.root.title("stopwatch")    
        self.root.geometry("350x100")
        self.root.resizable(False,False)
        self.text = StringVar()
        self.text.set("00:00:00:000")
        self.myFont =Font(family="Times New Roman", size=18)
        self.label = Label(self.root,textvariable=self.text)
        self.label.pack()
        self.label.configure(font=self.myFont)
        self.btnreset = Button(self.root,text="Reset",fg="Blue",command= self.resetstopwatch).place(x=10,y=70,height=20,width=80) 
        self.btnstart = Button(self.root,text="Start",fg="Green",command= self.startstopwatch).place(x=130,y=70,height=20,width=80) 
        self.btnstop = Button(self.root,text="Stop",fg="red",command= self.stopstopwatch).place(x=250,y=70,height=20,width=80)  

    def passofthetime(self,value):
        value +=1
        return value
        

    def getvalue(self,value,zeros):
        if zeros:
            if value < 10:
                return ("00" + str(value))
            elif value < 100 and value >= 10:
                return ("0" + str(value))
            else:
                return str(value)
        if zeros == False:
            if value <10:
                return ("0" + str(value))
            else:
                return str(value)

App=interface()
App.root.mainloop()
