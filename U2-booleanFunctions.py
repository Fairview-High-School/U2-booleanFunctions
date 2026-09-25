import turtle

# Setup
screen = turtle.Screen()
screen.setup(600, 600)   # visible x: about -300 to 300, y: about -300 to 300
screen.delay(0) #no turtle pause after screen redraw
canvas = screen.getcanvas()
t = turtle.Turtle()
t.speed(0) #no animation time within a single turtle move
t.shape("circle") #can also use "classic","arrow","turtle","square","triangle","blank"
t.shapesize(0.5) #half the turtle shape's default size
t.penup()
t.goto(-150, 0)
t.pendown()

#1)  WRITE BOOKLEAN FUNCTIONS HERE ###########################################
# Boolean Function Definitions

#returns True when x is larger than a and less than b.  
def isInBetween(x, a, b):
    return False

# Additional boolean functions (return True or False)







#END 1) #######################################################################

#Event Handling

#converts window coordinates to turtle coordinates
def convert(windowx, windowy):
    x = canvas.canvasx(windowx)
    y = -canvas.canvasy(windowy)
    return x,y

def screenDrag(event):
    x, y = convert(event.x, event.y)
    mouseDragOnScreen(x, y)
    
def screenClick(event):
    x, y = convert(event.x, event.y)
    mouseClickOnScreen(x,y)

#this function determines what happens when you click on the screen
def mouseClickOnScreen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

#2) ADD YOUR COLOR CHANGING RULES DEPENDING ON THE X AND Y COORDINATES ########
#this function determines what happens when you drag the mouse on the screen
def mouseDragOnScreen(x, y):  # x, y is the mouse position
    t.goto(x, y)

    if isInBetween(x, -300, -100):
        t.color("red")
        
        
#END 2) #######################################################################

#setup mouse button pressed event, 
#and mouse move with mouse button pressed event
canvas.bind("<Button-1>",screenClick)
canvas.bind("<B1-Motion>", screenDrag)


# Main Script
#3) TEST ALL OF YOUR BOOLEAN FUNCTIONS ##########################################

# Test isInBetween: is the first number between the next two?
print("2 is in between 1 and 5:", isInBetween(2, 1, 5))
print("4 is in between 1 and 5:", isInBetween(4, 1, 5))
print("1 is in between 1 and 5:", isInBetween(1, 1, 5))
print("6 is in between 1 and 5:", isInBetween(6, 1, 5))

# Test your other boolean functions here to show that they work
# Try to test every case, so you know it works in all cases



#END 3) #########################################################################

turtle.mainloop()  # Keeps the window open and responding to the mouse