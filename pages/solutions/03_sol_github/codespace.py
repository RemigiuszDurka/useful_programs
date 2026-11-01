import random
import turtle

szerokosc = 900
wysokosc = 650
kolory = ["black", "white", "red", "yellow", "blue"]

ekran = turtle.Screen()
ekran.setup(szerokosc, wysokosc)
ekran.bgcolor("gray")
ekran.title("Losowe kolorowe kwadraty")

zolw = turtle.Turtle()
zolw.speed(0)
zolw.hideturtle()

for _ in range(50):
    rozmiar = random.randint(20, 100)
    x = random.randint(-szerokosc // 2, szerokosc // 2 - rozmiar)
    y = random.randint(-wysokosc // 2, wysokosc // 2 - rozmiar)

    zolw.penup()
    zolw.goto(x, y)
    zolw.pendown()
    zolw.fillcolor(random.choice(kolory))
    zolw.begin_fill()

    for _ in range(4):
        zolw.forward(rozmiar)
        zolw.right(90)

    zolw.end_fill()

turtle.done()
