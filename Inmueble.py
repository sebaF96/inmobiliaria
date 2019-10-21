from db_config import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship


class Inmueble(Base):
    __tablename__ = 'inmueble'

    inmuebleId = Column('inmuebleId', Integer, primary_key=True)

    ubicacion = Column('ubicacion', String(100), nullable=False)

    tamanio = Column('tamanio', String(8), nullable=False)

    zona = Column('zona', String(80))

    habitaciones = Column('habitaciones', Integer)

    banios = Column('banios', Integer)

    propietarioId = Column(Integer, ForeignKey('cliente.clienteId'), nullable=False)

    propietario = relationship('Cliente', back_populates="propiedades")

    descripcion = Column('descripcion', String(450), nullable=False)

    alquilado = Column('alquilado', Boolean, default=0)

    alquiler = relationship('Alquiler', back_populates='inmueble')

    precio = Column('precio', Integer, nullable=False, default=6000)

    def __repr__(self):
        return str(self.ubicacion) + ', ' + str(self.habitaciones) + ' habitaciones, ' + str(
            self.descripcion)