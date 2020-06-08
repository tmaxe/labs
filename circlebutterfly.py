import turtle
turtle.shape('turtle')

def figure_eight(c, a):
    turtle.right(90)
    x=0
    y=0
    while x < c:
        turtle.forward(a)
        turtle.left(360/c)
        x = x+1
    else:
        while y < c:
            turtle.forward(a)
            turtle.right(360/c)
            y = y+1
for a in range (6,12,1):           
    figure_eight(60, a)
    turtle.right(-90)

    
   
    
 


    

