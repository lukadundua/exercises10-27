
import turtle

def draw_square(i, j, t, side=10, col="black"):
    x = -150 + j * side
    y = 150 - i * side
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(col)
    t.pendown()
    t.begin_fill()
    for k in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill()
    t.penup()


my_list = [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1]

t = turtle.Turtle()
t.speed(10)
t.hideturtle()

for j in range(len(my_list)):
    if my_list[j]== 1:
        draw_square(0,j, t, side=10, col="black")

# TODO: Use a for loop to iterate over the indices
# of my_list.
# If the element at index j is 1, call draw_square()
# to draw a black square at row 0, column j.


turtle.done()
