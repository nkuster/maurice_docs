import turtle as t


def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    # dieser Block zeichnet das Rechteck
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)

    t.end_fill()
    t.penup()

t.shape('turtle')
t.setpos(0, 0)

# Füsse
t.penup()
t.goto(-100, -150)
rectangle(50, 20, 'blue')

t.goto(-30, -150)
rectangle(50, 20, 'blue')

# Beine
t.goto(-25, -50)
rectangle(15, 100, 'grey')

t.goto(-65, -50)
rectangle(15, 100, 'grey')

# Rumpf
t.goto(-90, 100)
rectangle(100, 150, 'red')

# Rechter Oberarm und Unterarm
t.goto(-150, 70)
rectangle(60, 15, 'grey')

t.goto(-150, 110)
rectangle(15, 40, 'grey')

# Linker Oberarm und Unterarm
t.goto(10, 70)
rectangle(60, 15, 'grey')

t.goto(55, 110)
rectangle(15, 40, 'grey')

# Hals
t.goto(-50, 120)
rectangle(15, 20, 'grey')

# Kopf
t.goto(-85, 170)
rectangle(80, 50, 'red')

# Augen
t.goto(-60, 160)
rectangle(30, 10, 'white')

# Pupillen
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')

# Mund
t.goto(-65, 135)
rectangle(40, 5, 'black')

t.hideturtle()

