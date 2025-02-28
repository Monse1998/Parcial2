from turtle import *

# Creación del laberinto (Kuro)
kuro = Turtle()
kuro.penup()
kuro.color("black")
kuro.pensize(10)
kuro.goto(-225, 190)
kuro.pendown()

# Dibuja la primera parte del laberinto
kuro.forward(100)
kuro.right(90)
kuro.forward(80)
kuro.backward(80)
kuro.left(90)
kuro.forward(400)
kuro.right(90)
kuro.forward(190)
kuro.right(90)
kuro.forward(80)
kuro.right(90)
kuro.forward(80)
kuro.backward(80)
kuro.left(90)
kuro.forward(100)
kuro.left(90)
kuro.forward(80)
kuro.right(90)
kuro.forward(120)
kuro.left(90)
kuro.forward(80)

# Creación del laberinto (Laberinto)
Laberinto = Turtle()

# Establecemos el color de fondo de la ventana

Laberinto.pensize(10)
Laberinto.penup()
Laberinto.goto(-225, 75)
Laberinto.pendown()

# Dibuja el laberinto en la parte inferior
Laberinto.right(90)
Laberinto.forward(400)
Laberinto.left(90)
Laberinto.forward(500)
Laberinto.left(90)
Laberinto.forward(175)
Laberinto.left(90)
Laberinto.forward(100)
Laberinto.left(90)
Laberinto.forward(100)
Laberinto.right(90)
Laberinto.forward(200)

# Dibuja la segunda parte del laberinto
Laberinto.penup()
Laberinto.goto(-225, -25)
Laberinto.pendown()
Laberinto.backward(200)
Laberinto.right(90)
Laberinto.forward(100)
Laberinto.right(90)
Laberinto.forward(100)

# Terminamos de mostrar el laberinto
done()
