import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("Red")
#create the turtle brad- draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(8)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #create turtle angie draws a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.right(90)
    #angie.forward(200)
    window.exitonclick()

draw_art()
