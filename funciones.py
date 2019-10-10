from modelos import Cliente, Inmueble, Alquiler

def AgregarPropiedad(duenioid):

    propiedad = Inmueble()

    propiedad.ubicacion = str(input("Ubicacion: "))
    propiedad.habitaciones = int(input("Cantidad de habitaciones: "))
    propiedad.banios = int(input("Cantidad de baños: "))
    propiedad.zona = str(input("Zona: "))
    propiedad.tamanio = str(input("Tamaño: "))
    propiedad.descripcion = str(input("Descripcion: "))
    propiedad.propietarioId = duenioid

    return propiedad


def AgregarCliente():

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


def AgregarAlquiler(inquilino_id, inmueble_id):
    alquiler = Alquiler()

    alquiler.inquilinoId = inquilino_id
    alquiler.inmuebleId = inmueble_id
    alquiler.mesesduracion = int(input("Meses de duracion: "))

    return alquiler


def BorrarAlquiler():
    pass


def VenderCasa():
    pass


def ListarCasas():
    pass