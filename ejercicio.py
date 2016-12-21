# -*- coding: cp1252 -*-
import turtle
t=turtle.Pen()

A=int(input ("Ingrese los lados de la estrella: "))

for x in range(A):
    t.forward(108)
    t.left(((A-2)*180)/A)
    t.left(((A-2)*180)/A)

    t.forward(100)
    t.left(360/A)

t.reset() 
tamano=int(input ("Ingrese el tamaño del cuadrado: "))
def cuadrado ( tamano ):
    for x in range(0,5):
        t.forward(tamano)
        t.left(90)

cuadrado(tamano)

t.reset()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(100)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(90)
t.forward(175)


turtle.getscreen()._root.mainloop()
