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


def listar_propiedades():
    casas_disponibles = session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(Inmueble.inmuebleId).all()
    for casa in casas_disponibles:
        casa.mostrar_datos()


def get_cliente():
    dni = int(input("DNI: "))
    try:
        return session.query(Cliente).filter(Cliente.dni == dni).one()
    except exc.SQLAlchemyError:
        print("No existe un cliente de DNI " + str(dni))
        return None


def agregar_alquiler(inquilino_id, inmueble_id):
    alquiler = Alquiler()

    alquiler.inquilinoId = inquilino_id
    alquiler.inmuebleId = inmueble_id
    alquiler.mesesduracion = int(input("Meses de duracion: "))
    casa = session.query(Inmueble).filter(Inmueble.inmuebleId == inmueble_id).one()
    casa.alquilado = 1
    insert_in_db(alquiler)

    print("Alquiler registrado con exito!")


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
