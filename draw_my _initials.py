import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("Red")
#create the turtle brad- draws a s
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    brad.left(180)
    brad.forward(100)
    for i in range(1,3):
        brad.left(90)
        brad.forward(100)
    
    for i in range(1,3):
        brad.right(90)
        brad.forward(100)

    #create turtle angie draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.penup()
    angie.forward(100)
    angie.pendown()
    angie.forward(100)
    angie.left(180)
    angie.forward(50)
    angie.left(90)
    angie.forward(200)
    
    window.exitonclick()

draw_art()
