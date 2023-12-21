from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, Text, Date
from werkzeug.security import generate_password_hash, check_password_hash


class Auto(Base):
    __tablename__ = 'Autos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(64))
    pais = Column(String(30))
    year = Column(Integer)
    cantidad_fotos = Column(Integer)
    reservas = relationship('Reserva')

    def __init__(self, nombre=None, pais=None, year=None, cantidad_fotos=None):
        self.nombre = nombre
        self.pais = pais
        self.year = year
        self.cantidad_fotos = cantidad_fotos

    def __str__(self):
        return str(self.id)


class Reserva(Base):
    __tablename__ = 'Reservas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_auto = Column(Integer, ForeignKey('Autos.id'))
    fecha = Column(Date)

    def __init__(self, id_auto=None, fecha=None):
        self.id_auto = id_auto
        self.fecha = fecha


class Usuario(Base):
    __tablename__ = 'Usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password = Column(String(66))
    email = Column(String(45))
    grupo = Column(Integer, ForeignKey('Grupos.id'))


    def __init__(self, username=None, password=None, email=None, grupo=None):
        self.username = username
        self.password = self.__encriptar_pass(password)
        self.email = email
        self.grupo = grupo

    def __encriptar_pass(self, password):
        return generate_password_hash(password)

    def validar_password(self, password_a_validar):
        return check_password_hash(self.password, password_a_validar)


class Grupo(Base):
    __tablename__ = 'Grupos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    descripcion = Column(String(50))
    #permisos = relationship('Permiso', secondary='GrupoPermiso')

    def __init__(self, nombre=None, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion


class Permiso(Base):
    __tablename__ = 'Permisos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    descripcion = Column(String(50))
    #grupos = relationship('Grupo', secondary='GrupoPermiso')

    def __init__(self, nombre=None, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion

'''
class GrupoPermiso(Base):
    __tablename__ = 'Grupo_Permiso'
    id_grupo = Column(Integer,  ForeignKey('Grupos.id'))
    id_permiso = Column(Integer,  ForeignKey('Permisos.id'))
'''
