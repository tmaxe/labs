import turtle
turtle.shape('turtle')
    
a = 50
b = 90
c = 10

while a <=230:  
    turtle.pendown()
    turtle.forward(a),turtle.left(b) 
    turtle.forward(a),turtle.left(b)
    turtle.forward(a),turtle.left(b)
    turtle.forward(a),turtle.left(b)
    turtle.penup()
    turtle.goto(-c, -c)
    a = a+20
    c = c+10



    

