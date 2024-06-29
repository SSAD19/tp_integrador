from peewee import *
from utils import db_obras


class BaseModel(Model):
    
    class Meta:
        database = db_obras.db_sqlite

class AreaResponsable(BaseModel):
    id= AutoField(primary_key= True)
    nombre_area= CharField(unique = True, max_length=100)
    
    class Meta:
        db_table= 'areas_responsables'    
    
class TipoObra(BaseModel):
   
    id= AutoField(primary_key=True)
    nombre= CharField(unique = True)
    
    
    class Meta:
        db_table = 'tipos_obra'

class TipoContratacion(BaseModel):
    id= AutoField(primary_key=True)
    nombre= CharField(unique = True)
    
    class Meta:
        db_table = 'tipo_contratacion'

class Predio(BaseModel):
    id = AutoField()
    barrio = CharField(unique = True)
    
    class Meta:
        db_table = 'predios'

class EtapaObra(BaseModel):
    id = AutoField(primary_key=True)
    nombre = CharField(unique = True, max_length=100)
    
    class Meta:
        db_table= 'etapas_obra'     
        

#Modelos con màs de un campo
class Empresa (BaseModel):
    id = AutoField(primary_key=True)
    razon_social = CharField(unique=True)
    cuit = CharField(null= True, max_length=15)
    activa = BooleanField(default=True) 
    
    class Meta:
        db_table = 'empresas'
        
class Contratacion(BaseModel): 
    id = AutoField(primary_key=True)
    nro_contratacion=CharField(null= True)
    tipo_contratacion=ForeignKeyField(TipoContratacion, null= True) 
    empresa=ForeignKeyField(Empresa, null= True)    
    mano_de_obra=IntegerField(null=True)
    
    class Meta:
        db_table = 'contrataciones'

class Licitacion(BaseModel):
    id= AutoField(primary_key = True)
    expediente= CharField()
    licitacion_anio = DateField(null= True)
    descripcion = TextField(null= True)
    area_responsable = ForeignKeyField(AreaResponsable, null= True)
    #Este campo es la URL donde pueden descargar los pliegos que estarán en una base de dato externa -nube/servidor
    pliegos= CharField(null= True)
    
    
    class Meta:
        db_table= 'licitaciones'    

#TODO: clase obra - COMPLETAR SIGUIENDO ESQUEMA DE LAS CLASES YA HECHAS 
class Obra(BaseModel):
    
    id = AutoField(primary_key=True)
    entorno = CharField(null= True)
    nombre = CharField(null= True)
    tipo_obra = ForeignKeyField(TipoObra,null= True)
    etapa_obra =ForeignKeyField(EtapaObra,null= True)
    licitacion = ForeignKeyField(Licitacion, null= True)
    contratacion = ForeignKeyField(Contratacion, null= True)
    predio = ForeignKeyField(Predio, null= True)
    direccion = CharField(null= True)
    lat = FloatField(null= True)
    long = FloatField(null= True)
    fecha_inicio = DateField(null= True)
    fecha_estimada_fin = DateField(null= True)
    
    
    #TODO: FUNCIONES 
    def nuevo_proyecto(self, **args):
        #TODO:Probar
        #creo la licitacion
        Licitacion.create(args)
        #recupero la licitacion recien creada para tener el id
        Obra.create(
            entorno =args['entorno'],
            nombre= args['nombre'],            
            Licitacion = Licitacion.select().where(Licitacion.expediente == args['expediente']),)
      
        pass
    
    def iniciar_contratacion(self, id:int):
        #CREAR UNA CONTRATACION ENLAZANDO AL ID DE OBRA
        pass
    
    def adjudicar_obra(self):
        #CREAR O BUSCAR EMPRESA (?)
        pass
    
    def iniciar_obra(self):
        #MODIFICAR LA ETAPA DE OBRA O CREAR CAMPO DE FECHA DE INICI
        self.fecha_inicio = TimestampField()
        
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
    
    

