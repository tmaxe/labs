import turtle
turtle.shape('turtle')

a=6
c=36
turtle.left(90)

def semicircle_big():
    x=0
    while x < c/2:
        turtle.forward(a)
        turtle.left(362/c)
        x = x+1

def semicircle_small():
    x=0
    while x < c/2:
        turtle.forward(a/4)
        turtle.left(362/c)
        x=x+1

def pruxhinka():
    semicircle_big()
    semicircle_small()

for y in range (1,6,1):
    pruxhinka()

    
   
    
 


    

