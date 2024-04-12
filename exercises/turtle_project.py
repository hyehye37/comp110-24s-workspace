"""A house with multiple windows."""

__author__ = "730695168"

from turtle import Turtle, done 

width: int = 200


def main() -> None:
    """The entrypoint of my scene. A house with a rectangle chimney, a triangular roof, a pentagon shaped window, and a square body."""
    # TODO: Declare your Turtle variable(s) here.
    roof: Turtle = Turtle()
    square: Turtle = Turtle()
    chimney: Turtle = Turtle()
    pentagon_window: Turtle = Turtle()
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    roof.color("green", "yellow")
    draw_square(square, -150, -50)
    draw_roof(roof, -150, -50)
    draw_chimney(chimney, 0, 200)
    draw_pentagon_window(pentagon_window, -70, -10)
    done()


# TODO: Define the procedures for other components in your scene here.
def draw_square(square: Turtle, x: float, y: float) -> None:
    """Draw the square shaped body of a house given the x and y coordintes."""
    square.penup()
    square.goto(x, y)
    square.setheading(0.0)
    square.pendown()
    i: int = 0
    while i < 4:
        square.forward(width)
        square.right(90)
        i = i + 1
    

def draw_roof(roof: Turtle, x: float, y: float) -> None:
    """Draw the triangular roof of a house given the x and y coordinates."""
    roof.begin_fill()
    roof.penup()
    roof.goto(x, y)
    roof.setheading(0.0)
    roof.pendown()
    f(3, roof)
    roof.end_fill()
    # turning the while loop into recursion function


def f(i: int, roof: Turtle) -> int:
    """Recursive rule to draw a roof."""
    if i <= 0:  # base case 
        return 1
    else:  # recursive rule
        roof.forward(width)
        roof.left(120)
        return 1 + f(i - 1, roof)
        

def draw_chimney(chimney: Turtle, x: float, y: float) -> None:
    """Draw the rectangular chimney of a house given the x and y coordinates."""
    chimney.penup()
    chimney.goto(x, y)
    chimney.setheading(0.0)
    chimney.pendown()
    chimney.forward(50)
    chimney.right(90)
    chimney.forward(width)
    chimney.right(90)
    chimney.forward(50)
    chimney.right(90)
    chimney.forward(width)
    chimney.right(90)
            

def draw_pentagon_window(pentagon_window: Turtle, x: float, y: float) -> None:
    """Draw a pentagon shaped window on the roof given the x and y coordinates."""
    pentagon_window.penup()
    pentagon_window.goto(x, y)
    pentagon_window.setheading(0.0)
    pentagon_window.pendown()
    i: int = 0
    while i < 5:
        pentagon_window.forward(50)
        pentagon_window.left(72)
        i = i + 1
 

# TODO: Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__": 
    main()