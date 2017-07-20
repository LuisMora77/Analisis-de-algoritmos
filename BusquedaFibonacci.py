from tkinter import *
from time import time #importamos la función time para capturar tiempos
from random import choice
from string import ascii_uppercase
from string import digits
from tkinter import messagebox
from math import *  

arrayIni = []
llaves = []
archivos = []
tiempo1f = time()


def fiboSearch_AUX(array,elemento,tamano,fibo_Mayor,fibo_Men1,fibo_Men2,offsetA):
    fibMayor = fibo_Mayor  #numero fibonacci m
    fibMenor1 = fibo_Men1  #numero fibonacci m-1
    fibMenor2 = fibo_Men2  #numero fibonacci m-2
    offset = offsetA       #pivote de comparacion
    print("|FibMayor "+str(fibMayor)+" |FibMenor1 "+str(fibMenor1)+" |FibMenor2 "+str(fibMenor2)+" |Offset "+str(offset))
    if(fibMayor > 1):
        posicion = min(offset+fibMenor2,tamano-1)#Verifica si la posicion es valida
        if(array[posicion] < elemento):   #Si el elemento es mayor al de la posicion evaluada
            fibMayor = fibMenor1          #los numeros de fibonacci bajan un valor 
            fibMenor1 = fibMenor2
            fibMenor2 = fibMayor - fibMenor1
            return fiboSearch_AUX(array,elemento,tamano,fibMayor,fibMenor1,fibMenor2,posicion)
        elif(array[posicion] > elemento): #Si el elemento es menor al de la posicion evaluada
            fibMayor = fibMenor2          #los numeros de fibonacci bajan dos valores 
            fibMenor1 = fibMenor1 - fibMenor2
            fibMenor2 = fibMayor - fibMenor1
            return fiboSearch_AUX(array,elemento,tamano,fibMayor,fibMenor1,fibMenor2,offset) 
        else:
            return posicion               #Si el elemento es igual al de la posicion evaluada devuelve su posicion 
    elif((fibMenor1 and (offset+1 > tamano)) and (array[offset+1] == 0)):
        return offset+1  #compara la ultima posicion si es igual al elemento devuelve la posicion
    else:
        return -1        #si llega hasta el final y no encuentra ningun elemento igual retorna -1
    

def fiboSearch(tamano, arrayDatos, elemento):
    tama = tamano  #tamano del array
    fib_Men2 = 0   # Numero fibonacci m-2.
    fib_Men1 = 1   # Numero fibonacci m-1.
    fib_Mayor = fib_Men2 + fib_Men1  #Numero fibonaci m.
    while (fib_Mayor < tama):        #Calcula fibonacci mayor o igual al tamano
        fib_Men2 = fib_Men1
        fib_Men1 = fib_Mayor
        fib_Mayor  = fib_Men2 + fib_Men1  
    return fiboSearch_AUX(arrayDatos,elemento,tama,fib_Mayor,fib_Men1,fib_Men2,-1)#se inicia con -1 el offset

def principal(llave):
    global arrayIni
    global llaves
    try:
        tiempoInicial = time()
        elementos = llaves
        if elementos != []:
            tamaArray = len(elementos)
            elementos.sort()
            print(elementos)
            elementoBusqueda = llave
            #Aqui llama a la funcion fiboSearch
            result = fiboSearch(tamaArray,elementos,elementoBusqueda)
            tiempoFinal= time()
            tiempoTotal = tiempoFinal - tiempoInicial
            if(result != -1):
                messagebox.showinfo("Resultado","Elemento "+elementoBusqueda+" encontrado en posicion "+str(result) + "\n" + "Tiempo total de ejecucion:" + str(tiempoTotal))
                print("Success","Elemento "+elementoBusqueda+" encontrado en posicion "+str(result) )
            else:
                messagebox.showinfo("Resultado","Elemento no encontrado")
                print("Elemento no encontrado")
        else:
            messagebox.showerror("Error","El array debe tener mínimo 1 elemento y debe ingresar una llave")
    except:
        messagebox.showerror("Error","El array debe tener mínimo 1 elemento")


    
def LlenarArray(n): #Llena el array con elementos alfanuméricos
    global arrayIni
    global llaves
    try:
        arrayIni = []
        tiempoInicial2 = time()
        if  1 <= n <= 500:
            for i in range(n):
                   elemento = (''.join(choice(ascii_uppercase + digits)for i in range(6)))
                   arrayIni.append(elemento)
            print(arrayIni)
            llaves = arrayIni
            tiempoFinal2 = time()
            tiempoEjecucion2 = tiempoFinal2 - tiempoInicial2
            print ('El tiempo de ejecucion fue:',tiempoEjecucion2)#En segundos
            messagebox.showinfo("Éxito","Los datos se han cargado con éxito")
        else:
            messagebox.showerror("Error","Debe escribir un número válido (int), entre 1 y 500")
    except:
        messagebox.showerror("Error","Debe escribir un número válido (int), entre 1 y 500")

