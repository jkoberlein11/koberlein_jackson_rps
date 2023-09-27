import turtle
# turtle=user_choice
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 500

rock_w,rock_h = 256,280

paper_w,paper_h = 256, 204

scissors_w, scissors_h = 256, 170

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="purple")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)




# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# assign vars for rock position
rock_pos_x = -300
rock_pos_y = 0
# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)


# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# add the paper image as a shape
screen.addshape(paper_image)
# attach the paper_image to the paper_instance
paper_instance.shape(paper_image)
# remove the pen option from the paper_instance so it doesn't draw lines when moved
paper_instance.penup()
# assign vars for paper position
paper_pos_x = 0
paper_pos_y = 0
# set the position of the paper_instance
paper_instance.setpos(paper_pos_x,paper_pos_y)

# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
# add the scissors image as a shape
screen.addshape(scissors_image)
# attach the scissors_image to the scissors_instance
scissors_instance.shape(scissors_image)
# remove the pen option from the scissors_instance so it doesn't draw lines when moved
scissors_instance.penup()
# assign vars for scissors position
scissors_pos_x = 300
scissors_pos_y = 0
# set the position of the scissors_instance
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('black')
text.hideturtle()

# hide that turtle
t.hideturtle()

import turtle
from turtle import *

from random import randint
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="black")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()


def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)

# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup() 

show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)

# this function uses and x y value, an obj, and width and height 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick



def mouse_pos(x, y):
    if collide(x,y,rock_instance, rock_w, rock_h):
        print("rock")
        text.clear()
        text.write("you chose rock!!!", False, "left", ("Arial", 24, "normal"))
        paper_instance.hideturtle()
        # i need the computer to randomly choose...
        # i need to display what the computer chose and communicate winner
        # ma
    elif collide(x,y,paper_instance, paper_w, paper_h):
        print("paper")
    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        print("scissors")
    else:
        print("you chose nothing!!")

text.setpos(0,150)
text.write("Choose rock or paper or scissors", False, "left", ("Arial", 24, "normal"))

# user this to get mouse position
screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()


def mouse_pos(x, y):
    if collide(x,y,paper_instance, paper_w,paper_h):
        print ("user_choice_paper") 
    elif collide(x,y,paper_instance, paper_w,paper_h):
        print ("false")
    if collide (x,y,rock_instance, rock_w,rock_h):
        print ("user_choice_rock")
    elif collide (x,y,rock_instance, rock_w,rock_h):
        print ("false")
    if collide (x,y,scissors_instance, scissors_w,scissors_h):
        print ("user_choice_scissors")
    elif collide (x,y,scissors_instance, scissors_w,scissors_h):
        print ("false")



screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()









import random

