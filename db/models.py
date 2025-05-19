from .database import Base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Aprendiz(Base):
    __tablename__ = "aprendiz"
    id_Aprendiz = Column(Integer, 
                primary_key=True)
    nombre_Aprendiz = Column(String(50))
    apellido_Aprendiz = Column(String(50))
    email_Aprendiz = Column(String(60))
        
    clase = relationship("Clase",
                        back_populates="aprendiz")
    
    
class Categorias(Base):
    __tablename__ = "categorias"
    id_Categorias = Column(Integer,
                           primary_key=True)
    descripcion_Categoria = Column(String(100))
    nombre_Categoria = Column(String(50))
    
    #Relacion uno a muchos
    clase = relationship("Clase",
                        back_populates="categorias")
    

class Experto(Base):
    __tablename__ = "experto"
    id_Experto = Column(Integer, 
                primary_key=True)
    nombre_Experto = Column(String(50))
    apellido_Experto = Column(String(50))
    email_Experto = Column(String(60))
    
class Clase(Base):
    __tablename__ = "clase"
    id_Clase = Column(Integer, 
                primary_key=True)
    titulo = Column(String(50))
    descripcion = Column(String(200))
    
#Clave foranea

    categoria_id = Column(Integer, 
                          ForeignKey("categorias.id_Categorias"))
    
    aprendiz_id = Column(Integer, 
                          ForeignKey("aprendiz.id_Aprendiz"))
    
#Relaciones
    
    aprendiz = relationship("Aprendiz",
                        back_populates="roles")
    

class Rol(Base):
    __tablename__ = "Rol"
    id_Rol = Column(Integer, 
                primary_key=True)
    nombre_Rol = Column(String(50))
    estado_Rol = Column(Boolean)
    descripcion_Rol = Column(String(200))
    
class Usuario(Base):
    __tablename__ = "usuario"
    id_Usuario = Column(Integer, 
                primary_key=True)
    nombre_Usuario = Column(String(50))
    apellido_Usuario = Column(String(50))
    email_Usuario = Column(String(60))
    password_Usuario = Column(String(100))
    fecha_Creacion = Column(Date)
    habilidades_Usuario = Column(String(200))
    trueques_Usuario = Column(Integer)
    rol_UsuarioFK = Column(Integer,
                ForeignKey("Rol.id_Rol"))
    
class Trueque(Base):
    __tablename__ = "trueque"
    id_Trueque = Column(Integer, 
                primary_key=True)
    fecha_Trueque = Column(Date)
    estado_Trueque = Column(Boolean)
    descripcion_Trueque = Column(String(200))
    id_UsuariosFK = Column(Integer,
                ForeignKey("usuario.id_Usuario"))
    
class Feedback(Base):
    _tablename__ ="feedback"
    id_Feedback = Column(Integer, 
                primary_key=True)
    fecha_Feedback = Column(Date)
    descripcion_Feedback = Column(String(200))
    calificacion_Feedback = Column(Float)
    id_TruequeFK = Column(Integer,
                ForeignKey("trueque.id_Trueque"))
    id_UsuarioFK = Column(Integer,
                ForeignKey("usuario.id_Usuario"))
    
class Mensaje(Base):
    __tablename__ = "mensaje"
    