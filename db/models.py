from .database import Base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean, Enum, ForeignKey, Time
from sqlalchemy.orm import relationship

#Tablas


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
    trueques_Usuario = Column(Integer)
    fecha_registro = Column(Date)
    foto_perfil = Column(String(255), 
                default='default.jpg')
    descripcion_Usuario = Column(String(200))
    rol_UsuarioFK = Column(Integer,
                ForeignKey("Rol.id_Rol"))

class Habilidades(Base):
    __tablename__ = "habilidades"
    id_Habilidades = Column(Integer, 
                primary_key=True)
    nombre_Habilidades = Column(String(50))
    descripcion_Habilidades = Column(String(200))
    categoria_Habilidades = Column(String(50))
    id_usuarioFK = Column(Integer,
                ForeignKey("usuario.id_Usuario")) 
    categoria_Habilidad = Column(Integer,
                ForeignKey("categoria_habilidad.id_categoria"))
    
class categoria_habilidad(Base):
    __tablename__ = "categoria_habilidad"
    id_categoria = Column(Integer,
                          primary_key=True)
    categoria = Column(String(200)) 
    descripcion = Column(String(200)) 
    estado = Column(Boolean)  
    
class Intercambios(Base):
    __tablename__ = "intercambios"
    id_Intercambios = Column(Integer, 
                primary_key=True)
    fecha_Intercambio = Column(Date)
    estado_Intercambio = Column(Boolean)
    descripcion_Intercambio = Column(String(200))
    id_UsuarioFK = Column(Integer,
                ForeignKey("usuario.id_Usuario")) 
    id_HabilidadesFK = Column(Integer, 
                ForeignKey("habilidades.id_Habilidades"))    
   
class Curso(Base):
    __tablename__ = "curso"
    id_Curso = Column(Integer, 
                      primary_key=True) 
    nombre_Curso = Column(String(50))
    descripcion_Curso = Column(String(200))
    fecha_Curso = Column(Date)
    estado_Curso = Column(Boolean) 
    calificaciones = Column(Float)
    id_UsuarioFK = Column(Integer,
                ForeignKey("usuario.id_Usuario")) 
    id_HabilidadesFK = Column(Integer, 
                ForeignKey("habilidades.id_Habilidades")) 
        
            
class sesiones(Base):
    __tablename__ = "sesiones"
    id_sesiones = Column(Integer, 
                primary_key=True)
    fecha_inicio = Column(Date)
    hora_inicio = Column(Time) 
    tematica = Column(String(200))
    Estado = Column(Boolean) 
    id_IntercambioFK = Column(Integer,
                ForeignKey("intercambios.id_Intercambios"))
    id_cursoFK = Column(Integer,    
                ForeignKey("curso.id_Curso")) 

class Materiales(Base):
    __tablename__ = "materiales"
    id_Materiales = Column(Integer, 
                primary_key=True)
    nombre_Materiales = Column(String(50))
    descripcion_Materiales = Column(String(200))
    tipo_Materiales = Column(Enum('documento','video','audio')) 
    url_Materiales = Column(String(200)) 
    fecha_Subida = Column(Date) 
    id_IntercambioFK = Column(Integer,
                ForeignKey("intercambios.id_Intercambios"))  
    id_cursoFK = Column(Integer,
                ForeignKey("curso.id_Curso")) 
    
        

    