# -*- coding: utf-8 -*-

#! Comentario de error
#* Comentario de exito
#? Comentario de duda 
#^ Comentario de incompleto
# Comentario normal

from random import *
import numpy as np
import csv # Libreria para lectura y escritura de csv
import os # Libreria para eliminar archivos

capital = 0


def lectura_clientes():
    with open('clientes.csv', 'r', newline = '') as clientesCSV:
        contenidoClientes = csv.reader(clientesCSV, delimiter = ';')
        return list(contenidoClientes)
    
listaClientes = lectura_clientes() # Se guarda el retorno de la funcion lectura clientes en la variable listaClientes

print("---BIENVENIDO A LA APP OFICIAL DE LA PIZZERIA---")
trabajador_cliente = int(input("Usted es un cliente o trabajador?\n1.-Cliente\n2.-Trabajador\n"))

if trabajador_cliente == 1:
    opcion_cliente = int(input("Que desea hacer?\n1.-Realizar un pedido\n2.-Salir\n"))
    while opcion_cliente != 2:
        if opcion_cliente == 1:
            print("Funcion de realizar pedido no implementada, vuelva mas tarde!")
            opcion_cliente = int(input("Que desea hacer?\n1.-Realizar un pedido\n2.-Salir\n"))

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

