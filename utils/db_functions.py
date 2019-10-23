from config.db_config import Session
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


def set_alquilado(inmueble, value):
    inmueble.alquilado = value


def cliente_existe(cliente):
    existe = False
    if cliente is not None:
        if session.query(Cliente).filter(Cliente.dni == cliente.dni).count() == 1:
            existe = True
    return existe


def get_cliente():
    dni = int(input("DNI: "))
    try:
        return session.query(Cliente).filter(Cliente.dni == dni).one()
    except exc.SQLAlchemyError:
        print("No existe un cliente de DNI " + str(dni))
        return None


def get_inmueble(inmueble_id):
    return session.query(Inmueble).filter(Inmueble.inmuebleId == inmueble_id).one()


def get_alquiler(alquiler_id):
    return session.query(Alquiler).filter(Alquiler.alquilerId == alquiler_id).one()


def listar_clientes(filtro):
    lista_clientes = []
    if filtro == 1:     # Filtrar por DNI
        cliente = get_cliente()
        if cliente_existe(cliente):
            lista_clientes.append(cliente)
    elif filtro == 2:
        apellido = str(input("Apellido: "))
        lista_clientes = session.query(Cliente).filter(Cliente.apellido.ilike('%'+apellido+'%')).all()

    elif filtro == 3:
        lista_clientes = session.query(Cliente).all()

    return lista_clientes


def listar_inmuebles(cliente=0):
    if cliente != 0:
        return session.query(Inmueble).filter(Inmueble.alquilado == 0, Inmueble.propietario == cliente).all()
    else:
        return session.query(Inmueble).filter(Inmueble.alquilado == 0).order_by(Inmueble.inmuebleId).all()


def listar_alquileres(cliente, args):
    alquileres = []

    if args == 1 and cliente_existe(cliente):   # Filtrar por dueño
        alquileres = session.query(Alquiler).join(Inmueble).join(Cliente).filter(Cliente.dni == cliente.dni).all()

    elif args == 2 and cliente_existe(cliente):  # Filtrar por inquilino
        alquileres = session.query(Alquiler).join(Cliente).filter(Cliente.dni == cliente.dni).all()

    elif args == 3:
        alquileres = session.query(Alquiler).order_by(Alquiler.fechainicio).all()

    return alquileres


def contar_alquileres(dni):
    return session.query(Alquiler).join(Cliente).filter(Cliente.dni == dni).count()
