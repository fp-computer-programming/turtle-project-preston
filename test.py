import turtle

window = turtle.Screen()
window.setup(1350,750)
window.bgcolor("black")

#Title Screen
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

title.color("Cyan")
x=0
y=0
while (x <= 180):
    title.goto(0,0)
    title.right(2)
    title.forward(245)
    title.stamp()
    while (y <= 10):
        title.forward(10)
        title.stamp()
        y += 1
    y = 0
    x += 1

window.mainloop()