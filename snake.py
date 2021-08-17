import turtle
import time
import random
posponer = 0.1
window = turtle.Screen()
window.title("Hola Erick")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# cuerpo
segmentos = []

# score
score = 0
high_score = 0

# text
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0       Hight score:0",
            align="center", font=("courier", 24, "normal"))

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)


# funciones
def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def izquierda():
    cabeza.direction = "left"


def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down" :
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left" :
        x = cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction == "right" :
        x = cabeza.xcor()
        cabeza.setx(x+20)


# Teclado
window.listen()
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")
window.onkeypress(derecha, "Right")


while True:
    window.update()
    # bordes
    if cabeza.xcor() > 290 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        for seg in segmentos:
            seg.goto(1000, 1000)
        segmentos.clear()

        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # reset
        score = 0
        texto.clear()
        texto.write("Score: {}       Hight score:{}".format(
            score, high_score), align="center", font=("courier", 24, "normal"))

    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        # marcador
        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write("Score: {}       Hight score:{}".format(
            score, high_score), align="center", font=("courier", 24, "normal"))
    # mover cuerpo serp
    total = len(segmentos)
    for ind in range(total - 1, 0, -1):
        x = segmentos[ind-1].xcor()
        y = segmentos[ind-1].ycor()
        segmentos[ind].goto(x, y)

    if total > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()
    for seg in segmentos:
        if seg.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)           
            cabeza.direction = "stop"
            for segm in segmentos:
                segm.goto(1000, 1000)
            segmentos.clear()
            score = 0
            texto.clear()
            texto.write("Score: {}       Hight score:{}".format(
            score, high_score), align="center", font=("courier", 24, "normal"))

    time.sleep(posponer)
