"""Leo Xu, 400688437.
This program is a small fun game that consists of two players. Player 1 enters a coordinate of the place they decide to hide at, and Player 2 has 4 attempts to guess the coordinate that Player 1 had entered in."""


import turtle
import time
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Hide and Seek, Island Edition"
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.bgcolor("#1E6091")
screen.title(WINDOW_TITLE)
screen.tracer(0)
bg = turtle.Turtle() #One turtle is used for the background
bg.hideturtle()
bg.speed(0)
t = turtle.Turtle() #Another turtle is used for the game itself
t.hideturtle()
t.speed(0)
 ## Screen Functions

def draw_beach():

    """Draws the sand in the background"""
    bg.clear()
    screen.bgcolor("#87CEEB")
    bg.penup()
    bg.goto(-300, -180)
    bg.setheading(0)
    bg.pendown()
    bg.color("#D9B45B", "#F4D58D")
    bg.begin_fill()
    for i in range(2):
        bg.forward(600)
        bg.right(90)
        bg.forward(120)
        bg.right(90)
    bg.end_fill()
    bg.penup()

def draw_board():

    """Draws the sign that depicts the instructions and information"""

    t.clear()
    t.hideturtle()
    t.pensize(3)
    t.penup()
    t.goto(-12, -20)
    t.setheading(0)
    t.pendown()
    t.color("#654321", "#996633")
    t.begin_fill()
    for i in range(2):
        t.forward(24)
        t.right(90)
        t.forward(180)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(-210, 120)
    t.setheading(0)
    t.pendown()
    t.color("#654321", "#B9824A")
    t.begin_fill()
    for i in range(2):
        t.forward(430)
        t.right(90)
        t.forward(220)
        t.right(90)
    t.end_fill()
    t.penup()


def splash_screen():

    """Calls the beach and board function to provide the initial background, then on the board, it writes out the instructions and information"""

    draw_beach()
    draw_board()
    t.color("#4B2E1D")
    t.goto(0, 75)
    t.write("Ahoy there!", align = "center", font=("Arial", 24, "bold"))
    t.goto(0, 42)
    t.write("You have been stranded on a deserted island", align="center", font=("Arial", 12, "bold"))
    t.goto(0, 22)
    t.write("while running from pirates!", align="center", font=("Arial", 12, "bold"))
    t.goto(0, -10)
    t.write("Player 1: Choose a hiding spot!", align="center", font=("Arial", 11, "normal"))
    t.goto(0, -35)
    t.write("Player 2: Find the escapee!", align="center", font=("Arial", 11, "normal"))
    t.goto(0, -60)
    t.write("You have 4 guesses. Good luck!", align="center", font=("Arial", 11, "normal"))
    screen.update()


def display_screen():

    """Calls the beach and board function again to provide the initial background, and then on the board, it writes out the game results which include the total distance, score and closest distance"""

    draw_beach()
    draw_board()
    t.color("#4B2E1D")
    t.goto(0, 80)
    t.write("GAME RESULTS", align="center",font=("Arial", 22, "bold"))
    t.goto(0, 45)
    t.write(f"Total Distance: {round(total_distance, 2)}", align="center", font=("Arial", 13, "normal"))
    t.goto(0, 0)
    t.write(f"Total Score: {round(total_score, 2)}", align="center",font=("Arial", 13, "normal"))
    t.goto(0, -40)
    t.write(f"Closest Distance: {round(closest_distance, 2)}", align="center", font=("Arial", 13, "normal"))
    t.goto(0, -80)
    t.write("HOPE YOU ESCAPED!", align="center", font=("Arial", 22, "bold"))
    screen.update()

## Splash Screen

splash_screen() #Calls the splash screen function made above
time.sleep(4)
t.clear()
bg.clear()
screen.bgcolor("#1E6091")
screen.update()


##Background Functions
Island_Radius = 280 #sets an radius for the island that will be used in the island function

def island(x, y, size, color, sides):

    """Draws an regular rounded shape. It includes parameters such as the x and y position, the size of the island, the color, and the rounded shape is given by the sides parameter which depicts the amount of sides the island should have """

    bg.penup()
    bg.goto(x, y - size)
    bg.pendown()
    bg.fillcolor(color)
    bg.begin_fill()
    exterior_angle = 360 / sides #calculates the exterior angle of the polygon
    for i in range(sides): #Uses a for loop to draw a regular polygon with n amount of sides
        bg.forward(size * 0.3)
        bg.left(exterior_angle) #Turns left a certain angle depending on the number of sides
    bg.end_fill()


def mountain(x, y, size):

    """Draws a small cluster of brown triangles to look like a mountain range, as well as snow caps on top of it. Parameters include the x and y position, and the size of the mountains"""

    bg.penup()
    bg.goto(x, y)
    bg.pendown()
    bg.fillcolor("#8B7355")
    bg.begin_fill()
    bg.setheading(90)
    bg.forward(size)
    bg.right(150)
    bg.forward(size * 1.3)
    bg.right(120)
    bg.forward(size * 1.3)
    bg.end_fill()
    bg.penup() #snow cap
    bg.goto(x, y + size * 0.6)
    bg.pendown()
    bg.fillcolor("white")
    bg.begin_fill()
    bg.setheading(90)
    bg.forward(size * 0.4)
    bg.right(150)
    bg.forward(size * 0.5)
    bg.right(120)
    bg.forward(size * 0.5)
    bg.end_fill()



