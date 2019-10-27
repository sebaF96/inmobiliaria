from config.menu_config import print_menu, curses, opciones_menu, set_menu
from utils.context_functions import *
import time
import os


def main(stdscr):
    current_row_idx = 0
    set_menu()
    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx = current_row_idx - 1
        elif key == curses.KEY_DOWN and current_row_idx < len(opciones_menu) - 1:
            current_row_idx = current_row_idx + 1
        elif key == curses.KEY_RIGHT:
            current_row_idx = len(opciones_menu) - 1
        elif key == curses.KEY_LEFT:
            current_row_idx = 0
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.refresh()
            curses.endwin()
            os.system('clear')

            if current_row_idx == 0:  # Agregar cliente

                agregar_cliente()
                time.sleep(2.2)

            # Modificar cliente

            elif current_row_idx == 1:  # Listar propiedades

                for casa in db.listar_inmuebles():
                    casa.mostrar_datos()

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 2:  # Agregar propiedad

                print("Ingrese el dni del dueño de la propiedad\n")
                cliente = db.get_cliente()
                if db.cliente_existe(cliente):
                    agregar_propiedad(cliente.clienteId)

                time.sleep(2.2)

            elif current_row_idx == 3:  # Registrar alquiler
                print("Ingrese DNI del inquilino")
                inquilino = db.get_cliente()

                if db.cliente_existe(inquilino):
                    agregar_alquiler(inquilino.clienteId)

                time.sleep(2.2)

            elif current_row_idx == 4:  # Listar alquileres
                choice = int(input("1. DNI dueño\n2. DNI inquilino\n3. Todos\n"))

                cliente = db.get_cliente() if choice == 1 or choice == 2 else 0

                for alquiler in db.listar_alquileres(cliente, choice):
                    print("\n" + str(alquiler))

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 5:  # Ver cliente
                choice = int(input("1. Filtrar por DNI\n2. Filtrar por apellido\n3. Todos\n"))
                for cliente in db.listar_clientes(choice):
                    print("\n")
                    cliente.mostrar_datos()

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 6:  # Borrar alquiler
                print("Ingrese el dni del inquilino")
                inquilino = db.get_cliente()
                borrar_alquiler(inquilino)

                time.sleep(2.2)

            elif current_row_idx == 7:  # Borras propiedad
                print("Ingrese el dni del dueño")
                cliente = db.get_cliente()
                if db.cliente_existe(cliente):
                    borrar_propiedad(cliente)

                time.sleep(2.2)

            elif current_row_idx == 8:  # Registrar pago
                print("Ingrese el dni del inquilino")
                cliente = db.get_cliente()
                if db.cliente_existe(cliente):
                    registrar_pago(cliente)

                time.sleep(2.2)

            elif current_row_idx == 9:  # Imprimir
                casas_disponibles = db.listar_inmuebles()
                imprimir_casas(casas_disponibles)
                print("Archivo generado con exito!")

                time.sleep(1.3)

            elif current_row_idx == 10:
                cliente = db.get_cliente()
                modificar_cliente(cliente)

                time.sleep(2.2)

            elif current_row_idx == 11:
                print("Ingrese dni del dueño")
                cliente = db.get_cliente()
                modificar_propiedad(cliente)

                time.sleep(2.2)

            elif current_row_idx == len(opciones_menu) - 1:  # Salir
                print("Hasta luego!")
                for x in range(7):
                    time.sleep(0.2)
                    print(".")
                os.system('clear')
                break

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()


curses.wrapper(main)
