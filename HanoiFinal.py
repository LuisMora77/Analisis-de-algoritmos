from tkinter import *
from time import time #importamos la función time para capturar tiempos
from tkinter import messagebox
from math import *
import string
from tkinter import font
from random import randint
from time import time

tiempo_inicial = time()
contador = 1
tiempoTotalApp = 0

def creartxt():
        archi=open('hanoi.txt','w')
        archi.close()
    
def grabartxt(n):
        archi=open('hanoi.txt','a')
        archi.write(n+'\n')
        archi.close()


def hanoi(n, com, aux, fin, num):
    global contador
    if(n == 1):
        grabartxt(('Mueve de torre '+com + ' hacia torre '+ fin))
        print(com,'->',fin)
    else:
        hanoi(n-1,com,fin,aux,num)
        contador = contador + 1
        grabartxt(('Mueve de torre '+com + ' hacia torre '+ fin))
        print(com, '->',fin)
        hanoi(n-1,aux,com,fin,num+1)
        contador = contador + 1

                
    
def mostrar(t):
    total = t
    resultado =  StringVar()
    resultado.set(contador)
    limpiador = StringVar()
    limpiador.set("           ")
    #numero.destroy()
    numero = Label(app, text = "",bg="green", font = myFont, textvariable = limpiador)
    numero.pack()
    numero.place(x = 110,y = 210)
    numero = Label(app, text = "",bg="green", font = myFont, textvariable = resultado)
    numero.pack()
    numero.place(x = 110,y = 210)
    messagebox.showinfo("Éxito","Tiempo total del programa: " + str(total) + " segundos")



    
def calcularHanoiAux(n):
    creartxt()
    grabartxt('La cantidad de discos seleccionada: ' + n + '\n')
    global contador
    contador = 1
    try:
        n = float(n)
        n = floor(n)
        if n <= 0:
             messagebox.showerror("Error","Debe escribir un número válido")
        else:
            tiempoI1 = time()
            com = "A"
            aux = "B"
            fin = "C"
            num = 1
            hanoi(n,com,aux,fin,num)
            tiempoF1 = time()
            tiempoT1 = tiempoF1 - tiempoI1
            print("Tiempo","El tiempo total de ejecución fue de: " , tiempoT1, " segundos")
            print("\nLa cantidad de movimientos es: ", contador)
            grabartxt('\nLa cantidad de movimientos es: ' + str(contador))
            grabartxt('\nEl tiempo total de ejecución fue de: ' +str(tiempoT1)+' segundos')
            mostrar(tiempoT1)
    except:
            messagebox.showerror("Error","Debe escribir un número válido")
    


app = Tk()
app.title("Torres de Hanoi")
app.geometry("300x300")
app.configure(background = '#419873')
background_image=PhotoImage(file="../PHanoi/green.png")
background_label =Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
titulo = Label(app, text = "Torres de Hanoi",bg="green",font=("courier",20))
titulo.pack()

myFont = font.Font(family="Helvetica", size=20, weight="bold")


cantidad = Label(app, text = "Cantidad de discos deseados: ",bg="green",font=("courier",10))
cantidad.pack()
cantidad.place(x = 33,y = 50)

cantTorres = Entry(app,width = 18,bd=5,justify='center')
cantTorres.pack()
cantTorres.place(x = 90, y = 80)

llamarHanio = Button(app, text="Calcular Jugadas", command = lambda: calcularHanoiAux(cantTorres.get()), width = 15 ) 
llamarHanio.pack()
llamarHanio.place(x = 93, y= 110)

labelCantFinal = Label(app, text = "Cantidad total de pasos: ",bg="green",font=("courier",13) )
labelCantFinal.pack()
labelCantFinal.place(x = 25,y = 150)






