from random import randint
from time import time
from tkinter import *
from tkinter import font
import string
from tkinter import messagebox
from math import *
from math import sqrt


t_inicial = time()


##def mostrar(n):
##    resultado =  StringVar()
##    resultado.set(n)
##    limpiador = StringVar()
##    limpiador.set("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            \n")
##    labelMatrizReultado = Label(app, text = ". ",bg="#419873", fg = "lightgreen",textvariable = limpiador )
##    labelMatrizReultado.pack()
##    labelMatrizReultado.place(x = 0,y = 170)
##    labelMatrizReultado = Label(app, text = ". ",bg="#419873", fg = "lightgreen",textvariable = resultado )
##    labelMatrizReultado.pack()
##    labelMatrizReultado.place(x = 0,y = 170)

def creartxt():
        archi=open('resultado.txt','w')
        archi.close()
    
def grabartxt(n):
        archi=open('resultado.txt','a')
        archi.write(str(n))
        archi.close()



def matrizManual(n):
    creartxt()
    try:
        n = float(n)
        n = floor(n)
        if n <= 0:
             messagebox.showerror("Error","Debe escribir un número válido")
        else:
            t_inicial2 = time()
            m1 = []
            m2 = []
            resultado = []
            aux = 0

            filas = n
            columnas = filas

            for i in range(filas):
                m1.append([])
                m2.append([])
                resultado.append([])

            for i in range(filas):
                for j in range(columnas):
                    numInsert = randint(2,2**1024) / randint(2,2**1024)
                    m1[j].append(numInsert)
                    
            for i in range(filas):
                for j in range(columnas):
                    numInsert = randint(2,2**1024) / randint(2,2**1024)
                    m2[j].append(numInsert)
            for i in range(filas):
                for j in range(columnas):
                    for k in range(columnas):
                        aux = aux + m1[i][k]*m2[k][j]
                        
                    resultado[i].append(aux)
            
            

            print("Matriz Resultante:\n")
            for i in range(filas):
               print(resultado[i])
               grabartxt((resultado[i]))
            print(resultado)
            
            t_final2= time()
            print("\ntiempesirijillo", t_final2-t_inicial2)
            mostrar2((t_final2-t_inicial2))
            messagebox.showinfo("success","Matriz resultado guardada en resultado.txt")    
    except:
         messagebox.showerror("Error","Debe escribir un número válido")

#------------------------------------Desde Archivos-----------------------------------------------


def matrizAuto(m1,m2):
        creartxt()
        try:
            tIni= time()
            archivo1 = open(m1,"r")
            archivo2 = open(m2,"r")
            temp1 = archivo1.read()  
            temp1 = temp1.split(",")
            temp2 = archivo2.read()  
            temp2 = temp2.split(",")
            for i in range(len(temp1)):
                temp1[i] = float(temp1[i])
                temp2[i] = float(temp2[i])
            archivo2.close()
            archivo1.close()
            m1 = []
            m2 = []
            resultado = []
            aux = 0
            pos = 0

            filas = round(sqrt(len(temp1)))
            columnas = filas
            for i in range(filas):
                m1.append([])
                m2.append([])
                resultado.append([])
            for i in range(filas):
                for j in range(columnas):
                    m1[j].append(temp1[pos])
                    m2[j].append(temp2[pos])
                    pos = pos+1
            for i in range(filas):
                for j in range(columnas):
                    for k in range(columnas):
                        aux = aux + m1[i][k]*m2[k][j]
                    resultado[i].append(aux)
            print("Matriz Resultante:\n")
            for i in range(filas):
               print(resultado[i])
               grabartxt((resultado[i]))
    
            tFin = time()
            mostrar2(tFin-tIni)
            messagebox.showinfo("success","Matriz resultado guardada en resultado.txt")    
        except:
                messagebox.showerror("Error","Debe escribir un nombre válido y verificar que ingreso ambos archivos")
                


t_final= time()
print("tiempesirijillo", t_final-t_inicial)

#____________________ Interfaz___________________________

app = Tk()
app.title("Multiplicación de matrices")
app.geometry("500x300")
app.configure(background = '#419873')
background_image=PhotoImage(file="../PMatriz/yellow.png")
background_label =Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def mostrar2(t):
    labelCantFinal = Label(app, text = "Tiempo de ejecución: "+str(t)+"s",bg="yellow", font = myFont, fg = "orange" )
    labelCantFinal.pack()
    labelCantFinal.place(x = 50, y = 240)

myFont = font.Font(family="Helvetica", size=15, weight="bold")
myFont2 = font.Font(family="Helvetica", size=15, weight="bold")
myFont3 = font.Font(family="Helvetica", size=10)

titulo = Label(app, text = "Multiplicación de matrices ",bg="yellow", font = myFont2, fg ="orange")
titulo.pack()

cantidad = Label(app, text = "Tamaño de las matrices deseadas: ",bg="yellow", font = myFont3, fg ="orange")
cantidad.pack()
cantidad.place(x = 20,y = 50)

cantidad = Label(app, text = "Desde archivos",bg="yellow", font = myFont2, fg ="orange")
cantidad.pack()
cantidad.place(x = 170,y = 90)

cantidad = Label(app, text = "Archivo matriz 1: ",bg="yellow", font = myFont3, fg ="orange")
cantidad.pack()
cantidad.place(x = 20,y = 140)

arch1 = Entry(app,width = 18)
arch1.pack()
arch1.place(x = 130, y = 140)

cantidad = Label(app, text = "Archivo matriz 2: ",bg="yellow", font = myFont3, fg ="orange")
cantidad.pack()
cantidad.place(x = 250,y = 140)

arch2 = Entry(app,width = 18)
arch2.pack()
arch2.place(x = 360, y = 140)

tamaMatriz = Entry(app,width = 18)
tamaMatriz.pack()
tamaMatriz.place(x = 240, y = 50)

llamarHanio2 =Button(app, text="Multiplicar Matrices ", command = lambda: matrizAuto(arch1.get(),arch2.get()), width = 15 ) 
llamarHanio2.pack()
llamarHanio2.place(x = 190, y= 190)

llamarHanio = Button(app, text="Multiplicar Matrices", command = lambda: matrizManual(tamaMatriz.get()), width = 15 ) 
llamarHanio.pack()
llamarHanio.place(x = 370, y= 45)



#419873
    
