# -*- coding: utf-8 -*-
#! Comentario de error
#* Comentario de exito
#? Comentario de duda 
#^ Comentario de incompleto
#& Comentario de guia o ayuda
# Comentario normal

from random import *
import numpy as np
import csv # Libreria para lectura y escritura de csv
import os # Libreria para eliminar archivos

archivoClientes = 'clientes.csv'
archivoVentas = 'ventas.csv'
archivoInventario = 'inventario.csv'
archivoCapital = 'capital.csv'

capital = 4000

class Clientes:
    def __init__(self, idCliente, nombre, apellido, email):
        self.idCliente = idCliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return(f"Id: {self.idCliente}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email} ")
    
class Ventas:
    def __init__(self, idVenta, idClienteVenta, dineroGastado, nombrePizza, propina):
        self.idVenta = idVenta
        self.idClienteVenta = idClienteVenta
        self.dineroGastado = dineroGastado
        self.nombrePizza = nombrePizza
        self.propina = propina

    def __str__(self):
        return(f"Id venta: {self.idVenta}, Id cliente: {self.idClienteVenta}, Dinero gastado: {self.dineroGastado}, Nombre de la pizza: {self.nombrePizza}, Propina: {self.propina}")
    
def valor_numerico(opcion):
    while not opcion.isdigit():
        opcion=input("Usted no ingreso un numero\nIngrese un numero: ")
        if opcion.isdigit():
            return opcion
    return opcion
    
def leerArchivoClientes(archivoClientes):
    listaClientes = []
    with open(archivoClientes, 'r', newline = '', encoding = 'utf-8') as clientesCsv:
        lectorCsv = csv.reader(clientesCsv, delimiter = ';')
        next(lectorCsv)
        for fila in lectorCsv:
            id, nombre, apellido, email = fila
            cliente = Clientes(id, nombre, apellido, email)
            listaClientes.append(cliente)
    return listaClientes

def mostrar_ingrediente(archivo_inventario):
    with open(archivo_inventario) as archivo:
        contenido = csv.reader(archivo, delimiter = ';')
        buscador_ingr = input("Ingrese el ingrediente a buscar: ").lower()
        for linea in contenido:
            if linea[0].lower() == buscador_ingr:
                print("La cantidad de {} que queda es {}\n".format(buscador_ingr,linea[1]))
    archivo.close()

def leerArchivoVentas(archivoVentas):
    listaVentas = []
    with open(archivoVentas, 'r', newline = '', encoding = 'utf-8') as ventasCsv:
        lectorCsv2 = csv.reader(ventasCsv, delimiter = ';')
        next(lectorCsv2)
        for fila in lectorCsv2:
            idventa, idclienteventa, dinero, pizza, prop = fila
            venta = Ventas(idventa, idclienteventa, dinero, pizza, prop)
            listaVentas.append(venta)
    return listaVentas

listaVentas = leerArchivoVentas(archivoVentas)    
listaClientes = leerArchivoClientes(archivoClientes)

def buscarClientePorCorreo(listaClientes, email):
    for cliente in listaClientes:
        if cliente.email == email:
            return cliente
    return None
        
def encontrarUltimoIdClientes(archivoClientes):
    ultimo_id = None
    with open(archivoClientes, 'r', newline='', encoding='utf-8') as clientesCsv:
        lectorCsv = csv.reader(clientesCsv, delimiter=';')
        next(lectorCsv)  # Saltar la primera fila si contiene encabezados
        for fila in lectorCsv:
            id_cliente = int(fila[0])
            if ultimo_id is None or id_cliente > ultimo_id:
                ultimo_id = id_cliente
    return ultimo_id

def buscarVentaPorId(listaVentas, idVenta):
    for venta in listaVentas:
        if venta.idVenta == idVenta:
            return venta
    return None

def propinasTotales(listaVentas):
    contPropinas = 0
    for venta in listaVentas:
        contPropinas += float(venta.propina)
    return contPropinas

def gananciasTotales(listaVentas):
    contGanancia = 0
    for venta in listaVentas:
        contGanancia += float(venta.dineroGastado)
    return contGanancia

def gastoTotalCliente(listaVentas,archivoClientes, idClienteVenta):
    with open(archivoClientes,'r') as archivo:
        contenido = csv.reader(archivo,delimiter=';')
        datos = list(contenido)
        while int(idClienteVenta) > len(datos):
            print("id no encontrado")
            idClienteVenta = input("Ingrese el id del cliente a buscar:")
        for fila in datos:
            if idClienteVenta in fila:
                pos = fila[1]
                nombre = pos   
    contGasto = 0
    for venta in listaVentas:
        if idClienteVenta == venta.idClienteVenta:
            contGasto += float(venta.dineroGastado)        
    print("\n{} se ha gastado {} dolares en la pizzeria\n".format(nombre,contGasto))        

