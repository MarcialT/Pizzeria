
#! Comentario de error
#* Comentario de exito
#? Comentario de duda
# Comentario normal

print("---BIENVENIDO A LA APP OFICIAL DE LA PIZZERIA---")
trabajador_cliente = int(input("Usted es un cliente o trabajador?\n1.-Cliente\n2.-Trabajador\n"))
if trabajador_cliente == 1:
    opcion_cliente = int(input("Que desea hacer?\n1.-Realizar un pedido\n2.-Salir\n"))

if trabajador_cliente == 2:
    opcion_trabajador = int(input("Que desea hacer el dia de hoy?\n1.-Mostrar el capital actual de la pizzeria\n2.-Mostrar cuanto gasto un cliente\n3.-Mostrar cuanto queda de algun ingrediente\n4.-Modificar archivo de clientes o ventas\n5.-Mostrar total de propinas\n6.-Salir\n"))