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
    setup()

def tron_right():
    global tron

    tron.right(90)
    tron.speed(10)

def tron_left():
    global tron
    
    tron.left(90)
    tron.speed(10)

def clu_left():
    global clu
    
    clu.left(90)
    clu.forward(1)

def clu_right():
    global clu
    
    clu.right(90)
    clu.forward(1)

def setup():

    global clu
    global tron
    global tron_xList
    global tron_yList
    global clu_xList
    global clu_yList
    global window

    clu_xList = []
    clu_yList = []
    tron_xList = []
    tron_yList = []

    #Boundary
    bounds = turtle.Turtle()
    bounds.speed(0)
    bounds.hideturtle()
    bounds.penup()
    bounds.goto(650,350)
    bounds.pendown()
    bounds.left(180)
    bounds.forward(1300)
    bounds.left(90)
    bounds.forward(700)
    bounds.left(90)
    bounds.forward(1300)
    bounds.left(90)
    bounds.forward(700)
    bounds.left(90)

    #Bikes
    tron = turtle.Turtle()
    tron.color("cyan")
    tron.speed(5)
    clu = turtle.Turtle()
    clu.color("orange")
    clu.speed(5)

    #moving bikes to starting positions
    tron.penup()
    clu.penup()
    tron.goto(-450,200)
    clu.goto(450,-200)
    clu.left(180)
    tron.pendown()
    clu.pendown()

    movement()

def coordinates(bike):
    x = bike.xcor()
    y = bike.ycor()
    return x, y

def movement():
    global clu
    global tron
    global moving

    moving = True

    while moving != False:
        tron.forward(5)
        clu.forward(5)

        window.listen()

        window.onkey(tron_right, "Right")
        window.onkey(tron_left, "Left")

        window.onkey(clu_left, "q")
        window.onkey(clu_right, "e")

        x,y = coordinates(tron)
        bikecheck(x, y, tron)

        x,y = coordinates(clu)
        bikecheck(x, y, clu)      

def bikecheck(x,y,bike):
    global moving
    global tron_xList
    global tron_yList
    global clu_xList
    global clu_yList

    if abs(x)> 650 or abs(y) > 350:
        moving = False
        #bike blowing up animation
        bike.hideturtle()
        for t in range(12):
                bike.right(30)
                bike.forward(30)
                bike.setposition(x,y)

    if bike == tron:
        for i in range(len(tron_xList)):
            if x == tron_xList[i] and y == tron_yList[i]:
                moving = False
                bike.hideturtle()
                for t in range(12):
                    tron.right(30)
                    tron.forward(30)
                    tron.setposition(x,y)
                end_game = turtle.Turtle()
                end_game.speed(10)
                end_game.hideturtle()
                end_game.penup()
                end_game.goto(-100,30)
                end_game.color("orange")
                end_game.write("GAME OVER!", font=("Germania One",24),)
                end_game.goto(-350,-20)
                end_game.write("CONGRATUALTIONS CLU ON YOUR VICTORY!", font=("Germania One",24))
                
    if bike == clu:
        for i in range(len(clu_xList)):
            if x == clu_xList[i] and y == clu_yList[i]:
                moving = False
                bike.hideturtle()
                for t in range(12):
                    clu.right(30)
                    clu.forward(30)
                    clu.setposition(x,y)
                end_game = turtle.Turtle()
                end_game.speed(10)
                end_game.hideturtle()
                end_game.penup()
                end_game.goto(-100,30)
                end_game.color("cyan")
                end_game.write("GAME OVER!", font=("Germania One",24))
                end_game.goto(-325,-20)
                end_game.write("CONGRATUALTIONS TRON ON YOUR VICTORY!", font=("Germania One",24))

    tron_xList.append(x)
    tron_yList.append(y)

    clu_xList.append(x)
    clu_yList.append(y)

title_screen()
window.listen()
window.mainloop()