def LlenarArrayAux(n):
    try:
        n = float(n)
        n = floor(n)
        if n <= 0:
             messagebox.showerror("Error","Debe escribir un número válido (int), entre 1 y 500")
        else:
            return LlenarArray(n)
    except:
        messagebox.showerror("Error","Debe escribir un número válido (int), entre 1 y 500")
        


def leerArchivo(nombre):
    global arrayIni
    global llaves
    try:
        arrayIni = []
        llaves = []
        archivo = open(nombre,"r")
        contenido = archivo.read()
        arrayIni = (contenido.split(","))
        archivo.close()
        llaves = arrayIni
        print(llaves)
        messagebox.showinfo("Éxito","Los datos se han leído con éxito")
    except:
        messagebox.showerror("Error","Debe escribir un nombre válido para el archivo que desea abrir")

def creartxt(n):
    try:
        n = float(n)
        n = floor(n)
        if n <= 0:
             messagebox.showerror("Error","Debe escribir un número válido (int), entre 1 y 500")
        else:
            archi=open('datos.txt','w')
            archi.close()
            return grabartxt(n)
    except:
        messagebox.showerror("Error","Debe escribir un número válido (int), entre 1 y 500")
    

def grabartxt(n):
    global archivos
    archivos = []
    archi=open('datos.txt','a')
    for i in range(n):
        elemento = (''.join(choice(ascii_uppercase + digits)for i in range(6)))
        archivos.append(elemento)
    for i in range(len(archivos)):
        archi.writelines(archivos[i])
        if i != (len(archivos)-1):
            archi.write(',')
    archi.close()
    messagebox.showinfo("Éxito","Se ha creado el archivo datos.txt con éxito")


def mostrar():
    resultado =  StringVar()
    resultado.set("Elemento "+elementoBusqueda+" encontrado en posicion "+str(result))
    limpiador = StringVar()
    limpiador.set("                     ")
    #numero.destroy()
    numero = Label(app, text = "",bg="#419873", textvariable = limpiador)
    numero.pack()
    numero.place(x = 200,y = 240)
    numero = Label(app, text = "",bg="#419873", font = myFont, textvariable = resultado)
    numero.pack()
    numero.place(x = 200,y = 240)
    messagebox.showinfo("Éxito","El programa se ha ejecutado con éxito")


#___________________________ Interfaz __________________________________________
tiempo1 = time()
app = Tk()
app.title("Búsqueda de Fibonacci")
app.geometry("450x300")
#app.configure(background = '#419873')
background_image=PhotoImage(file="../fPython/fibo.png")
background_label =Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
titulo = Label(app, text = "Búsqueda de fibonacci", bg = "cadet blue",font =("courier",20))
titulo.pack()



#_______Leer desde archivo_______________
nomArchivo= Label(app, text="Nombre del archivo   ", bg="royal blue",font =("Helvetica",9))
nomArchivo.pack()
nomArchivo.place(x = 50, y = 50)

nombreArchivo = Entry(app,width = 18,bd=5)
nombreArchivo.pack()
nombreArchivo.place(x = 50, y = 72)

abrirArchivo = Button(app, text="Abrir archivo .txt", command = lambda: leerArchivo(nombreArchivo.get()), width = 16,height = 2,font =("Helvetica",9)) 
abrirArchivo.pack()
abrirArchivo.place(x = 50, y= 100)

#____________________________________

#_______Crear lista aleatoria______________
cantElementos= Label(app, text="Cantidad de elementos  ",bg="steel blue")
cantElementos.pack()
cantElementos.place(x = 260, y = 50)

largoArray = Entry(app,width = 20,bd=5)
largoArray.pack()
largoArray.place(x = 261, y = 72)

crearArray = Button(app, text="Crear array aleatorio", command = lambda: LlenarArrayAux(largoArray.get()), width = 18,height = 2,font =("Helvetica",9)) 
crearArray.pack()
crearArray.place(x = 260, y= 100)

#____________________________________

#______ Búsequeda de fibonacci_____________
labelFibo= Label(app, text="       Llave a buscar           ",bg="steel blue")
labelFibo.pack()
labelFibo.place(x = 260, y = 160) #260 160

nombreLlave = Entry(app,width = 20,bd=5)#260 180
nombreLlave.pack()
nombreLlave.place(x = 260, y = 180)#261 208

busqueda = Button(app, text="Realizar búsqueda", command = lambda: principal(nombreLlave.get()), width = 17,height = 2,font =("Helvetica",9) ) 
busqueda.pack()
busqueda.place(x = 262, y= 208)

tiempo1t= tiempo1f - tiempo1 # tiempo que tarda en ejecutar la creación de la interfaz
print("Tiempo tardado en crear la interfaz: ", tiempo1t )
#_________________________________________________________________________

#___________________Crear Archivo _________________________

labelarch= Label(app, text="Cantidad de elementos",bg="royal blue")
labelarch.pack()
labelarch.place(x = 50, y = 160)

nombreNArch = Entry(app,width = 19,bd=5)
nombreNArch.pack()
nombreNArch.place(x = 50, y = 180)

creacion = Button(app, text="Crear Archivo.txt", command = lambda: creartxt(nombreNArch.get()), width = 17,height = 2 ) 
creacion.pack()
creacion.place(x = 50, y= 208)
#_____________________________________________________________

