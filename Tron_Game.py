# Author: PCL 3/22/23

import turtle

#creating the screen, its dimensions, and its background color
window = turtle.Screen()
window.setup(1350,750)
window.bgcolor("black")

#Title Screen
def title_screen():
    global title
    global initialize_1
    global initialize_2

    #creating a turtle which will write the title of the game TRON followed by the control instructions for each player in smaller text right below the title
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

    #creating a turtle which will draw one half of the title/loading animation I made
    initialize_1 = turtle.Turtle()
    initialize_1.color("Cyan")
    initialize_1.shape("square")
    initialize_1.shapesize(.1)
    initialize_1.speed(0)
    initialize_1.penup()
    initialize_1.hideturtle()

    #creating a turtle which will draw one half of the title/loading animation I made    
    initialize_2 = turtle.Turtle()
    initialize_2.color("Cyan")
    initialize_2.shape("square")
    initialize_2.shapesize(.1)
    initialize_2.speed(0)
    initialize_2.penup()
    initialize_2.hideturtle()

    #creating the first line of the animation which would be skipped in the following loop
    y=0
    initialize_1.forward(245)
    initialize_1.stamp()
    while (y <= 10):
            initialize_1.forward(10)
            initialize_1.stamp()
            y += 1

    x=0
    y=0
    #drawing a ring of dots around the title in a circle which has multiple slightly spaced out layers to look like a game initializing / booting up
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
    
    #promting the users to press enter when they are ready to begin the game
    title.goto(-57,-60)
    title.write("Press Enter to Begin", font=("Germania One", 9))
    window.onkey(title_cleanup, "Return")

#Function which erases the title screen to empty the map for the bikes to play on and starts the setup
def title_cleanup():
    title.hideturtle()
    initialize_1.hideturtle()
    initialize_2.hideturtle()
    title.clear()
    initialize_1.clear()
    initialize_2.clear()
    setup()

#Function for the onkey for Tron turning right
def tron_right():
    global tron

    tron.right(90)
    tron.speed(10)

#Function for the onkey for Tron turning left
def tron_left():
    global tron
    
    tron.left(90)
    tron.speed(10)

#Function for the onkey for Clu turning left
def clu_left():
    global clu
    
    clu.left(90)
    clu.forward(1)

#Function for the onkey for Clu turning right
def clu_right():
    global clu
    
    clu.right(90)
    clu.forward(1)

#creates both bikes and the boundary
def setup():

    global clu
    global tron
    global tron_xList
    global tron_yList
    global clu_xList
    global clu_yList
    global window

    #creating the empty lists where the coordinates for every point where each bike has been will be recorded
    clu_xList = []
    clu_yList = []
    tron_xList = []
    tron_yList = []

    #Boundary - drawing a box
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

    #Bikes - creating tron and clu with their respective colors and speeds
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

    #calling the function to begin the movement of the game
    movement()

#Returns the current coordinate of whichever turtle is called as seperate x and y variables
def coordinates(bike):
    x = bike.xcor()
    y = bike.ycor()
    return x, y

#Movement of both players
def movement():
    global clu
    global tron
    global moving

    #setting moving equal to true to have a while loop that runs until a condition such as out of map or collision sets it to false
    moving = True

    #While loop as long as moving equals true
    while moving != False:
        #each time the loop is iterated both bikes move forward 1 pixel
        tron.forward(1)
        clu.forward(1)

        #making sure that the turn commands will be listened to by the code
        window.listen()

        #Left and right controls for Tron
        window.onkey(tron_right, "Right")
        window.onkey(tron_left, "Left")

        #Left and right controls for Clu
        window.onkey(clu_left, "q")
        window.onkey(clu_right, "e")

        #after every single individual movement both bikes individually have their coordinates checked to determine if either has gone out of the map or hit eachothers lines
        x,y = coordinates(tron)
        bikecheck(x, y, tron)

        x,y = coordinates(clu)
        bikecheck(x, y, clu)      

#Checks current coordinates of 1 bike at a time against a list of previous coordinates, checks if out of map, and writes end of game text
def bikecheck(x,y,bike):
    global moving
    global tron_xList
    global tron_yList
    global clu_xList
    global clu_yList

    #getting the names of the bikes and their colors based on their variable name to have a string for the winner or loser if one of the players goes out of map
    if (bike == tron):
        bike_name = "TRON"
        bike_color = "cyan"

    if (bike == clu):
        bike_name = "CLU"
        bike_color = "orange"

    #Checking if either of the bikes is out of range of the map
    if abs(x)> 650 or abs(y) > 350:
        #stopping all movement
        moving = False
        #explosion of losing bike animation
        bike.hideturtle()
        for t in range(12):
            bike.right(30)
            bike.forward(30)
            bike.setposition(x,y)
        #creating a seperate turtle that writes the end game text for the winner and the loser
        end_game = turtle.Turtle()
        end_game.speed(10)
        end_game.hideturtle()
        end_game.penup()
        end_game.goto(-100,30)
        end_game.color(bike_color)
        end_game.write("GAME OVER!", font=("Germania One",24),)
        end_game.goto(-350,-20)
        end_game.write("CONGRATUALTIONS "+bike_name+" ON YOUR VICTORY!", font=("Germania One",24))

    #Tron hit-check
    if bike == tron:
        #looping over cooridnate list for Tron
        for i in range(len(tron_xList)):
            #checking each individual coordinate in the list of previous coordinates of both bikes, against the current coordinate of clu
            if x == tron_xList[i] and y == tron_yList[i]:
                #stopping all movement
                moving = False
                #hiding the losing bike
                bike.hideturtle()
                #explosion of losing bike animation
                for t in range(12):
                    tron.right(30)
                    tron.forward(30)
                    tron.setposition(x,y)
                #creating a seperate turtle that writes the end game text for the winner and the loser
                end_game = turtle.Turtle()
                end_game.speed(10)
                end_game.hideturtle()
                end_game.penup()
                end_game.goto(-100,30)
                end_game.color("orange")
                end_game.write("GAME OVER!", font=("Germania One",24),)
                end_game.goto(-350,-20)
                end_game.write("CONGRATUALTIONS CLU ON YOUR VICTORY!", font=("Germania One",24))

    #CLU hit-check            
    if bike == clu:
        #looping over cooridnate list for Clu
        for i in range(len(clu_xList)):
            #checking each individual coordinate in the list of previous coordinates of both bikes, against the current coordinate of clu
            if x == clu_xList[i] and y == clu_yList[i]:
                #stopping all movement
                moving = False
                #hiding the losing bike
                bike.hideturtle()
                #explosion of losing bike animation
                for t in range(12):
                    clu.right(30)
                    clu.forward(30)
                    clu.setposition(x,y)
                #creating a seperate turtle that writes the end game text for the winner and the loser
                end_game = turtle.Turtle()
                end_game.speed(10)
                end_game.hideturtle()
                end_game.penup()
                end_game.goto(-100,30)
                end_game.color("cyan")
                end_game.write("GAME OVER!", font=("Germania One",24))
                end_game.goto(-325,-20)
                end_game.write("CONGRATUALTIONS TRON ON YOUR VICTORY!", font=("Germania One",24))

    #Recording the current coordinates of the bike and adding it to a list which is used to check hitboxes for Tron
    tron_xList.append(x)
    tron_yList.append(y)

    #Recording the current coordinates of the bike and adding it to a list which is used to check hitboxes for Clu
    clu_xList.append(x)
    clu_yList.append(y)

#Calling the title screen function to start the game
title_screen()

#Taste, Smell, Touch
window.listen()
window.mainloop()