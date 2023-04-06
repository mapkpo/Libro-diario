#PROGRAMA CONTABLE V1.15
#MIJAIL POTINSKI 19/1/2021

import os
from datetime import datetime
close = False

def fecha():
    #toma la fecha del sistema
    now = datetime.today()
    fecha = now.strftime("%d-%m-%Y")
    return(fecha)

def fecha1():
    #toma la fecha del sistema
    now = datetime.today()
    fecha = now.strftime("%Y/%m")
    return(fecha)    

def presentacion():
    #presenta el programa y dice la fecha
    print("Programa de libro diario Mercería la nueva")
    print("------------------------------------------")
    print("Día",fecha())

def creararchivo():
    #en caso de ser un libro nuevo se encarga de crear el libro
    archivo = open(nombrelibro,"a+")

def nombrelibro():
    #formatea el nombre del libro
    nombre = "C:/Libros/" + fecha1() + "/Libro dia " + fecha() + ".txt"
    return nombre
    
def añadir():
    #añade los montos al libro y chequea que sean números
    solosumarsimple()
    escribir = open(nombrelibro(),"a")
    valor = input("Monto nuevo: ")

    if valor == "sumar" or valor =="SUMAR":
        solosumar()

    if valor == "cerrar" or valor == "CERRAR":
        close = True
        sumar()
        
    else:               
        escribir.write(",")
        escribir.write("\n")
        escribir.write(valor)
        escribir.write(",")
        escribir.write("\n") 
    
def inicio():
    #chequea si existe un libro del dia y sino llama a la función para crear uno
    try:
        f = open(nombrelibro(),"a+")   
    except IOError:
        print("Archivo nuevo, creando archivo")
        creararchivo()
    finally:
        añadir()

def sumar():
    #suma los valores del libro 
    suma = 0
    sumartodo = open(nombrelibro(),"r")  

    lineavacia = False
    cantidad = 0
    retiros = 0
    while lineavacia == False:
        a = sumartodo.readline()
        if a == "":
            lineavacia = True

        elif (any(char.isdigit() for char in a)) == True:

            if a.startswith("*"):
                suma = suma
            
            elif a.startswith("-"):
                retiros = retiros + 1
                b = int ( ''.join(filter(str.isdigit, a) ) )
                suma = suma - b
            
            else:                
                cantidad = cantidad + 1
                b = int ( ''.join(filter(str.isdigit, a) ) )
                suma = suma + b                

    sumartodo.close()
    guardar = open(nombrelibro(),"a")
    suma1 = str(suma)
    cantidadstr = str(cantidad)
    retirosstr = str(retiros)
    guardar.write("\n")
    guardar.write("*El monto total fue de: " + suma1 + " pesos, con: " + cantidadstr + " ventas y "+ retirosstr
    +" retiros\n")
    guardar.write("*El dia: " + fecha())
    guardar.close()
    print("El monto total fue de: " + suma1 + " pesos, con: " + cantidadstr + " ventas y "+ retirosstr
    +" retiros")
    input("Ya puede cerrar esta ventana")
    exit()

def solosumar():
    solosuma = 0
    solosumartodo = open(nombrelibro(),"r")

    sololineavacia = False
    solocantidad = 0
    soloretiros = 0
    while sololineavacia == False:
        a = solosumartodo.readline()
        if a == "":
            sololineavacia = True

        elif (any(char.isdigit() for char in a)) == True:

            if a.startswith("*"):
                solosuma = solosuma
            
            if a.startswith("-"):
                soloretiros = soloretiros + 1
                b = int ( ''.join(filter(str.isdigit, a) ) )
                solosuma = solosuma - b
            
            else:
                solocantidad = solocantidad + 1
                b = int ( ''.join(filter(str.isdigit, a) ) )
                solosuma = solosuma + b
    
    solosumartodo.close()
    solosuma1 = str(solosuma)
    solocantidadstr = str(solocantidad)
    soloretirosstr = str(soloretiros) 

    print ("Monto de venta hasta el momento: " + solosuma1 + " pesos, con: " + solocantidadstr + " ventas y " + soloretirosstr + " retiros.")
    añadir()

def solosumarsimple():
    solosuma = 0
    solosumartodo = open(nombrelibro(),"r")

    sololineavacia = False
    solocantidad = 0
    soloretiros = 0
    while sololineavacia == False:
        a = solosumartodo.readline()
        if a == "":
            sololineavacia = True

        elif (any(char.isdigit() for char in a)) == True:

            if a.startswith("*"):
                solosuma = solosuma
            
            if a.startswith("-"):
                soloretiros = soloretiros + 1
                b = int ( ''.join(filter(str.isdigit, a) ) )
                solosuma = solosuma - b
            
            else:
                solocantidad = solocantidad + 1
                b = int ( ''.join(filter(str.isdigit, a) ) )
                solosuma = solosuma + b
    
    solosumartodo.close()
    solosuma1 = str(solosuma)
 

    print ("Monto actual: " + solosuma1 + " pesos")


#código principal >>>>>

newpath = ("C:/Libros/" + fecha1())
if not os.path.exists(newpath):
    os.makedirs(newpath)

presentacion()
inicio()

while close == False:
    añadir()