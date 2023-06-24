import turtle

def draw_fractal_tree(branch_length, angle, depth):
    if depth == 0:
        return
    if depth < 3:
        turtle.color("green")  
    else:
        turtle.color("brown")  

    turtle.forward(branch_length)
    turtle.left(angle)
    draw_fractal_tree(branch_length * 0.7, angle, depth - 1)
    turtle.right(angle * 2)
    draw_fractal_tree(branch_length * 0.7, angle, depth - 1)
    turtle.left(angle)
    turtle.backward(branch_length)

turtle.setup(width=800, height=600)  
turtle.speed(0)  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.penup()
turtle.goto(0, -250)  
turtle.pendown()

turtle.left(90)
draw_fractal_tree(80, 30, 7)
turtle.done()
