from config.menu_config import print_menu, curses, opciones_menu
from funciones import agregar_cliente, agregar_alquiler, agregar_propiedad, borrar_propiedad, borrar_alquiler,\
    imprimir_casas
import utils.db_functions as db
import time
import os


def main(stdscr):
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0
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
                time.sleep(3)

            elif current_row_idx == 1:  # Listar propiedades

                for casa in db.listar_inmuebles():
                    casa.mostrar_datos()

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 2:  # Agregar propiedad

                print("Ingrese el dni del dueño de la propiedad\n")
                cliente = db.get_cliente()
                if db.cliente_existe(cliente):
                    agregar_propiedad(cliente.clienteId)

                time.sleep(3)

            elif current_row_idx == 3:  # Registrar alquiler
                print("Ingrese DNI del inquilino")
                inquilino = db.get_cliente()

                if db.cliente_existe(inquilino):
                    for casa in db.listar_inmuebles():
                        casa.mostrar_datos()

                    inmueble_id = int(input("\nIngrese el numero de propiedad: "))
                    agregar_alquiler(inquilino.clienteId, inmueble_id)

                time.sleep(3)

            elif current_row_idx == 4:  # Listar alquileres
                choice = int(input("1. DNI dueño\n2. DNI inquilino\n3. Todos\n"))

                if choice == 1 or choice == 2:
                    cliente = db.get_cliente()
                else:
                    cliente = 0

                for alquiler in db.listar_alquileres(cliente, choice):
                    print("\n")
                    print(alquiler)

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

                time.sleep(3)

            elif current_row_idx == 7:  # Borras propiedad
                print("Ingrese el dni del dueño")
                cliente = db.get_cliente()
                if db.cliente_existe(cliente):
                    borrar_propiedad(cliente)

                time.sleep(3)

                '''            
                elif current_row_idx == 8:  # Registrar pago
                dni_inquilino = int(input("Ingrese el dni del inquilino: "))
                if session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni_inquilino).count() == 1:
                    alquiler = session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni_inquilino).one()
                    meses = registrar_pago(alquiler.inmueble)
                    if meses != 0:
                        alquiler.mesespagados = alquiler.mesespagados + meses
                        session.commit()
                        print("Pago registrado con exito")
                else:
                    print("Este cliente no existe o no esta alquilando ninguna propiedad")
                time.sleep(3)
                '''
            elif current_row_idx == 9:  # Imprimir
                casas_disponibles = db.listar_inmuebles()
                imprimir_casas(casas_disponibles)
                print("Archivo generado con exito!")
                time.sleep(3)

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
