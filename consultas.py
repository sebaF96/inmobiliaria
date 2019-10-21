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


def cliente_existe(dni):
    aux = False
    if session.query(Cliente).filter(Cliente.dni == dni).count() == 1:
        aux = True
    return aux


def listar_propiedades():
    return session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(Inmueble.inmuebleId).all()


def get_cliente():
    dni = int(input("DNI: "))
    try:
        return session.query(Cliente).filter(Cliente.dni == dni).one()
    except exc.SQLAlchemyError:
        print("No existe un cliente de DNI " + str(dni))
        return None