def pizzaNapolitana(archivoInventario, factura):
    elegir_tamaño = input("\nIngrese el tamaño de su Pizza Napolitana :)\n1-Tamaño personal (6.50$)\n2-Tamaño mediano (8$)\n3-Tamaño familiar (10$)\n")
    if elegir_tamaño == "1":
        factura += 6.50
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';') 
            datos = list(contenido)
            caja = "cajaPersonal"
            salsa = "salsa"
            queso = "mozzarella"
            masa = "masa"
            servilleta = "servilleta"
            for fila in datos:
                if queso in fila:
                    pos = int(fila[1])
                    pos -= 1
                    fila[1] = str(pos)
                if masa in fila:
                    pos1 = int(fila[1])
                    pos1 -= 1
                    fila[1] = str(pos1)
                if salsa in fila:
                    pos2 = int(fila[1])  
                    pos2 -= 1
                    fila[1] = str(pos2)
                if caja in fila:
                    pos3 = int(fila[1])      
                    pos3 -= 1
                    fila[1] = str(pos3)
                if servilleta in fila:
                    pos4 = int(fila[1])
                    pos4 -= 1
                    fila[1] = str(pos4)
                        
        with open(archivoInventario,'w', newline = '') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(datos)
        
    elif elegir_tamaño == "2":
        factura += 8
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';') 
            datos = list(contenido)
            caja = "cajaMediana"
            salsa = "salsa"
            queso = "mozzarella"
            masa = "masa"
            servilleta = "servilleta"
            for fila in datos:
                if queso in fila:
                    pos = int(fila[1])
                    pos -= 2
                    fila[1] = str(pos)
                if masa in fila:
                    pos1 = int(fila[1])
                    pos1 -= 2
                    fila[1] = str(pos1)
                if salsa in fila:
                    pos2 = int(fila[1])  
                    pos2 -= 2
                    fila[1] = str(pos2)
                if caja in fila:
                    pos3 = int(fila[1])      
                    pos3 -= 1
                    fila[1] = str(pos3)
                if servilleta in fila:
                    pos4 = int(fila[1])
                    pos4 -= 1
                    fila[1] = str(pos4)
        
        with open(archivoInventario,'w', newline = '') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(datos)    

    elif elegir_tamaño == "3":
        factura += 10
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';') 
            datos = list(contenido)
            caja = "cajaFamiliar"
            salsa = "salsa"
            queso = "mozzarella"
            masa = "masa"
            servilleta = "servilleta"
            for fila in datos:
                if queso in fila:
                    pos = int(fila[1])
                    pos -= 3
                    fila[1] = str(pos)
                if masa in fila:
                    pos1 = int(fila[1])
                    pos1 -= 3
                    fila[1] = str(pos1)
                if salsa in fila:
                    pos2 = int(fila[1])  
                    pos2 -= 3
                    fila[1] = str(pos2)
                if caja in fila:
                    pos3 = int(fila[1])      
                    pos3 -= 1
                    fila[1] = str(pos3)
                if servilleta in fila:
                    pos4 = int(fila[1])  
                    pos4 -= 1
                    fila[1] = str(pos4)  
            with open(archivoInventario,'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(datos)
    else:
        print("Elija una opcion valida")

    return factura

def pizzaPepperoni(archivoInventario, factura):
    elegir_tamaño = input("\nIngrese el tamaño de su Pizza Pepperoni :)\n1-Tamaño personal (7.50$)\n2-Tamaño mediano (9.50$)\n3-Tamaño familiar (12$)\n")
    if elegir_tamaño == "1":
        factura += 7.50
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';') 
            datos = list(contenido)
            caja = "cajaPersonal"
            salsa = "salsa"
            queso = "mozzarella"
            masa = "masa"
            servilleta = "servilleta"
            pepperoni = "pepperoni"
            for fila in datos:
                if queso in fila:
                    pos = int(fila[1])
                    pos -= 1
                    fila[1] = str(pos)
                if masa in fila:
                    pos1 = int(fila[1])
                    pos1 -= 1
                    fila[1] = str(pos1)
                if salsa in fila:
                    pos2 = int(fila[1])  
                    pos2 -= 1
                    fila[1] = str(pos2)
                if caja in fila:
                    pos3 = int(fila[1])      
                    pos3 -= 1
                    fila[1] = str(pos3)
                if servilleta in fila:
                    pos4 = int(fila[1])
                    pos4 -= 1
                    fila[1] = str(pos4) 
                if pepperoni in fila:
                    pos5 = int(fila[1])
                    pos5 -= 1
                    fila[1] = str(pos5)   
        with open(archivoInventario,'w', newline = '') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(datos)

    elif elegir_tamaño == "2":
        factura += 9.50
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';') 
            datos = list(contenido)
            caja = "cajaMediana"
            salsa = "salsa"
            queso = "mozzarella"
            masa = "masa"
            servilleta = "servilleta"
            pepperoni = "pepperoni"
            for fila in datos:
                if queso in fila:
                    pos = int(fila[1])
                    pos -= 2
                    fila[1] = str(pos)
                if masa in fila:
                    pos1 = int(fila[1])
                    pos1 -= 2
                    fila[1] = str(pos1)
                if salsa in fila:
                    pos2 = int(fila[1])  
                    pos2 -= 2
                    fila[1] = str(pos2)
                if caja in fila:
                    pos3 = int(fila[1])      
                    pos3 -= 1
                    fila[1] = str(pos3)
                if servilleta in fila:
                    pos4 = int(fila[1])
                    pos4 -= 1
                    fila[1] = str(pos4)
                if pepperoni in fila:
                    pos5 = int(fila[1])
                    pos5 -= 2
                    fila[1] = str(pos5)   
        with open(archivoInventario,'w', newline = '') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(datos)    

    elif elegir_tamaño == "3":
        factura += 12
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';') 
            datos = list(contenido)
            caja = "cajaFamiliar"
            salsa = "salsa"
            queso = "mozzarella"
            masa = "masa"
            servilleta = "servilleta"
            pepperoni = "pepperoni"
            for fila in datos:
                if queso in fila:
                    pos = int(fila[1])
                    pos -= 3
                    fila[1] = str(pos)
                if masa in fila:
                    pos1 = int(fila[1])
                    pos1 -= 3
                    fila[1] = str(pos1)
                if salsa in fila:
                    pos2 = int(fila[1])  
                    pos2 -= 3
                    fila[1] = str(pos2)
                if caja in fila:
                    pos3 = int(fila[1])      
                    pos3 -= 1
                    fila[1] = str(pos3)
                if servilleta in fila:
                    pos4 = int(fila[1])  
                    pos4 -= 1
                    fila[1] = str(pos4)
                if pepperoni in fila:
                    pos5 = int(fila[1])
                    pos5 -= 3
                    fila[1] = str(pos5)     
            with open(archivoInventario,'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(datos)
    else:
        print("Elija una opcion valida")
    return factura

def calzone(archivoInventario, factura):
    eleccion_ingrediente = input("Que ingrediente desea agregar a su calzone? ").lower()
    factura += 5.50
    with open(archivoInventario,'r') as archivo:
        contenido = csv.reader(archivo, delimiter = ';')
        datos = list(contenido)
        ingredientes = [linea[0] for linea in datos]
        while eleccion_ingrediente not in ingredientes:
            eleccion_ingrediente = input("Ingrediente no encontrado, ingrese uno valido: ")
        masa = "masa"
        salsa = "salsa"
        queso = "mozzarella"
        caja = "cajaPersonal"
        servilleta = "servilleta"
        # print(datos)
        for linea in datos:
            # print(linea)
            if eleccion_ingrediente in linea:
                pos = int(linea[1])
                pos -= 1
                linea[1] = str(pos)
                
            if masa in linea:
                pos1 = int(linea[1])
                pos1 -= 1
                linea[1] = str(pos1)
            if salsa in linea:
                pos2 = int(linea[1])
                pos2 -= 1
                linea[1] = str(pos2)
            if queso in linea:
                pos3 = int(linea[1])
                pos3 -= 1
                linea[1] = str(pos3)
            if caja in linea:
                pos4 = int(linea[1])
                pos4 -= 1
                linea[1] = str(pos4)
            if servilleta in linea:
                pos5 = int(linea[1])
                pos5 -= 1
                linea[1] = str(pos5)
               
    with open(archivoInventario, 'w', newline = '') as archivo:
        escritor = csv.writer(archivo, delimiter = ';')
        escritor.writerows(datos)
    return factura

def cuatroQuesos(archivoInventario, factura):
    elegir_tamaño = input("\nIngrese el tamaño de su pizza Cuatro Quesos\n1-Tamaño personal (8.50$)\n2-Tamaño mediano (11$)\n3-Tamaño familiar (13.50$)\n").lower()
    factura += 8.50
    if elegir_tamaño == "1":
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter=';')
            lista = list(contenido)
            caja_personal = "cajaPersonal"
            servilleta = "servilleta"
            masa = "masa"
            salsa = "salsa"
            mozzarella = "mozzarella"
            roquefort = "quesoRoquefort"
            rabiola = "quesoRabiola"
            pecorino = "quesoPecorino"
            for linea in lista:
                if caja_personal in linea:
                    pos = int(linea[1])
                    pos -= 1
                    linea[1] = str(pos)
                if servilleta in linea:
                    pos1 = int(linea[1])    
                    pos1 -= 1
                    linea[1] = str(pos1)
                if masa in linea:
                    pos2 = int(linea[1])
                    pos2 -= 1
                    linea[1] = str(pos2)    
                if salsa in linea:
                    pos3 = int(linea[1])
                    pos3 -= 1
                    linea[1] = str(pos3)    
                if mozzarella in linea:
                    pos4 = int(linea[1])
                    pos4 -= 1
                    linea[1] = str(pos4)    
                if roquefort in linea:
                    pos5 = int(linea[1])
                    pos5 -= 1
                    linea[1] = str(pos5)    
                if rabiola in linea:
                    pos6 = int(linea[1])
                    pos6 -= 1
                    linea[1] = str(pos6)    
                if pecorino in linea:
                    pos7 = int(linea[1])  
                    pos7 -= 1
                    linea[1] = str(pos7)  
        with open(archivoInventario, 'w', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(lista)
        
    elif elegir_tamaño == "2":
        factura += 11
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter=';')
            lista = list(contenido)
            caja_mediana = "cajaMediana"
            servilleta = "servilleta"
            masa = "masa"
            salsa = "salsa"
            mozzarella = "mozzarella"
            roquefort = "quesoRoquefort"
            rabiola = "quesoRabiola"
            pecorino = "quesoPecorino"
            for linea in lista:
                if caja_mediana in linea:
                    pos = int(linea[1])
                    pos -= 1
                    linea[1] = str(pos)
                if servilleta in linea:
                    pos1 = int(linea[1])    
                    pos1 -= 1
                    linea[1] = str(pos1)
                if masa in linea:
                    pos2 = int(linea[1])
                    pos2 -= 2
                    linea[1] = str(pos2)    
                if salsa in linea:
                    pos3 = int(linea[1])
                    pos3 -= 2
                    linea[1] = str(pos3)    
                if mozzarella in linea:
                    pos4 = int(linea[1])
                    pos4 -= 2
                    linea[1] = str(pos4)    
                if roquefort in linea:
                    pos5 = int(linea[1])
                    pos5 -= 2
                    linea[1] = str(pos5)    
                if rabiola in linea:
                    pos6 = int(linea[1])
                    pos6 -= 2
                    linea[1] = str(pos6)    
                if pecorino in linea:
                    pos7 = int(linea[1])  
                    pos7 -= 2
                    linea[1] = str(pos7)  
        with open(archivoInventario, 'w', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(lista)
    elif elegir_tamaño == "3":
        factura += 13.50
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';')
            lista = list(contenido)
            caja_familiar = "cajaFamiliar"
            servilleta = "servilleta"
            masa = "masa"
            salsa = "salsa"
            mozzarella = "mozzarella"
            roquefort = "quesoRoquefort"
            rabiola = "quesoRabiola"
            pecorino = "quesoPecorino"
            for linea in lista:
                if caja_familiar in linea:
                    pos = int(linea[1])
                    pos -= 1
                    linea[1] = str(pos)
                if servilleta in linea:
                    pos1 = int(linea[1])    
                    pos1 -= 1
                    linea[1] = str(pos1)
                if masa in linea:
                    pos2 = int(linea[1])
                    pos2 -= 3
                    linea[1] = str(pos2)    
                if salsa in linea:
                    pos3 = int(linea[1])
                    pos3 -= 3
                    linea[1] = str(pos3)    
                if mozzarella in linea:
                    pos4 = int(linea[1])
                    pos4 -= 3
                    linea[1] = str(pos4)    
                if roquefort in linea:
                    pos5 = int(linea[1])
                    pos5 -= 3
                    linea[1] = str(pos5)    
                if rabiola in linea:
                    pos6 = int(linea[1])
                    pos6 -= 3
                    linea[1] = str(pos6)    
                if pecorino in linea:
                    pos7 = int(linea[1])  
                    pos7 -= 3
                    linea[1] = str(pos7)  
        with open(archivoInventario, 'w', newline = '') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(lista)
    return factura

