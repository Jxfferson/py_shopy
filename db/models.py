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