import turtle

window = turtle.Screen()
window.setup(1350,750)
window.bgcolor("black")

#Title Screen
def title_screen():
    global title
    global initialize_1
    global initialize_2


    title = turtle.Turtle()
    title.pencolor("cyan")
    title.shape("square")
    title.shapesize(.1)
    title.speed(0)
    title.penup()
    title.write("TRON", font=("Germania One", 32), align=("center"))
    title.goto(-155,-15)
    title.pencolor("white")
    title.write("Player 1, Tron, is Cyan and will control with q:left and e:right", font=("Germania One", 9))
    title.goto(-207,-30)
    title.write("Player 2, Clu, is Orange and will control with left-arrow:left and right-arrow:right", font=("Germania One", 9))

    initialize_1 = turtle.Turtle()
    initialize_1.color("Cyan")
    initialize_1.shape("square")
    initialize_1.shapesize(.1)
    initialize_1.speed(0)
    initialize_1.penup()
    initialize_1.hideturtle()

    initialize_2 = turtle.Turtle()
    initialize_2.color("Cyan")
    initialize_2.shape("square")
    initialize_2.shapesize(.1)
    initialize_2.speed(0)
    initialize_2.penup()
    initialize_2.hideturtle()

    y=0
    initialize_1.forward(245)
    initialize_1.stamp()
    while (y <= 10):
            initialize_1.forward(10)
            initialize_1.stamp()
            y += 1

    x=0
    y=0
    while (x <= 90):
        initialize_1.goto(0,0)
        initialize_2.goto(0,0)
        initialize_1.right(2)
        initialize_2.left(2)
        initialize_1.forward(245)
        initialize_2.forward(245)
        initialize_1.stamp()
        initialize_2.stamp()
        while (y <= 10):
            initialize_1.forward(10)
            initialize_2.forward(10)
            initialize_1.stamp()
            initialize_2.stamp()
            y += 1
        y = 0
        x += 1
    
    title.goto(-57,-60)
    title.write("Press Enter to Begin", font=("Germania One", 9))
    window.onkey(title_cleanup, "Return")

def title_cleanup():
    title.hideturtle()
    initialize_1.hideturtle()
    initialize_2.hideturtle()
    title.clear()
    initialize_1.clear()
    initialize_2.clear()

title_screen()
window.mainloop()