def sail_boat(x, y, size=1):

    """Draws a sail boat on the top left corner of the screen that represents the pirates ship. Parameters include the x and y position of the ship, and the size is a fixed value of 1"""

    bg.penup()
    bg.goto(x - 40 * size, y)
    bg.setheading(0)
    bg.pendown()
    bg.fillcolor("#8B4513")
    bg.begin_fill()
    bg.forward(50 * size)
    bg.right(130)
    bg.forward(25 * size)
    bg.end_fill()
    bg.penup()
    bg.goto(x, y)
    bg.setheading(90)
    bg.pendown()
    bg.pencolor("black")
    bg.forward(90 * size)
    bg.penup()
    bg.goto(x, y + 88 * size)
    bg.setheading(-90)
    bg.pendown()
    bg.fillcolor("white")
    bg.begin_fill()
    bg.forward(75 * size)
    bg.right(125)
    bg.forward(60 * size)
    bg.right(125)
    bg.forward(45 * size)
    bg.end_fill()
    bg.penup()
    bg.goto(x, y + 88 * size)
    bg.setheading(-90)
    bg.pendown()
    bg.fillcolor("#F4E285")
    bg.begin_fill()
    bg.forward(50 * size)
    bg.right(145)
    bg.forward(42 * size)
    bg.right(115)
    bg.forward(35 * size)
    bg.end_fill()
    bg.penup()
    bg.goto(x, y + 90 * size)
    bg.setheading(0)
    bg.pendown()
    bg.fillcolor("red")
    bg.begin_fill()
    bg.forward(15 * size)
    bg.right(150)
    bg.forward(8 * size)
    bg.right(120)
    bg.forward(8 * size)
    bg.end_fill()
    bg.penup()

def long_lake(x, y, width, height):

    """Draws an oval shaped lake using the circle function. The x and y parameter is the position of the lake, width and height act as radii for the circle functions below."""

    bg.penup()
    bg.goto(x, y - height)
    bg.setheading(0)
    bg.pendown()
    bg.fillcolor("#3FA7D6")
    bg.begin_fill()
    for i in range(2):
        bg.circle(width, 90, 20)
        bg.circle(height, 90, 20)
    bg.end_fill()


def tree(x, y, size):

    """Draws circles of radii parameter 'size' to depict trees, and x and y parameter is the position."""

    bg.penup()
    bg.goto(x, y - size)
    bg.pendown()
    bg.fillcolor("#2D6A4F")
    bg.begin_fill()
    bg.circle(size)
    bg.end_fill()


## Draw Island Base
island(0, 0, Island_Radius, "#D9C589", sides = 18) #Draws the outer island shape that consists of the beach using the island function

island(0, 0, Island_Radius - 25, "#8FBF6B", sides=18)
#Draws the inland grass area hat consists of the mountains, trees and lake using the island function

## Draw Mountains

"""Draws three mountains using the mountain function"""

mountain(-90, 110, 80)
mountain(0, 130, 80)
mountain(90, 110, 80)

## Draw Lake

"""Draws a lake using the long lake function"""

long_lake(-70, -150, 70, 25)

## Draw Trees

"""Draws 5 trees using the tree function"""

tree(-150, 20, 18)
tree(-110, -40, 16)
tree(130, 10, 18)
tree(100, -50, 16)
tree(0, -30, 15)

## Draw Sailboat

"""Draws a sail boat using the sail boat function"""

sail_boat(-200, 200, size=1)

bg.hideturtle()
screen.update()

##User Inputs

t.hideturtle()
hide_x = int(screen.numinput("Config", "User 1: Enter your x coordinate (-300, 300)")) #User 1 inputs the x-coordinate of their desired hiding spot
hide_y = int(screen.numinput("Config", "User 1: Enter your y coordinate (-300, 300)")) #User 1 inputs the y-coordinate of their desired hiding spot
t.up() #Forbids the turtle to draw a line as it goes to the hiding spot
t.goto(hide_x, hide_y) #Goes to hiding spot
t.dot(10) #Shows User 1 where they hid
screen.update()
time.sleep(2)
t.clear() #Clears the board for User 2
total_distance = 0 #Variable initialization of distance
total_score = 0 #Variable initialization of score
distances = [] #Sets up an initial empty list for the 4 distances
for i in range(4): #Allows User 2 to input 4 different guesses
    guess_x = int(screen.numinput("Config", "User 2: Enter your x coordinate guess (-300, 300)"))
    guess_y = int(screen.numinput("Config", "User 2: Enter your y coordinate guess (-300, 300)"))
    t.up()
    t.goto(guess_x, guess_y)
    t.pencolor("red")
    t.dot(10)
    distance = round(math.sqrt((hide_x - guess_x)**2 + (hide_y - guess_y)**2)) #Calculates the distance that User 2 is from the hiding spot
    distances.append(distance) #Uses the append method to add the 4 distance values into the previous empty list
    score = round((max(200 - distance, 0)**2)/400, 2) #Calculates the score User 2 has gotten from their guess
    total_distance += distance #Calculates the total distance through all guesses
    total_score += score #Calculates the total score through all guesses
    t.write(f"distance: {distance}", align = "center", font = ('Arial', 9, "normal")) #Depicts the distance to User 2
    t.goto(guess_x, guess_y + 15)
    t.write(f"score: {score}", align = "center", font = ('Arial', 9, 'normal')) #Depicts the score to User 2
    screen.update()
    time.sleep(2)
closest_distance = min(distances) #Closest distance is the smallest distance in the distances list

t.goto(hide_x, hide_y)
t.dot(10)
t.showturtle() #Shows User 2 where the hiding spot was
screen.update()
time.sleep(4)

##End Display

"""Uses the display screen function to provide the total distance, total score, and closest distance"""

display_screen()

screen.exitonclick()