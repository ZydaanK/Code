# says hello there
print("Hello there...")
# a 480 x 720 white screen that also has a system that creates a cursor and lines that travels for a certain predetermined 
from turtle import *
# colors of line and cursor
color('red', 'yellow')
# starts the drawing (program)
begin_fill()
# does not fill
while True:
    # how many pixels it travels for
    forward(200)
    # how many degrees it turns and which direction
    left(170)
    right (1)
    if abs(pos()) < 1:
        # stops movement
        break
# fills the shape with the color
end_fill()
# finished
done()