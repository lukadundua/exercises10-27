
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


# Read the first line from the file
file = open("pattern.txt")
line = file.readline()
file.close()

my_list = []
for c in line:
    if c == "#":
        my_list.append(1)
    elif c ==" ":
        my_list.append(0)
# TODO: Iterate over the characters in line.
# Append 1 for each '#' and 0 for each space.
# Ignore any newline character.


print(my_list)

t = turtle.Turtle()
t.speed(10)
t.hideturtle()
for j in range(len(my_list)):
    if my_list[j]== 1:
        draw_square(0,j, t, side=10, col="black")

# TODO: Iterate over the indices of my_list.
# Draw a black square at row 0, column j
# whenever my_list[j] is 1.


turtle.done()
