import random
tuplita = ([], [], [], [],[], [], [], [],[], [], [], [])
mostrarLista = list(tuplita)
contadorsin = 0

def registrar():
    global contadorsin
    global mostrarLista
    print("======================================")
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    telefono = int(input("telefono: "))
    direccion = input("direccion: ")
    mostrarLista[0].append(nombre)
    mostrarLista[1].append(apellido)
    mostrarLista[2].append(telefono)
    mostrarLista[3].append(direccion)
    print("paquetes ofimaticos\n")
    print("1. pc + monitor: 500\n2. pc + monitor4k: 2000\n3. laptop pro IA: 1500\n4. servidor potente: 3000")
    opcionTecnologia = int(input("opcion: "))
    if opcionTecnologia == 1:
        mostrarLista[4].append(500)
        mostrarLista[5].append((500*0.15)+500)
    elif opcionTecnologia == 2:
         mostrarLista[4].append(2000)
         mostrarLista[5].append((2000*0.15)+2000)
    elif opcionTecnologia == 3:
        mostrarLista[4].append(1500)
        mostrarLista[5].append((1500*0.15)+1500)
    elif opcionTecnologia == 4:
         mostrarLista[4].append(3000)
         mostrarLista[5].append((3000*0.15)+3000)
    mostrarLista[6].append(random.randint(1,1000))
    contadorsin=contadorsin+1
    print("======================================\ngracias\n")


def mostrar():
    global contadorsin
    if contadorsin == 0:
        print("no hay registros")
    else:
        print("======================================")
        print("nombres: ",mostrarLista[0])
        print("apellidos: ",mostrarLista[1])
        print("telefonos: ",mostrarLista[2])
        print("direcciones: ",mostrarLista[3])
        print("pagos: ",mostrarLista[4])
        print("pagos(IVA): ",mostrarLista[5])
        print("codigo unico: ", mostrarLista[6])
        print("======================================")

def detalles():
    print("======================================")
    codigo = int(input("codigo unico: "))
    if codigo in mostrarLista[6]:
        codigoBusqueta = mostrarLista[6].index(codigo)
        print("nombres: ",mostrarLista[0][codigoBusqueta])
        print("apellidos: ",mostrarLista[1][codigoBusqueta])
        print("telefonos: ",mostrarLista[2][codigoBusqueta])
        print("direcciones: ",mostrarLista[3][codigoBusqueta])
        print("pagos: ",mostrarLista[4][codigoBusqueta])
        print("pagos(IVA): ",mostrarLista[5][codigoBusqueta])
        print("codigo unico: ", mostrarLista[6][codigoBusqueta])
    else:
        print("no existe ese codigo\n")
    print("======================================")

def borrar():
    print("======================================")
    codigo = int(input("codigo unico: "))
    if codigo in mostrarLista[6]:
        codigoBusqueta = mostrarLista[6].index(codigo)
        for i in range(7):
            mostrarLista[i].pop(codigoBusqueta)
            print("borrado")
    else:
        print("no existe ese codigo\n")
    print("======================================")
#==================MAIN======================
opcion = int(input("1.registrar\n2.mostrar\n3.detalle de un pedido\n4.eliminar\n5.salir\nopcion: "))
while(opcion != 5):
    if(opcion == 1):
        registrar()
        opcion = int(input("1.registrar\n2.mostrar\n3.detalle de un pedido\n4.eliminar\n5.salir\nopcion: "))
    elif(opcion == 2):
        mostrar()
        opcion = int(input("1.registrar\n2.mostrar\n3.detalle de un pedido\n4.eliminar\n5.salir\nopcion: "))
    elif(opcion == 3):
        detalles()
        opcion = int(input("1.registrar\n2.mostrar\n3.detalle de un pedido\n4.eliminar\n5.salir\nopcion: "))
    elif(opcion == 4):
        borrar()
        opcion = int(input("1.registrar\n2.mostrar\n3.detalle de un pedido\n4.eliminar\n5.salir\nopcion: "))
    else:
        print("Incorrecto, intenta de nuevo")
        break
print("Gracias e.e")