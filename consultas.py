from db_config import Session
from Cliente import Cliente
from Alquiler import Alquiler
from Inmueble import Inmueble
from sqlalchemy import exc

session = Session()


def insert_in_db(objeto):
    session.add(objeto)
    session.commit()


def delete_from_db(objeto):
    session.delete(objeto)
    session.commit()


def cliente_existe(cliente):
    aux = False
    if cliente is not None:
        if session.query(Cliente).filter(Cliente.dni == cliente.dni).count() == 1:
            aux = True
    return aux


def get_cliente():
    dni = int(input("DNI: "))
    try:
        return session.query(Cliente).filter(Cliente.dni == dni).one()
    except exc.SQLAlchemyError:
        print("No existe un cliente de DNI " + str(dni))
        return None


def agregar_cliente():

    cliente = Cliente()

    cliente.dni = str(input("DNI: "))
    if not cliente_existe(cliente):
        cliente.nombre = str(input("Nombre: "))
        cliente.apellido = str(input("Apellido: "))
        cliente.telefono = int(input("Telefono: "))
        cliente.domicilio = str(input("Domicilio: "))
        cliente.email = str(input("Email: "))

        insert_in_db(cliente)
        print("\nCliente añadido con exito!")
    else:
        print("\nEl cliente que esta intentando añadir ya existe")


def listar_clientes():
    clientes = session.query(Cliente).all()

    for cliente in clientes:
        print("\n")
        cliente.mostrar_datos()


def listar_propiedades():
    casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(Inmueble.inmuebleId).all()
    for casa in casas_disponibles:
        casa.mostrar_datos()


def agregar_propiedad(duenioid):
    propiedad = Inmueble()

    propiedad.ubicacion = str(input("Ubicacion: "))
    propiedad.habitaciones = int(input("Cantidad de habitaciones: "))
    propiedad.banios = int(input("Cantidad de baños: "))
    propiedad.zona = str(input("Zona: "))
    propiedad.tamanio = str(input("Tamaño: "))
    propiedad.descripcion = str(input("Descripcion: "))
    propiedad.propietarioId = duenioid

    insert_in_db(propiedad)
    print("\n Propiedad añadida con exito!")


def agregar_alquiler(inquilino_id, inmueble_id):
    alquiler = Alquiler()

    alquiler.inquilinoId = inquilino_id
    try:
        alquiler.inmuebleId = inmueble_id
        alquiler.mesesduracion = int(input("Meses de duracion: "))
        casa = session.query(Inmueble).filter(Inmueble.inmuebleId == inmueble_id).one()
        casa.alquilado = 1
        insert_in_db(alquiler)

        print("Alquiler registrado con exito!")
    except exc.SQLAlchemyError:
        print("\nNo se pudo registrar alquiler. Seleccion de casa incorrecta")


def listar_alquileres(cliente, args):

    global alquileres
    if args == 3:
        alquileres = session.query(Alquiler).order_by(Alquiler.fechainicio).all()

    elif args == 2:
        alquileres = session.query(Alquiler).join(Inmueble).join(Cliente).filter(Cliente.dni == cliente.dni).all()

    elif args == 1:
        alquileres = session.query(Alquiler).join(Cliente).filter(Cliente.dni == cliente.dni).all()

    for alquiler in alquileres:
        print("\n")
        print(alquiler)
