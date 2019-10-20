from modelos import Cliente, Inmueble, Alquiler
import curses

opciones = ["Registrar cliente", "Listar propiedades", "Añadir propiedad", "Registrar alquiler", "Ver alquileres",
            "Ver clientes", "Borrar alquiler", "Borrar propiedad", "Registrar pago", "Salir"]


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(opciones):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(opciones) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def agregar_propiedad(duenioid):

    propiedad = Inmueble()

    propiedad.ubicacion = str(input("Ubicacion: "))
    propiedad.habitaciones = int(input("Cantidad de habitaciones: "))
    propiedad.banios = int(input("Cantidad de baños: "))
    propiedad.zona = str(input("Zona: "))
    propiedad.tamanio = str(input("Tamaño: "))
    propiedad.descripcion = str(input("Descripcion: "))
    propiedad.propietarioId = duenioid

    return propiedad


def agregar_cliente():

    cliente = Cliente()

    cliente.dni = str(input("DNI: "))
    cliente.nombre = str(input("Nombre: "))
    cliente.apellido = str(input("Apellido: "))
    try:
        cliente.telefono = int(input("Telefono: "))
    except ValueError:
        print("El telefono no puede contener letras, reintente")
    cliente.domicilio = str(input("Domicilio: "))
    cliente.email = str(input("Email: "))

    return cliente


def agregar_alquiler(inquilino_id, inmueble_id):
    alquiler = Alquiler()

    alquiler.inquilinoId = inquilino_id
    alquiler.inmuebleId = inmueble_id
    alquiler.mesesduracion = int(input("Meses de duracion: "))

    return alquiler


def mostrar_cliente(cliente):
    print(cliente)
    print("Telefono: " + str(cliente.telefono))
    print("Domicilio: " + str(cliente.domicilio))
    print("Email: " + str(cliente.email))
    print("Dueño de: ")
    for propiedad in cliente.propiedades:
        print(propiedad)


def registrar_pago(Inmueble):
    meses = int(input("Cantidad de meses a pagar: "))
    print("\nUsted pagara "+str(meses) + "meses por una suma de $" + str(Inmueble.precio * meses))
    confirmacion = str(input("Confirmar operacion? (S/N)\n"))
    if confirmacion != 's' and confirmacion != 'S':
        meses = 0
    return meses
