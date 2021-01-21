from tkinter import *
import random

master = Tk()
xSize = 500
ySize = 500
canvas = Canvas(master, width=xSize, height=ySize)

canvas.create_rectangle(  10, 10 , 18, 18, fill='green')
test = canvas.find_closest(20,20)
direction = (10,0)
snake = [(10,10)]
foodTup = (100,100)
food = canvas.create_oval(100,100,108,108, fill='red')
moveMade = False
freeSpots = list()
for x in range(10,500,10):
    for y in range(10,500,10):
        freeSpots.append((x,y))

freeSpots.remove((10,10))
freeSpots.remove((100,100))

class App(object):
    def __init__(self, master1, **kwargs):
        self.master1=master
        #master1.bind('<KeyRelease>',self.release)
        master1.bind('<KeyPress>',self.press)
        
    def press(self,event):
        global direction
        global moveMade
        if event.keysym=='a' and direction !=(10,0) and not moveMade:
            direction = (-10,0)
            moveMade = True
            #canvas.move(rect,-10,0) #Left
        if event.keysym=='w' and direction != (0,10) and not moveMade:
            #canvas.move(rect,0,-10) #Up
            direction = (0,-10)
            moveMade = True
        if event.keysym=='d' and direction != (-10,0) and not moveMade:
            direction = (10,0)
            moveMade = True
            #canvas.move(rect,10,0) #Right
        if event.keysym=='s' and direction != (0,-10) and not moveMade:
            direction = (0,10)
            moveMade = True
            #canvas.move(rect,0,10) #Down

        if event.keysym=='z':
            test = canvas.find_closest(20,20)
            canvas.delete(test)
def clock():
    global moveMade
    global direction
    global food
    global foodTup
    dead = False
    moveMade = False
    
    length = len(snake)
    oldHead = snake[length-1]
    newHead = ((oldHead[0] + direction[0]),(oldHead[1] + direction[1]))



    if newHead in snake:
        dead = True
        
    elif newHead[0]>xSize or newHead[1]>ySize or newHead[0]<0 or newHead[1]<0:
        dead = True
        
    
    snake.append(newHead)
    xNew = newHead[0]
    yNew = newHead[1]
    canvas.create_rectangle(  xNew, yNew , xNew+8, yNew+8, fill='blue')
    
    if not dead:
        master.after(100, clock)
        if newHead != foodTup:
            Tail = snake.pop(0)
            xTail = Tail[0]
            yTail = Tail[1]
            toDelete = canvas.find_closest(xTail,yTail)
            canvas.delete(toDelete)
            freeSpots.append(Tail)
        if newHead == foodTup:
            canvas.delete(food)
            foodTup = random.choice(freeSpots)
            food = canvas.create_oval(foodTup[0],foodTup[1],foodTup[0]+9,foodTup[1]+8, fill='red')
        else:
            freeSpots.remove(newHead)
    else:
        print("Game Over")
        lose = Label(master, text="Game Over", font=("Courier", 44, "bold"))
        lose.place(x=100, y=10)

        
clock()

canvas.pack()
app=App(master)
mainloop()
