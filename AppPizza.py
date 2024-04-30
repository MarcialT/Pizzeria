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

capital = 0

class Clientes:
    def __init__(self, idCliente, nombre, apellido, email):
        self.idCliente = idCliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return(f"Id: {self.idCliente}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email} ")

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
        
listaClientes = leerArchivoClientes(archivoClientes)

def buscarClientePorId(listaClientes, idCliente):
    for cliente in listaClientes:
        if cliente.idCliente == idCliente:
            return cliente
    return None
        
def encontrarUltimoId(archivoClientes):
    ultimo_id = None
    with open(archivoClientes, 'r', newline='', encoding='utf-8') as clientesCsv:
        lectorCsv = csv.reader(clientesCsv, delimiter=';')
        next(lectorCsv)  # Saltar la primera fila si contiene encabezados
        for fila in lectorCsv:
            id_cliente = int(fila[0])
            if ultimo_id is None or id_cliente > ultimo_id:
                ultimo_id = id_cliente
    return ultimo_id
        
# for cliente in listaClientes: #& Estas dos lineas eran para comprobar el funcionamiento de la clase
#     print(cliente) #& Estas dos lineas eran para comprobar el funcionamiento de la clase

print("---BIENVENIDO A LA APP OFICIAL DE LA PIZZERIA---")
trabajador_cliente = int(input("Usted es un cliente o trabajador?\n1.-Cliente\n2.-Trabajador\n"))
if trabajador_cliente == 1:
    opcion_cliente = int(input("Que desea hacer?\n1.-Realizar un pedido\n2.-Salir\n"))
    while opcion_cliente != 2:
        if opcion_cliente == 1:
            idIngreso = input("Ingrese su Id por favor: ")
            verificarCliente = buscarClientePorId(listaClientes, idIngreso)
            if verificarCliente:
                print(f"Hola {verificarCliente.nombre}, cual es su pedido?")
                break #^ Coloco break mientras tanto porque aun no se ha implementado una funcion para hacer pedido
            else:
                opcionRegistro = int(input("Id no encontrado, desea registrarse?\n\n1.-Si\n2.-No\n"))
                if opcionRegistro == 1:
                    ultimoId = encontrarUltimoId(archivoClientes)
                    idNuevoUsuario = ultimoId + 1
                    nombreNuevoUsuario = input("Ingrese su nombre: ")
                    apellidoNuevoUsuario = input("Ingrese su apellido: ")
                    emailNuevoUsuario = input("Ingrese su email: ")
                    registroUsuario = open(archivoClientes, 'a')
                    registroUsuario.write(f"{idNuevoUsuario};{nombreNuevoUsuario};{apellidoNuevoUsuario};{emailNuevoUsuario}\n")
                    registroUsuario.close()
                    print(f"\nUsted se ha registrado exitosamente, su id es: {idNuevoUsuario}")
                    break
                elif opcionRegistro == 2:
                    print("Para poder realizar un pedido debe registrarse, hasta luego!!")
                    break

        elif opcion_cliente == 2:
            print("Saliendo, gracias por preferirnos!!")

        else:
            print("Opcion invalida, ingrese nuevamente")
            opcion_cliente = int(input("Que desea hacer?\n1.-Realizar un pedido\n2.-Salir\n"))

elif trabajador_cliente == 2:
    opcion_trabajador = int(input("Que desea hacer el dia de hoy?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Salir\n"))
    while opcion_trabajador != 6:
        if opcion_trabajador == 1:
            print("El capital actual es:",capital) #^ Esta opcion aun esta incompleta ya que se debe acordar como se va a guardar el capital, esto es un mero ejemplo
            opcion_trabajador = int(input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Salir\n"))
        
        elif opcion_trabajador == 2:
            print("Funcion aun no implementada")
            opcion_trabajador = int(input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Salir\n"))

        elif opcion_trabajador == 3:
            print("Funcion aun no implementada")
            opcion_trabajador = int(input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Salir\n"))

        elif opcion_trabajador == 4:
            print("Funcion aun no implementada")
            opcion_trabajador = int(input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Salir\n"))

        elif opcion_trabajador == 5:
            print("Funcion aun no implementada")
            opcion_trabajador = int(input("Desea hacer algo mas?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Salir\n"))

        elif opcion_trabajador == 6:
            print("Saliendo, hasta la proxima!!")

        else:
            print("Ingrese una opcion valida")
            opcion_trabajador = int(input("Que desea hacer el dia de hoy?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Salir\n"))

else:
    print("Ingrese una opcion valida por favor\n")
print("Gracias por visitar la app de nuestra pizzeria, vuelve pronto:)")
# for fila in listaClientes:
#     print(', '.join(fila))