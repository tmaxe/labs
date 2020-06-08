import turtle
import math
turtle.shape('turtle')

a=75
x=0
n=3
f=(180-((180*(n-2))/n)/2)
r=180-(((180*((n+1)-2))/(n+1))/2)
while x < n:
    turtle.forward(a)
    turtle.left(360/n)
    x = x+1
else:
    d= 2*(a/(2*(math.sin(((360/(2*n))*math.pi/180)))))
    c=d-a
    turtle.right(f)
    turtle.penup()
    turtle.forward(c)
    turtle.pendown()
    turtle.left(r)
   
def poligon(n):
    x=0
    a=d
    f=(180-((180*(n-2))/n)/2)
    r=180-(((180*((n+1)-2))/(n+1))/2)
    while x < n:
        turtle.forward(a)
        turtle.left(360/n)
        x = x+1
    else:
        a= 2*(a/(2*(math.sin(((360/(2*n))*math.pi/180)))))
        turtle.right(f)
        turtle.penup()
        turtle.forward(c)
        turtle.pendown()
        turtle.left(r)
for n in range(4,17,1):
    poligon(n)





    
   
    
 


    

