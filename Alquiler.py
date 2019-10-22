from db_config import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


class Alquiler(Base):
    __tablename__ = 'alquiler'

    alquilerId = Column('alquilerId', Integer, primary_key=True)

    inmuebleId = Column('inmuebleId', ForeignKey('inmueble.inmuebleId'), nullable=False)

    inmueble = relationship('Inmueble', back_populates="alquiler", uselist=False)

    inquilinoId = Column('inquilinoId', ForeignKey('cliente.clienteId'), nullable=False)

    inquilino = relationship('Cliente', back_populates="alquilando")

    fechainicio = Column('fechainicio', DateTime, default=func.now())

    mesesduracion = Column('mesesduracion', Integer, nullable=False)

    mesespagados = Column('mesespagados', Integer, nullable=False, default=1)

    def __repr__(self):
        return 'Casa: ' + str(self.inmueble) + '\nInquilino:  ' + str(self.inquilino) + '\nDueño:  ' + str(
            self.inmueble.propietario) + "\nInicio de alquiler: " + str(
            self.fechainicio.strftime("%d %B, %Y")) + "\nMeses de duracion: " + str(
            self.mesesduracion) + '\nMeses pagados: ' + str(self.mesespagados)