def bebidas(archivoInventario, factura):
    opcion_bebida = input("Que bebida desea agregar a su pedido?\n1.-Coca-Cola (2$)\n2.-Pepsi (2$)\n3.-Frescolita (2$)\n4.-7up (2$)\n5.-Finalizar pedido de bebidas\n")
    while opcion_bebida != "5":
        if opcion_bebida == "1":
            cantidad_bebidas = input("Ingrese el numero de Coca-Cola a pedir: ")
            verificar_cantidad_bebidas = valor_numerico(cantidad_bebidas)
            cantidad_bebidas_verificada = verificar_cantidad_bebidas
            contBebidas = int(cantidad_bebidas_verificada)
            with open(archivoInventario, 'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';')
                lista = list(contenido)
                bebida = "cocacola"
                for linea in lista:
                    if bebida in linea:
                        pos = int(linea[1])
                        pos -= contBebidas
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(lista)
            factura += 2*contBebidas
            opcion_bebida = "5"
        elif opcion_bebida == "2":
            cantidad_bebidas = input("Ingrese el numero de Pepsi a pedir: ")
            verificar_cantidad_bebidas = valor_numerico(cantidad_bebidas)
            cantidad_bebidas_verificada = verificar_cantidad_bebidas
            contBebidas = int(cantidad_bebidas_verificada)
            with open(archivoInventario, 'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';')
                lista = list(contenido)
                bebida = "pepsi"
                for linea in lista:
                    if bebida in linea:
                        pos = int(linea[1])
                        pos -= contBebidas
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(lista)
            factura += 2*contBebidas
            opcion_bebida = "5"
        elif opcion_bebida == "3":
            cantidad_bebidas = input("Ingrese el numero de Frescolita a pedir: ")
            verificar_cantidad_bebidas = valor_numerico(cantidad_bebidas)
            cantidad_bebidas_verificada = verificar_cantidad_bebidas
            contBebidas = int(cantidad_bebidas_verificada)
            with open(archivoInventario, 'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';')
                lista = list(contenido)
                bebida = "frescolita"
                for linea in lista:
                    if bebida in linea:
                        pos = int(linea[1])
                        pos -= contBebidas
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(lista)
            factura += 2*contBebidas
            opcion_bebida = "5"
        elif opcion_bebida == "4":
            cantidad_bebidas = input("Ingrese el numero de 7up a pedir: ")
            verificar_cantidad_bebidas = valor_numerico(cantidad_bebidas)
            cantidad_bebidas_verificada = verificar_cantidad_bebidas
            contBebidas = int(cantidad_bebidas_verificada)
            with open(archivoInventario, 'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';')
                lista = list(contenido)
                bebida = "7up"
                for linea in lista:
                    if bebida in linea:
                        pos = int(linea[1])
                        pos -= contBebidas
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(lista)
            factura += 2*contBebidas
            opcion_bebida = "5"
        else:
            opcion_bebida = input("Ingrese una opcion valida por favor...\n\n1.-Coca-Cola (2$)\n2.-Pepsi (2$)\n3.-Frescolita (2$)\n4.-7up (2$)\n5.-Finalizar pedido de bebidas\n")
    return factura

def postres(archivoInventario, factura):
    opcion_postre = input("Cual postre desea agregar a su pedido?\n1.-Quesillo (3.50$)\n2.-Torta de Chocolate (3.75$)\n3.-Pie de Limón (3.50$)\n4.-Torta Tres Leches (4$)\n5.-Finalizar pedido\n")
    verificar_opcion_postre = valor_numerico(opcion_postre)
    opcion_postre_verificada = verificar_opcion_postre
    while opcion_postre_verificada != "5":
        if opcion_postre_verificada == "1":
            cant_postre = input("Cuantos quesillos desea agregar a su orden? ")
            verificar_cant_postre = valor_numerico(cant_postre)
            cant_postre_verificada = verificar_cant_postre
            contPostre = int(cant_postre_verificada)
            with open(archivoInventario, 'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';')
                lista = list(contenido)
                postre = "quesillo"
                for linea in lista:
                    if postre in linea:
                        pos = int(linea[1])
                        pos -= contPostre
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(lista)
            factura += 3.50*contPostre
            opcion_postre_verificada = "5"

        elif opcion_postre_verificada == "2":
            cant_postre = input("Cuantos quesillos desea agregar a su orden? ")
            verificar_cant_postre = valor_numerico(cant_postre)
            cant_postre_verificada = verificar_cant_postre
            contPostre = int(cant_postre_verificada)
            with open(archivoInventario, 'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';')
                lista = list(contenido)
                postre = "tortaChocolate"
                for linea in lista:
                    if postre in linea:
                        pos = int(linea[1])
                        pos -= contPostre
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(lista)
            factura += 3.75*contPostre
            opcion_postre_verificada = "5"
        
        elif opcion_postre_verificada == "3":
            cant_postre = input("Cuantos quesillos desea agregar a su orden? ")
            verificar_cant_postre = valor_numerico(cant_postre)
            cant_postre_verificada = verificar_cant_postre
            contPostre = int(cant_postre_verificada)
            with open(archivoInventario, 'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';')
                lista = list(contenido)
                postre = "pieDeLimon"
                for linea in lista:
                    if postre in linea:
                        pos = int(linea[1])
                        pos -= contPostre
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(lista)
            factura += 3.50*contPostre
            opcion_postre_verificada = "5"

        elif opcion_postre_verificada == "4":
            cant_postre = input("Cuantos quesillos desea agregar a su orden? ")
            verificar_cant_postre = valor_numerico(cant_postre)
            cant_postre_verificada = verificar_cant_postre
            contPostre = int(cant_postre_verificada)
            with open(archivoInventario, 'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';')
                lista = list(contenido)
                postre = "tortaTresLeches"
                for linea in lista:
                    if postre in linea:
                        pos = int(linea[1])
                        pos -= contPostre
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(lista)
            factura += 4*contPostre
            opcion_postre_verificada = "5"

        else:
            opcion_postre_verificada = input("Opcion invalida...\n\nCual postre desea agregar a su pedido?\n1.-Quesillo (3.50$)\n2.-Torta de Chocolate (3.75$)\n3.-Pie de Limón (3.50$)\n4.-Torta Tres Leches (4$)\n5.-Finalizar pedido\n")
    return factura

def capitalActual(archivoCapital):
    with open(archivoCapital, 'r') as archivo:
        contenido = csv.reader(archivo,delimiter=';')
        lista = list(contenido)
        lista2 = list(lista[0])
        capital = lista2[1]
    print(f"El capital de la pizzeria es: {capital}")

def comprarIngredientes(archivoInventario):
    opcion = ""
    while opcion != "2":
        opcion = input("Que desea hacer?\n1-Comprar ingrediente\n2-Salir\n")
        if opcion == "1":
            eleccion_ingrediente = input("Ingrese el ingrediente a comprar: ")
            cantidad_a_comprar = int(input("\nIngrese la cantidad a comprar de ese ingrediente: "))
            with open(archivoInventario,'r') as archivo:
                contenido = csv.reader(archivo,delimiter=';')
                lista = list(contenido)
                for linea in lista:
                    if eleccion_ingrediente == linea[0]:
                        pos = int(linea[1])
                        pos += cantidad_a_comprar
                        linea[1] = str(pos)
            with open(archivoInventario, 'w', newline='') as archivo:
                lector = csv.writer(archivo,delimiter=';')   
                lector.writerows(lista)
        else:
            break                            
# prubaGastoCliente = input("Ingrese el id: ")
# prubaGastoCliente = input("Ingrese el id: ")
# pruebaGastoCliente = gastoTotalCliente(listaVentas, prubaGastoCliente)
# print(pruebaGastoCliente)


        
# for cliente in listaClientes: #& Estas dos lineas eran para comprobar el funcionamiento de la clase
#     print(cliente) #& Estas dos lineas eran para comprobar el funcionamiento de la clase

print("---BIENVENIDO A LA APP OFICIAL DE LA PIZZERIA---")
trabajador_cliente = input("Usted es un cliente o trabajador?\n1.-Cliente\n2.-Trabajador\n")
verificar_opcion = valor_numerico(trabajador_cliente)
opcion_trabajador_cliente = verificar_opcion

if opcion_trabajador_cliente == "1":
    opcion_cliente = input("Que desea hacer?\n1.-Realizar un pedido\n2.-Salir\n")
    verificar_opcion_cliente = valor_numerico(opcion_cliente)
    opcion_verificada_cliente = verificar_opcion_cliente
    while opcion_verificada_cliente != "2":
        if opcion_verificada_cliente == "1":
            esta_registrado = input("Usted ya esta registrado en nuestra app?\n1.-Si\n2.-No\n")
            verificar_esta_registrado = valor_numerico(esta_registrado)
            esta_registrado_verificado = verificar_esta_registrado
            if esta_registrado_verificado == "1":
                email = input("Ingrese su email por favor: ")
                verificarCliente = buscarClientePorCorreo(listaClientes, email)
                if verificarCliente:
                    opcion_pedido = input(f"Hola {verificarCliente.nombre}, cual es su pedido?\n1.-Pizza Napolitana\n2.-Pizza Pepperoni\n3.-Pizza Cuatro Quesos\n4.-Calzone (5.50$)\n5.-Finalizar pedido de pizzas\n")
                    factura = 0
                    while opcion_pedido != "5":
                        if opcion_pedido == "1":
                            factura = pizzaNapolitana(archivoInventario, factura)
                            opcion_pedido = input(f"Pizza agregada a su factura, el total a pagar es: {factura}$, desea agregar algun producto mas?\n1.-Pizza Napolitana\n2.-Pizza Pepperoni\n3.-Pizza Cuatro Quesos\n4.-Calzone (5.50$)\n5.-Finalizar pedido de pizzas\n")
                        elif opcion_pedido == "2":
                            factura = pizzaPepperoni(archivoInventario, factura)
                            opcion_pedido = input(f"Pizza agregada a su factura, el total a pagar es: {factura}$, desea agregar algun producto mas?\n1.-Pizza Napolitana\n2.-Pizza Pepperoni\n3.-Pizza Cuatro Quesos\n4.-Calzone (5.50$)\n5.-Finalizar pedido de pizzas\n")
                        elif opcion_pedido == "3":
                            factura = cuatroQuesos(archivoInventario, factura)
                            opcion_pedido = input(f"Pizza agregada a su factura, el total a pagar es: {factura}$, desea agregar algun producto mas?\n1.-Pizza Napolitana\n2.-Pizza Pepperoni\n3.-Pizza Cuatro Quesos\n4.-Calzone (5.50$)\n5.-Finalizar pedido de pizzas\n")
                        elif opcion_pedido == "4":
                            factura = calzone(archivoInventario, factura)
                            opcion_pedido = input(f"Calzone agregado a su factura, el total a pagar es: {factura}$, desea agregar algun producto mas?\n1.-Pizza Napolitana\n2.-Pizza Pepperoni\n3.-Pizza Cuatro Quesos\n4.-Calzone (5.50$)\n5.-Finalizar pedido de pizzas\n")
                        else:
                            opcion_pedido = input(f"Ingrese una opcion valida, el total a pagar es: {factura}$, desea agregar algun producto mas?\n1.-Pizza Napolitana\n2.-Pizza Pepperoni\n3.-Pizza Cuatro Quesos\n4.-Calzone (5.50$)\n5.-Finalizar pedido de pizzas\n")
                    quiere_bebida = input("Desea agregar una bebida a su pedido?\n1.-Si\n2.-No\n")
                    verificar_quiere_bebida = valor_numerico(quiere_bebida)
                    quiere_bebida_verificada = verificar_quiere_bebida
                    while quiere_bebida_verificada != "2":
                        if quiere_bebida_verificada == "1":
                            factura = bebidas(archivoInventario, factura)
                            quiere_bebida_verificada = input(f"Bebida agregada a su factura, el total a pagar es: {factura}$, desea agregar otra bebida?\n1.-Si\n2.-No\n")
                        else:
                            quiere_bebida_verificada = input("Ingrese una opcion valida...\n\nDesea agregar una bebida a su pedido?\n1.-Si\n2.-No\n")
                    quiere_postre = input("Desea agregar un postre a su pedido?\n1.-Si\n2.-No\n")
                    verificar_quiere_postre = valor_numerico(quiere_postre)
                    quiere_postre_verificada = verificar_quiere_postre
                    while quiere_postre_verificada != "2":
                        if quiere_postre_verificada == "1":
                            factura = postres(archivoInventario, factura)
                            quiere_postre_verificada = input(f"Postre agregado a su factura, el total a pagar es: {factura}$, desea agregar otro postre?\n1.-Si\n2.-No\n")
                        else:
                            quiere_postre_verificada = input("Ingrese una opcion valida...\n\nDesea agregar un postre a su pedido?\n1.-Si\n2.-No\n")
                    if factura == 0:
                        print("Usted no realizo ninguna compra, vayase pobre")
                        break
                    elif factura > 0:
                        print(f"El total a pagar es: {factura}$\n")
                        pago = input("Ya hizo el pago?\n1.-Si\n2.-No\n")
                        verificar_pago = valor_numerico(pago)
                        pago_verificado = verificar_pago
                        while pago_verificado != "1":
                            pago_verificado = input(f"\nPara continuar debe realizar el pago de {factura}$...\n\nYa hizo el pago?\n1.-Si\n2.-No\n")
                        print("Recibido, gracias por su compra, muy buen provecho ;)")
                        break
                else:
                    opcionRegistro = input("Correo no encontrado, desea registrarse?\n\n1.-Si\n2.-No\n")
                    verificar_opcion_registro = valor_numerico(opcionRegistro)
                    opcion_registro_verificada = verificar_opcion_registro
                    if opcion_registro_verificada == "1":
                        ultimoId = encontrarUltimoIdClientes(archivoClientes)
                        idNuevoUsuario = ultimoId + 1
                        nombreNuevoUsuario = input("Ingrese su nombre: ")
                        apellidoNuevoUsuario = input("Ingrese su apellido: ")
                        emailNuevoUsuario = input("Ingrese su email: ")
                        registroUsuario = open(archivoClientes, 'a')
                        registroUsuario.write(f"{idNuevoUsuario};{nombreNuevoUsuario};{apellidoNuevoUsuario};{emailNuevoUsuario}\n")
                        registroUsuario.close()
                        print("\nUsted se ha registrado exitosamente :)")
                        break
                    elif opcion_registro_verificada == "2":
                        print("Para poder realizar un pedido debe registrarse, hasta luego!!")
                        break
            elif esta_registrado_verificado == "2":
                registrarse = input("Para realizar un pedido en nuestra app debe registrarse, desea hacerlo?\n1.-Si\n2.-No\n")
                verificar_registrarse = valor_numerico(registrarse)
                registrarse_verificado = verificar_registrarse
                if registrarse_verificado == "1":
                    ultimoId = encontrarUltimoIdClientes(archivoClientes)
                    idNuevoUsuario = ultimoId + 1
                    nombreNuevoUsuario = input("Ingrese su nombre: ")
                    apellidoNuevoUsuario = input("Ingrese su apellido: ")
                    emailNuevoUsuario = input("Ingrese su email: ")
                    registroUsuario = open(archivoClientes, 'a')
                    registroUsuario.write(f"{idNuevoUsuario};{nombreNuevoUsuario};{apellidoNuevoUsuario};{emailNuevoUsuario}\n")
                    registroUsuario.close()
                    print("\nUsted se ha registrado exitosamente :)")
                    break
                elif registrarse_verificado == "2":
                    print("Lo sentimos, registrese para poder pedir en nuestra app")
                    break

        elif opcion_verificada_cliente == "2":
            print("Saliendo, gracias por preferirnos!!")

        else:
            print("Opcion invalida, ingrese nuevamente")
            opcion_verificada_cliente = input("Que desea hacer?\n1.-Realizar un pedido\n2.-Salir\n")

elif opcion_trabajador_cliente == "2":
    opcion_trabajador = input("Que desea hacer el dia de hoy?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar el nombre de un cliente y cuanto gasto\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Comprar ingredientes\n8.-Salir\n")
    opcion_trabajador_verificar = valor_numerico(opcion_trabajador)
    opcion_trabajador_verificada = opcion_trabajador_verificar
    while opcion_trabajador_verificada != "8":
        if opcion_trabajador_verificada == "1":
            capitalActual(archivoCapital)
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar el nombre de un cliente y cuanto gasto\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Comprar ingredientes\n8.-Salir\n")
        
        elif opcion_trabajador_verificada == "2":
            id_buscar_gasto = input("Ingrese el Id del cliente para buscar su gasto total: ")
            id_buscar_gasto_verificar = valor_numerico(id_buscar_gasto)
            id_buscar_gasto_verificada = id_buscar_gasto_verificar
            gastoTotalCliente(listaVentas, archivoClientes,id_buscar_gasto_verificada)
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Comprar ingredientes\n8.-Salir\n")

        elif opcion_trabajador_verificada == "3":
            mostrar_ingrediente("inventario.csv")
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Comprar ingredientes\n8.-Salir\n")

        elif opcion_trabajador_verificada == "4":
            print("Funcion aun no implementada")
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Comprar ingredientes\n8.-Salir\n")

        elif opcion_trabajador_verificada == "5":
            totalPropinas = propinasTotales(listaVentas)
            print("\nEl total de propinas es: {:.2f}\n".format(totalPropinas))
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Comprar ingredientes\n8.-Salir\n")

        elif opcion_trabajador_verificada == "6":
            totalGanancias = gananciasTotales(listaVentas)
            print("\nEl total de ganancias obtenidas en las ventas es de: {:.2f}\n".format(totalGanancias))
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Comprar ingredientes\n8.-Salir\n")

        elif opcion_trabajador_verificada == "7":
            comprarIngredientes(archivoInventario)
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Comprar ingredientes\n8.-Salir\n")

        elif opcion_trabajador_verificada == "8":
            print("Saliendo, hasta la proxima!!")

        else:
            print("Ingrese una opcion valida")
            opcion_trabajador_verificada = input("Que desea hacer el dia de hoy?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")

else:
    print("Ingrese una opcion valida por favor\n")
print("Gracias por visitar la app de nuestra pizzeria, vuelve pronto :)")
# for fila in listaClientes:
#     print(', '.join(fila))