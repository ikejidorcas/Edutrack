import turtle as t
t.bgcolor('blue')
t.pensize(5)
t.speed(1)
t.color('black')
t.begin_fill()
t.fillcolor('red')
t.left(150)
t.forward(180)
t.circle(-90, 180)
t.setheading(60)
t.circle(-90, 180)
t.forward(180)
t.end_fill()
t.hideturtle()
msg = 'I LOVE YOU ❤💕'
t.write(msg,move=True, align='left', font=('Arial', 25, 'italic', 'bold'))

t.done

