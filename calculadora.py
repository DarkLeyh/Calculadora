#import tkinter
from tkinter import *

#Iniciando una vista de la ventana
ventana = Tk()

#Dandole tamaño a la ventana
ventana.geometry("392x500")

#Dandole titulo a la ventana
ventana.title("Mi calculadora basica en Python")

salida = Entry(ventana, font=('arial', 20, 'bold'),width=22, bd = 20, insertwidth = 4, bg = "pink", justify="right")
salida.place(x=10, y=60)

#variable global
i=0

#Funciones
#poner numeros en la salida
def boton(value):
    global i
    salida.insert(i, value)
    i += 1

#borrar texto de la pantalla
def borrar():
    salida.delete(0, END)
    i = 0

#hacer la operacion
def operacion():
    ecuacion = salida.get()
    resultado = eval(ecuacion)
    salida.delete(0, END)
    salida.insert(0, resultado)
    i = 0

#poniendo botones
boton1 = Button(ventana, text="1", width = 9, height = 3, command = lambda: boton(1))
boton1.place(x=37, y=220)

boton2 = Button(ventana, text="2", width = 9, height = 3, command = lambda: boton(2))
boton2.place(x=117, y=220)

boton3 = Button(ventana, text="3", width = 9, height = 3, command = lambda: boton(3))
boton3.place(x=197, y=220)

boton4 = Button(ventana, text="4", width = 9, height = 3, command = lambda: boton(4))
boton4.place(x=37, y=280)

boton5 = Button(ventana, text="5", width = 9, height = 3, command = lambda: boton(5))
boton5.place(x=117, y=280)

boton6 = Button(ventana, text="6", width = 9, height = 3, command = lambda: boton(6))
boton6.place(x=197, y=280)

boton7 = Button(ventana, text="7", width = 9, height = 3, command = lambda: boton(7))
boton7.place(x=37, y=340)

boton8 = Button(ventana, text="8", width = 9, height = 3, command = lambda: boton(8))
boton8.place(x=117, y=340)

boton9 = Button(ventana, text="9", width = 9, height = 3, command = lambda: boton(9))

boton9.place(x=197, y=340)

botonAC = Button(ventana, text="AC", width = 9, height = 3, command = lambda: borrar())
botonAC.place(x=37, y=160)

boton0 = Button(ventana, text="0", width = 21, height = 3, command = lambda: boton(0))
boton0.place(x=37, y=400)

botonIgual = Button(ventana, text="=", width = 9, height = 7, command = lambda: operacion())
botonIgual.place(x=277 ,y=340)

botonSuma = Button(ventana, text="+", width = 9, height = 7, command = lambda: boton("+"))
botonSuma.place(x =277 ,y=220)

botonResta = Button(ventana, text="/", width = 9, height = 3, command = lambda: boton("-"))
botonResta.place(x=117, y=160)

botonX = Button(ventana, text="*", width = 9, height = 3, command = lambda: boton("*"))
botonX.place(x=197, y=160)

botonDiv = Button(ventana, text="-", width = 9, height = 3, command = lambda: boton("/"))
botonDiv.place(x=277, y=160)

botonPunto = Button(ventana, text=".", width = 9, height = 3, command = lambda: boton("."))
botonPunto.place(x=197, y=400)

#Manteniendo la ventana activa
ventana.mainloop()