user_action = input("Do you want to play a game...? Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print("You chose {user_action}, computer chose {computer_action}.")

if user_action == computer_action:
    print("It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("You win")
        import turtle
        from turtle import *

        # The os module allows us to access the current directory in order to access assets
        import os
        print("The current working directory is (getcwd): " + os.getcwd())
        print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
        # setup the width and height for the window
        WIDTH, HEIGHT = 1000, 400
        # setup the game folders using the os module
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # setup the Screen class using the turtle module
        screen = turtle.Screen()
        screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
        screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")
        # setup the scissors image using the os module as scissors_image
        scissors_image = os.path.join(images_folder, 'scissors.gif')
        # instantiate (create an instance of) the Turtle class for the scissors
        scissors_instance = turtle.Turtle()
        # add the the scissors image as a shape
        screen.addshape(scissors_image)
        # attach the scissors_image to the scissors_instance
        scissors_instance.shape(scissors_image)
        # remove the pen option from the scissors instance so it doesn't draw lines when moved
        scissors_instance.penup()
        scissors_pos_x = 0
        scissors_pos_y = 0
        # set the position of the scissors_instance
        scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
        # define a function that can be called when a key is pressed
        def someFunction():
            print("someFunction is doing something when a key is pressed...")
            # allow scissors_pos_x to be accessed outside the function using 'global'
            global scissors_pos_x
            # change scissors_pos_x by 5
            scissors_pos_x += 5
            # set the new scissors position...
            scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
        # have the turtle module use the onkey to run a function when pressing
        turtle.onkey(someFunction, "r")  # This will call the up function if the "Left" arrow key is pressed
        # have the turtle module 'listen' for when keys are pressed
        turtle.listen()
        # when the turtle 'x' key is pressed then quit turtle
        turtle.done()
    else:
        print("you (° ͜ʖ ͡°) lose")
        import turtle
        from turtle import *
        # The os module allows us to access the current directory in order to access assets
        import os
        print("The current working directory is (getcwd): " + os.getcwd())
        print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
        # setup the width and height for the window
        WIDTH, HEIGHT = 1000, 400
        # setup the game folders using the os module
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # setup the Screen class using the turtle module
        screen = turtle.Screen()
        screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
        screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")
        # setup the paper image using the os module as paper_image
        paper_image = os.path.join(images_folder, 'paper.gif')
        # instantiate (create an instance of) the Turtle class for the paper
        paper_instance = turtle.Turtle()
        # add the the paper image as a shape
        screen.addshape(paper_image)
        # attach the paper_image to the paper_instance
        paper_instance.shape(paper_image)
        # remove the pen option from the paper instance so it doesn't draw lines when moved
        paper_instance.penup()
        paper_pos_x = 0
        paper_pos_y = 0
        # set the position of the paper_instance
        paper_instance.setpos(paper_pos_x,paper_pos_y)
        # define a function that can be called when a key is pressed
        def someFunction():
            print("someFunction is doing something when a key is pressed...")
            # allow paper_pos_x to be accessed outside the function using 'global'
            global paper_pos_x
            # change paper_pos_x by 5
            paper_pos_x += 5
            # set the new paper position...
            paper_instance.setpos(paper_pos_x,paper_pos_y)
        # have the turtle module use the onkey to run a function when pressing
        turtle.onkey(someFunction, "r")  # This will call the up function if the "Left" arrow key is pressed
        # have the turtle module 'listen' for when keys are pressed
        turtle.listen()
        # when the turtle 'x' key is pressed then quit turtle
        turtle.done()
elif user_action == "paper":
    if computer_action == "rock":
        print("You win")
        import turtle
        from turtle import *
        # The os module allows us to access the current directory in order to access assets
        import os
        print("The current working directory is (getcwd): " + os.getcwd())
        print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
        # setup the width and height for the window
        WIDTH, HEIGHT = 1000, 1000
        # setup the game folders using the os module
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # setup the Screen class using the turtle module
        screen = turtle.Screen()
        screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
        screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")
        # setup the rock image using the os module as rock_image
        rock_image = os.path.join(images_folder, 'rock.gif')
        # instantiate (create an instance of) the Turtle class for the rock
        rock_instance = turtle.Turtle()
        # add the the rock image as a shape
        screen.addshape(rock_image)
        # attach the rock_image to the rock_instance
        rock_instance.shape(rock_image)
        # remove the pen option from the rock instance so it doesn't draw lines when moved
        rock_instance.penup()
        rock_pos_x = 0
        rock_pos_y = 0
        # set the position of the rock_instance
        rock_instance.setpos(rock_pos_x,rock_pos_y)
        # define a function that can be called when a key is pressed
        def someFunction():
            print("someFunction is doing something when a key is pressed...")
            # allow rock_pos_x to be accessed outside the function using 'global'
            global rock_pos_x
            # change rock_pos_x by 5
            rock_pos_x += 5
            # set the new rock position...
            rock_instance.setpos(rock_pos_x,rock_pos_y)
        # have the turtle module use the onkey to run a function when pressing
        turtle.onkey(someFunction, "r")  # This will call the up function if the "Left" arrow key is pressed
        # have the turtle module 'listen' for when keys are pressed
        turtle.listen()
        # when the turtle 'x' key is pressed then quit turtle
        turtle.done()

    else:
        print("you (° ͜ʖ ͡°) lose")
        import turtle

        from turtle import *

        # The os module allows us to access the current directory in order to access assets
        import os
        print("The current working directory is (getcwd): " + os.getcwd())
        print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
        # setup the width and height for the window
        WIDTH, HEIGHT = 1000, 400
        # setup the game folders using the os module
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # setup the Screen class using the turtle module
        screen = turtle.Screen()
        screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
        screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")
        # setup the scissors image using the os module as scissors_image
        scissors_image = os.path.join(images_folder, 'scissors.gif')
        # instantiate (create an instance of) the Turtle class for the scissors
        scissors_instance = turtle.Turtle()
        # add the the scissors image as a shape
        screen.addshape(scissors_image)
        # attach the scissors_image to the scissors_instance
        scissors_instance.shape(scissors_image)
        # remove the pen option from the scissors instance so it doesn't draw lines when moved
        scissors_instance.penup()
        scissors_pos_x = 0
        scissors_pos_y = 0
        # set the position of the scissors_instance
        scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
        # define a function that can be called when a key is pressed
        def someFunction():
            print("someFunction is doing something when a key is pressed...")
            # allow scissors_pos_x to be accessed outside the function using 'global'
            global scissors_pos_x
            # change scissors_pos_x by 5
            scissors_pos_x += 5
            # set the new scissors position...
            scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
        # have the turtle module use the onkey to run a function when pressing
        turtle.onkey(someFunction, "r")  # This will call the up function if the "Left" arrow key is pressed
        # have the turtle module 'listen' for when keys are pressed
        turtle.listen()
        # when the turtle 'x' key is pressed then quit turtle
        turtle.done()
elif user_action == "scissors":
    if computer_action == "paper":
        print("You win")
        import turtle
        from turtle import *
        # The os module allows us to access the current directory in order to access assets
        import os
        print("The current working directory is (getcwd): " + os.getcwd())
        print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
        # setup the width and height for the window
        WIDTH, HEIGHT = 1000, 400
        # setup the game folders using the os module
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # setup the Screen class using the turtle module
        screen = turtle.Screen()
        screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
        screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")
        # setup the paper image using the os module as paper_image
        paper_image = os.path.join(images_folder, 'paper.gif')
        # instantiate (create an instance of) the Turtle class for the paper
        paper_instance = turtle.Turtle()
        # add the the paper image as a shape
        screen.addshape(paper_image)
        # attach the paper_image to the paper_instance
        paper_instance.shape(paper_image)
        # remove the pen option from the paper instance so it doesn't draw lines when moved
        paper_instance.penup()
        paper_pos_x = 0
        paper_pos_y = 0
        # set the position of the paper_instance
        paper_instance.setpos(paper_pos_x,paper_pos_y)
        # define a function that can be called when a key is pressed
        def someFunction():
            print("someFunction is doing something when a key is pressed...")
            # allow paper_pos_x to be accessed outside the function using 'global'
            global paper_pos_x
            # change paper_pos_x by 5
            paper_pos_x += 5
            # set the new paper position...
            paper_instance.setpos(paper_pos_x,paper_pos_y)
        # have the turtle module use the onkey to run a function when pressing
        turtle.onkey(someFunction, "r")  # This will call the up function if the "Left" arrow key is pressed
        # have the turtle module 'listen' for when keys are pressed
        turtle.listen()
        # when the turtle 'x' key is pressed then quit turtle
        turtle.done()
    else:
        print("you (° ͜ʖ ͡°) lose")
        import turtle
        from turtle import *
        # The os module allows us to access the current directory in order to access assets
        import os
        print("The current working directory is (getcwd): " + os.getcwd())
        print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
        # setup the width and height for the window
        WIDTH, HEIGHT = 1000, 1000
        # setup the game folders using the os module
        game_folder = os.path.dirname(__file__)
        images_folder = os.path.join(game_folder, 'images')
        # setup the Screen class using the turtle module
        screen = turtle.Screen()
        screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
        screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")
        # setup the rock image using the os module as rock_image
        rock_image = os.path.join(images_folder, 'rock.gif')
        # instantiate (create an instance of) the Turtle class for the rock
        rock_instance = turtle.Turtle()
        # add the the rock image as a shape
        screen.addshape(rock_image)
        # attach the rock_image to the rock_instance
        rock_instance.shape(rock_image)
        # remove the pen option from the rock instance so it doesn't draw lines when moved
        rock_instance.penup()
        rock_pos_x = 0
        rock_pos_y = 0
        # set the position of the rock_instance
        rock_instance.setpos(rock_pos_x,rock_pos_y)
        # define a function that can be called when a key is pressed
        def someFunction():
            print("someFunction is doing something when a key is pressed...")
            # allow rock_pos_x to be accessed outside the function using 'global'
            global rock_pos_x
            # change rock_pos_x by 5
            rock_pos_x += 5
            # set the new rock position...
            rock_instance.setpos(rock_pos_x,rock_pos_y)
        # have the turtle module use the onkey to run a function when pressing
        turtle.onkey(someFunction, "r")  # This will call the up function if the "Left" arrow key is pressed
        # have the turtle module 'listen' for when keys are pressed
        turtle.listen()
        # when the turtle 'x' key is pressed then quit turtle
        turtle.done()
