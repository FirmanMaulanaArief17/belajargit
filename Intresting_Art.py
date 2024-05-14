import turtle as ART
import random

ART.bgcolor("black")
ART.speed(99999999)
ART.penup()
ART.goto(0, 0)
ART.pendown()

colors = ["#FF7F50", "#DC143C", "#FFD700",
          "#00FF7F", "#8B008B", "#1E90FF"]
          
for i in range(60):
    color = random.choice(colors)
    ART.pencolor(color)
    ART.fillcolor(color)
    ART.begin_fill()
    for j in range(6):
        ART.forward(100)
        ART.right(60)
    ART.end_fill()
    ART.right(6)
    
ART.penup()
ART.goto(0, 0)
ART.pendown()

for i in range(60):
    color = random.choice(colors)
    ART.pencolor(color)
    ART.fillcolor(color)
    ART.begin_fill()
    for j in range(4):
        ART.forward(80)
        ART.right(90)
    ART.end_fill()
    ART.right(6)
    
ART.penup()
ART.goto(0, 0)
ART.pendown()

for i in range(60):
    color = random.choice(colors)
    ART.pencolor(color)
    ART.fillcolor(color)
    ART.begin_fill()
    for j in range(3):
        ART.forward(60)
        ART.right(120)
    ART.end_fill()
    ART.right(6)
    
ART.penup()
ART.goto(0, 0)
ART.pendown()
    
for i in range(60):
    color = random.choice(colors)
    ART.pencolor(color)
    ART.fillcolor(color)
    ART.begin_fill()
    ART.circle(50)
    ART.end_fill()
    ART.right(6)

ART.done()