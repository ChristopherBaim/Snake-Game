from tkinter import *

master = Tk()
canvas = Canvas(master, width=100, height=100)
rect = canvas.create_rectangle(  50, 50 , 60, 60, fill='black')
canvas.create_rectangle(  20, 20 , 30, 30, fill='black')
test = canvas.find_closest(20,20)
class App(object):
    def __init__(self, master1, **kwargs):
        self.master1=master
        #master1.bind('<KeyRelease>',self.release)
        master1.bind('<KeyPress>',self.press)
        
    def press(self,event):
        if event.keysym=='a':
            canvas.move(rect,-10,0)
        if event.keysym=='w':
            canvas.move(rect,0,-10)
        if event.keysym=='d':
            canvas.move(rect,10,0)
        if event.keysym=='s':
            canvas.move(rect,0,10)

        if event.keysym=='z':
            test = canvas.find_closest(20,20)
            canvas.delete(test)
            
canvas.pack()
app=App(master)
mainloop()
