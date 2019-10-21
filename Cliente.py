from db_config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Cliente(Base):
    __tablename__ = 'cliente'

    clienteId = Column('clienteId', Integer, primary_key=True)

    nombre = Column('nombre', String(70), nullable=False)

    apellido = Column('apellido', String(70), nullable=False)

    domicilio = Column('domicilio', String(100), nullable=False)

    telefono = Column('telefono', String(15), nullable=False)

    email = Column('email', String(70))

    dni = Column('dni', String(10), nullable=False)

    propiedades = relationship('Inmueble', back_populates="propietario")

    alquilando = relationship('Alquiler', back_populates="inquilino")

    def __repr__(self):
        return str(self.nombre) + ' ' + str(self.apellido) + ' ' + str(self.dni)
