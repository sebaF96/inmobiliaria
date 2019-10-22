from funciones import *
from consultas import *
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
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.refresh()
            curses.endwin()
            os.system('clear')

            if current_row_idx == 0:  # Agregar cliente

                agregar_cliente()
                time.sleep(3)

            elif current_row_idx == 1:  # Listar propiedades

                listar_propiedades()

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 2:  # Agregar propiedad

                print("Ingrese el dni del dueño de la propiedad\n")
                cliente = get_cliente()
                if cliente_existe(cliente):
                    agregar_propiedad(cliente.clienteId)

                time.sleep(3)

            elif current_row_idx == 3:  # Registrar alquiler
                print("Ingrese DNI del inquilino")
                inquilino = get_cliente()

                if cliente_existe(inquilino):
                    listar_propiedades()
                    inmueble_id = int(input("\nIngrese el numero de propiedad: "))
                    agregar_alquiler(inquilino.clienteId, inmueble_id)

                time.sleep(2)

            elif current_row_idx == 4:  # Listar alquileres
                choice = int(input("1. DNI dueño\n2. DNI inquilino\n3. Todos\n"))

                if choice == 1 or choice == 2:
                    cliente = get_cliente()
                else:
                    cliente = 0

                listar_alquileres(cliente, choice)

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 5:  # Ver cliente
                choice = int(input("1. Filtrar por DNI\n2. Todos\n"))
                if choice == 1:
                    cliente = get_cliente()
                    if cliente_existe(cliente):
                        cliente.mostrar_datos()
                    else:
                        print("Cliente no encontrado")
                elif choice == 2:
                    listar_clientes()

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 6:  # Borrar alquiler
                print("Ingrese el dni del inquilino")
                inquilino = get_cliente()
                borrar_alquiler(inquilino)

                time.sleep(2)

            elif current_row_idx == 7:  # Borras propiedad
                ownerdni = int(input("Ingrese el DNI del dueño "))
                if cliente_existe(ownerdni):
                    propiedades = session.query(Inmueble).join(Cliente).filter(Inmueble.alquilado == 0,
                                                                               Cliente.dni == ownerdni).order_by(
                        Inmueble.inmuebleId).all()

                    for casa in propiedades:
                        print(casa.inmuebleId, casa)

                    propiedad_id = int(input("\n\nSeleccione la propiedad a eliminar "))
                    try:
                        propiedad = session.query(Inmueble).filter(Inmueble.inmuebleId == propiedad_id).one()
                        print(propiedad)
                        confirmacion = str(input("\nSeguro que desea borrar esta propiedad? (s/n)"))
                        if confirmacion == 'S' or confirmacion == 's':
                            session.delete(propiedad)
                            session.commit()
                            print("Propiedad borrada con exito")
                            time.sleep(2)
                    except exc.SQLAlchemyError:
                        print("Seleccion incorrecta")
                else:
                    print("El cliente no existe")
                time.sleep(2)

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
                time.sleep(2)

            elif current_row_idx == 9:  # Imprimir
                casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(
                    Inmueble.precio).all()

                imprimir_casas(casas_disponibles)

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
