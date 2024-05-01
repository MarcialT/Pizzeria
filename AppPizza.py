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

capital = 0

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

def buscarClientePorId(listaClientes, idCliente):
    for cliente in listaClientes:
        if cliente.idCliente == idCliente:
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

def gastoTotalCliente(listaVentas, idClienteVenta):
    contGasto = 0
    for venta in listaVentas:
        if idClienteVenta == venta.idClienteVenta:
            contGasto += float(venta.dineroGastado)
    return contGasto

def pizzaNapolitana(archivoInventario):
    elegir_tamaño = input("\nIngrese el tamaño de su pizza\n1-Tamaño personal\n2-Tamaño mediano\n3-Tamaño familiar\n")
    if elegir_tamaño == "1":
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';') 
            datos = list(contenido)
            caja = "cajaPersonal"
            salsa = "salsa"
            queso = "mozzarella"
            masa = "masa"
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
        with open(archivoInventario,'w', newline = '') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(datos)

    elif elegir_tamaño == "2":
        with open(archivoInventario,'r') as archivo:
            contenido = csv.reader(archivo, delimiter = ';') 
            datos = list(contenido)
            caja = "cajaPersonal"
            salsa = "salsa"
            queso = "mozzarella"
            masa = "masa"
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
                    pos3 -= 2
                    fila[1] = str(pos3)
        with open(archivoInventario,'w', newline = '') as archivo:
            escritor = csv.writer(archivo, delimiter = ';')
            escritor.writerows(datos)    

    elif elegir_tamaño == "3":
            with open(archivoInventario,'r') as archivo:
                contenido = csv.reader(archivo, delimiter = ';') 
                datos = list(contenido)
                caja = "cajaPersonal"
                salsa = "salsa"
                queso = "mozzarella"
                masa = "masa"
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
                        pos3 -= 3
                        fila[1] = str(pos3)
            with open(archivoInventario,'w', newline = '') as archivo:
                escritor = csv.writer(archivo, delimiter = ';')
                escritor.writerows(datos)
        
            

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
            idIngreso = input("Ingrese su Id por favor: ")
            verificarCliente = buscarClientePorId(listaClientes, idIngreso)
            if verificarCliente:
                print(f"Hola {verificarCliente.nombre}, cual es su pedido?")
                break #^ Coloco break mientras tanto porque aun no se ha implementado una funcion para hacer pedido
            else:
                opcionRegistro = input("Id no encontrado, desea registrarse?\n\n1.-Si\n2.-No\n")
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
                    print(f"\nUsted se ha registrado exitosamente, su id es: {idNuevoUsuario}")
                    break
                elif opcion_registro_verificada == "2":
                    print("Para poder realizar un pedido debe registrarse, hasta luego!!")
                    break

        elif opcion_verificada_cliente == "2":
            print("Saliendo, gracias por preferirnos!!")

        else:
            print("Opcion invalida, ingrese nuevamente")
            opcion_verificada_cliente = input("Que desea hacer?\n1.-Realizar un pedido\n2.-Salir\n")

elif opcion_trabajador_cliente == "2":
    opcion_trabajador = input("Que desea hacer el dia de hoy?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")
    opcion_trabajador_verificar = valor_numerico(opcion_trabajador)
    opcion_trabajador_verificada = opcion_trabajador_verificar
    while opcion_trabajador_verificada != "7":
        if opcion_trabajador_verificada == "1":
            print("El capital actual es:",capital) #^ Esta opcion aun esta incompleta ya que se debe acordar como se va a guardar el capital, esto es un mero ejemplo
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")
        
        elif opcion_trabajador_verificada == "2":
            id_buscar_gasto = input("Ingrese el Id del cliente para buscar su gasto total: ")
            id_buscar_gasto_verificar = valor_numerico(id_buscar_gasto)
            id_buscar_gasto_verificada = id_buscar_gasto_verificar
            gastoCliente = gastoTotalCliente(listaVentas, id_buscar_gasto_verificada)
            if gastoCliente == 0.00:
                print("\nId no encontrado\n")
            else:
                print("\nEl gasto total del cliente con Id {} es: {:.2f}\n".format(id_buscar_gasto_verificada, gastoCliente))
                opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")

        elif opcion_trabajador_verificada == "3":
            mostrar_ingrediente("inventario.csv")
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")

        elif opcion_trabajador_verificada == "4":
            print("Funcion aun no implementada")
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")

        elif opcion_trabajador_verificada == "5":
            totalPropinas = propinasTotales(listaVentas)
            print("\nEl total de propinas es: {:.2f}\n".format(totalPropinas))
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")

        elif opcion_trabajador_verificada == "6":
            totalGanancias = gananciasTotales(listaVentas)
            print("\nEl total de ganancias obtenidas en las ventas es de: {:.2f}\n".format(totalGanancias))
            opcion_trabajador_verificada = input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")

        elif opcion_trabajador_verificada == "7":
            print("Saliendo, hasta la proxima!!")

        else:
            print("Ingrese una opcion valida")
            opcion_trabajador_verificada = input("Que desea hacer el dia de hoy?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Mostrar total de ganancias\n7.-Salir\n")

else:
    print("Ingrese una opcion valida por favor\n")
print("Gracias por visitar la app de nuestra pizzeria, vuelve pronto :)")
# for fila in listaClientes:
#     print(', '.join(fila))