from funciones import *
from modelos import Cliente, Inmueble, Alquiler
from database import Session
from sqlalchemy import exc
import time
import os


session = Session()


def cliente_existe(dni):
    aux = False
    if session.query(Cliente).filter(Cliente.dni == dni).count() == 1:
        aux = True
    return aux


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0
    print_menu(stdscr, current_row_idx)

    while 1:

        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx = current_row_idx - 1
        elif key == curses.KEY_DOWN and current_row_idx < len(opciones) - 1:
            current_row_idx = current_row_idx + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.refresh()
            curses.endwin()
            os.system('clear')

            if current_row_idx == 0:    # Agregar cliente
                cliente = agregar_cliente()
                if not cliente_existe(cliente.dni):
                    print("\nCliente añadido con exito!\n")
                    print(cliente)
                    session.add(cliente)
                    session.commit()
                else:
                    print("\nEl cliente que esta intentando añadir ya existe")
                time.sleep(2)

            elif current_row_idx == 1:  # Listar propiedades

                casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(
                    Inmueble.inmuebleId).all()

                for casa in casas_disponibles:
                    print("\n")
                    print(casa.inmuebleId, casa)

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 2:  # Agregar propiedad

                ownerdni = str(input("Ingrese el dni del dueño de la propiedad: "))
                if cliente_existe(ownerdni):
                    cliente = session.query(Cliente).filter(Cliente.dni == ownerdni).one()
                    inmueble = agregar_propiedad(cliente.clienteId)
                    print("Propiedad añadida con exito!\n")
                    print(inmueble)
                    session.add(inmueble)
                    session.commit()
                else:
                    print("No hay un cliente de dni " + str(ownerdni))
                time.sleep(3)

            elif current_row_idx == 3:  # Registrar alquiler
                dni_inquilino = str(input("Ingrese DNI del inquilino: "))
                if cliente_existe(dni_inquilino):
                    inquilino = session.query(Cliente).filter(Cliente.dni == dni_inquilino).one()
                    if session.query(Alquiler).filter(Alquiler.inquilino == inquilino).count() == 0:
                        print("Ingrese el numero de propiedad: ")
                        casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(
                            Inmueble.inmuebleId).all()

                        for casa in casas_disponibles:
                            print("\n")
                            print(casa.inmuebleId, casa)

                        inmueble_id = int(input())
                        try:
                            alquiler = agregar_alquiler(inquilino.clienteId, inmueble_id)
                            session.add(alquiler)
                            casa = session.query(Inmueble).filter(Inmueble.inmuebleId == inmueble_id).one()
                            casa.alquilado = 1
                            session.commit()
                            print("\nAlquiler registrado con exito!")

                        except exc.SQLAlchemyError:
                            print("Numero de propiedad incorrecto")
                    else:
                        print("Este cliente ya esta alquilando una propiedad.")
                else:
                    print("No existe cliente de DNI " + str(dni_inquilino))

                time.sleep(2)

            elif current_row_idx == 4:  # Listar alquileres
                print("1. DNI dueño\n2. DNI inquilino\n3. Todos")
                choice = int(input())
                if choice == 1:
                    dni = int(input("Ingrese DNI de cliente "))
                    alquileres = session.query(Alquiler).join(Inmueble).join(Cliente).filter(Cliente.dni == dni).all()

                elif choice == 2:
                    dni = int(input("Ingrese DNI del cliente "))
                    alquileres = session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni).all()

                elif choice == 3:
                    alquileres = session.query(Alquiler).order_by(Alquiler.fechainicio).all()

                for alquiler in alquileres:
                    print("\n")
                    print(alquiler)

                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 5:  # Ver cliente
                dni = int(input("Ingrese el DNI del cliente "))
                if cliente_existe(dni):
                    cliente = session.query(Cliente).filter(Cliente.dni == dni).one()
                    mostrar_cliente(cliente)
                    if session.query(Alquiler).filter(Alquiler.inquilino == cliente).count() > 0:
                        alquiler = session.query(Alquiler).filter(Alquiler.inquilino == cliente).one()
                        print("Alquilando: " + str(alquiler.inmueble))
                    else:
                        print("No esta alquilando ninguna propiedad")
                else:
                    print("\nCliente no encontrado")
                goback = str(input("\n\nPresione una tecla para volver al menu..."))

            elif current_row_idx == 6:  # Borrar alquiler
                dni_inquilino = int(input("Igrese el DNI del inquilino: "))
                try:
                    alquiler = session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni_inquilino).one()
                    print(alquiler)
                    confirmacion = str(input("Seguro que desea borrar el alquiler? (s/n) "))
                    if confirmacion == 'S' or confirmacion == 's':
                        alquiler.inmueble.alquilado = 0
                        session.delete(alquiler)
                        session.commit()
                        print("Alquiler borrado con exito")
                except exc.SQLAlchemyError:
                    print("Este cliente no esta alquilando ninguna propiedad")
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

            elif current_row_idx == len(opciones) - 1:  # Salir
                print("Hasta luego!")
                for x in range(7):
                    time.sleep(0.2)
                    print(".")
                os.system('clear')
                break

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()


curses.wrapper(main)
