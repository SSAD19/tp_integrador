from peewee import *
from utils import db_obras


class BaseModel(Model):
    
    class Meta:
        database = db_obras.db_sqlite

class AreaResponsable(BaseModel):
    id_area = AutoField(primary_key= True)
    nombre_area = CharField(unique = True, max_length=100)
    
    class Meta:
        db_table= 'areas_respondables'    
    
class TipoObra(BaseModel):
   
    id_tipo_obra = AutoField(primary_key=True)
    nombre = CharField()
    
    
    class Meta:
        db_table = 'tipos_obra'


class TipoContratacion(BaseModel):
    id_tipo_contratacion= AutoField(primary_key=True)
    nombre_tipo = CharField(unique = True)
    
    class Meta:
        db_table = 'tipo_contratacion'


class Predio(BaseModel):
    id_predio = AutoField()
    comuna = CharField(unique = True)
    barrio = CharField(unique = True)
    
    class Meta:
        db_table = 'predios'

class Empresa (BaseModel):
    id_empresa = AutoField(primary_key=True)
    razon_social = CharField(unique=True)
    cuit = IntegerField(unique=True)
    activa = BooleanField(default=True) 
    
    class Meta:
        db_table = 'empresas'
        
class Contratacion(BaseModel): 
    id_contratacion = AutoField(primary_key=True)
    nro_contratacion = CharField(unique=True)
    tipo_contratacion = ForeignKeyField(TipoContratacion) 
    empresa = ForeignKeyField(Empresa)    
    mano_de_obra = IntegerField()
    
    class Meta:
        db_table = 'contrataciones'

class Licitacion(BaseModel):
    id_licitacion = AutoField(primary_key = True)
    licitacion_anio = DateField()
    descripcion = TextField()
    area_responsable = ForeignKeyField(AreaResponsable)
    
    #Este campo es la URL donde pueden descargar los pliegos que estarán en una base de dato externa -nube/servidor
    pliegos= CharField()
    
    
    class Meta:
        db_table= 'licitaciones'    
        
class EtapaObra(BaseModel):
    id_etapa_obra = AutoField(primary_key=True)
    nombre = CharField(unique = True, max_length=100)
    estado = BooleanField(default=True)

    class Meta:
        db_table= 'etapas_obra'



#TODO: clase obra - COMPLETAR SIGUIENDO ESQUEMA DE LAS CLASES YA HECHAS 

class Obra(BaseModel):
    
    id_obra = AutoField(primary_key=True)
    entorno = CharField(unique = True)
    nombre = CharField(unique = True)
    tipo_obra = ForeignKeyField(TipoObra)
    etapa_obra =ForeignKeyField(EtapaObra)
    licitacion = ForeignKeyField(Licitacion)
    contratacion = ForeignKeyField(Contratacion)
    predio = ForeignKeyField(Predio)
    direccion = CharField()
    lat = FloatField()
    long = FloatField()
    fecha_inicio = DateField()
    fecha_estimada_fin = DateField()
    
    
    #TODO: FUNCIONES 
    def nuevo_proyecto(self):
        #CREAR UNA LICITACION
        #CREAR OBRA SOLO ON ID, NOMBRE Y LICITACION CREADA
        pass
    
    def iniciar_contratacion(self):
        #CREAR UNA CONTRATACION ENLAZANDO AL ID DE OBRA
        pass
    
    def adjudicar_obra(self):
        #CREAR O BUSCAR EMPRESA (?)
        pass
    
    def iniciar_obra(self):
        #MODIFICAR LA ETAPA DE OBRA O CREAR CAMPO DE FECHA DE INICI
        pass
    
    def actualizar_porcentaje_avance(self):
        #segun la etapa en la que esta (numero de etapas) modificar el porcentaje
        pass
    
    def incrementar_plazo(self): 
        #incremenar dias a la fecha estimada fin
        pass
    
    def incrementar_mano_obra(self, num):
        # sumar num a la mano de obra que esta en clase contratacion 
        pass
    
    def finalizar_obra(self):
        #actualizar etapa de obra
        pass
    
    def rescindir_obra(self):
        #¿actualizar etapa obra?
        pass
    
class Meta:
    db_table = 'obra'
    
    

