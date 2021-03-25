import turtle as t
import random as r
s=t.Screen()
c=t.clone()

c.shape("circle")
c.shapesize(0.5,0.5)
c.speed(0)
c.penup()
c.goto(r.randint(-300,300),r.randint(-250,250))

s.title("Movement")
s.bgcolor("Lightgreen")
t.penup()
t.shape("turtle")
t.speed(1)


def up():
    t.fd(50)
def lt():
    t.lt(90)
def rt():
    t.rt(90)
def bk():
    t.right(180)
    t.fd(50)
def q():
    t.bye()
s.onkey(up," Up")
s.onkey(lt," Left")
s.onkey(rt," Right")
s.onkey(bk," Down")
s.onkey(q,"q")
s.listen()
a=1

while True:
    if (c.pos()-t.pos())>=(0,0):
        if (c.pos()-t.pos())<=(5,5):
            c.goto(r.randint(-300,300),r.randint(-250,250))
            print("f")
            
            a=a+1
            t.shapesize(1,a,1)
    if (t.pos()-c.pos())>=(0,0):
        if (t.pos()-c.pos())<=(10,10):
            c.goto(r.randint(-300,300),r.randint(-250,250))
            print("m")
            a=a+1
            t.shapesize(1,a,1)
    
    
    t.fd(10)
 
    

s.mainloop()

