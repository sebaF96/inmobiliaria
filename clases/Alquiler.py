from config.db_config import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property


class Alquiler(Base):
    __tablename__ = 'alquiler'

    __alquilerId = Column('alquilerId', Integer, primary_key=True)

    __fechainicio = Column('fechainicio', DateTime, default=func.now())

    __mesesduracion = Column('mesesduracion', Integer, nullable=False)

    __mesespagados = Column('mesespagados', Integer, nullable=False, default=1)

    inmuebleId = Column('inmuebleId', ForeignKey('inmueble.inmuebleId'), nullable=False)

    inmueble = relationship('Inmueble', back_populates="alquiler", uselist=False)

    inquilinoId = Column('inquilinoId', ForeignKey('cliente.clienteId'), nullable=False)

    inquilino = relationship('Cliente', back_populates="alquilando")

    @hybrid_property
    def alquilerId(self):
        return self.__alquilerId

    @hybrid_property
    def fechainicio(self):
        return self.__fechainicio

    @fechainicio.setter
    def fechainicio(self, value):
        self.__fechainicio = value

    @property
    def mesesduracion(self):
        return self.__mesesduracion

    @mesesduracion.setter
    def mesesduracion(self, value):
        self.__mesesduracion = value

    @property
    def mesespagados(self):
        return self.__mesespagados

    @mesespagados.setter
    def mesespagados(self, value):
        self.__mesespagados = value

    def __repr__(self):
        return 'Casa: ' + str(self.inmueble) + '\nInquilino:  ' + str(self.inquilino) + '\nDueño:  ' + str(
            self.inmueble.propietario) + "\nInicio de alquiler: " + str(
            self.fechainicio.strftime("%d %B, %Y")) + "\nMeses de duracion: " + str(
            self.mesesduracion) + '\nMeses pagados: ' + str(self.mesespagados)
