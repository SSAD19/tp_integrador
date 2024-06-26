from peewee import *
from models.base_model import *
from models import tipo_obra as to, etapa_obra as eo, licitacion as li, contrataciones as con, predio as pr

#TODO: clase obra - COMPLETAR SIGUIENDO ESQUEMA DE LAS CLASES YA HECHAS 

class Obra(BaseModel):
    
    id_obra = AutoField(primary_key=True)
    entorno = CharField(unique = True)
    nombre = CharField(unique = True)
    tipo_obra = ForeignKeyField(to.TipoObra)
    etapa_obra =ForeignKeyField(eo.EtapaObra)
    licitacion = ForeignKeyField(li.Licitacion)
    contratacion = ForeignKeyField(con.Contratacion)
    predio = ForeignKeyField(pr.Predio)
    direccion = CharField()
    lat = FloatField()
    long = FloatField()
    fecha_inicio = DateField()
    fecha_estimada_fin = DateField()
   

class Meta:
    db_table = 'obra'
    
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
    
   
    
