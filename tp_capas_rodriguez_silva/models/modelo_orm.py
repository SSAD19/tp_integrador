from datetime import date
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
        
class Comuna(BaseModel):
    id= AutoField(primary_key=True)
    nombre= CharField(unique = True)

class Predio(BaseModel):
    id = AutoField()
    barrio = CharField(unique = True)
    
    class Meta:
        db_table = 'predios'

class EtapaObra(BaseModel):
    id = AutoField(primary_key=True)
    nombre=CharField(unique=True)
    
    class Meta:
        db_table= 'etapas_obra'     
        

#Modelos con màs de un campo
class Empresa (BaseModel):
    id=AutoField(primary_key=True)
    razon_social = CharField(unique=True)
    activa = BooleanField(default=True) 
    
    class Meta:
        db_table = 'empresas'
        
class Contratacion(BaseModel): 
    id = AutoField(primary_key=True)
    nro_contratacion=CharField(null= True)
    tipo_contratacion=ForeignKeyField(TipoContratacion, null= True) 
    empresa=ForeignKeyField(Empresa, null= True)    
    mano_de_obra=IntegerField(null=True)
    monto=FloatField(null=True)
    
    class Meta:
        db_table = 'contrataciones'

class Licitacion(BaseModel):
    
    id= AutoField(primary_key = True)
    expediente = CharField()
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
    comuna = CharField(null=True)
    direccion = CharField(null= True)
    lat = FloatField(null= True)
    long = FloatField(null= True)
    fecha_inicio = DateField(null= True)
    fecha_estimada_fin = DateField(null= True)
    plazo_meses=DoubleField(null=True)
    porcentaje_avance=IntegerField(default=0)
    
    
    
   #Funciona
    @staticmethod
    def nuevo_proyecto(obra_data:dict):
        try:      
            nueva_obra = Obra.create(**obra_data) 
            return nueva_obra       
        except Exception as e:
            print('Error en nuevo_proyecto', e)
            return None
    
    #Funciona
    @staticmethod
    def iniciar_contratacion(data, id):
        #CREAR UNA CONTRATACION ENLAZANDO AL ID DE OBRA
          try:
            contratacion = Contratacion.create(**data)
            obra = Obra.get(Obra.id == id)
            obra.contratacion = contratacion
            obra.save()
          except Exception as e:
            print(e)
    
    #Funciona
    @staticmethod
    def adjudicar_obra(id, empresa:Empresa, monto:float):
        #CREAR O BUSCAR EMPRESA (?)
        try:
            obra = Obra.get(Obra.id == id)
            obra.contratacion.empresa = empresa
            obra.contratacion.monto = monto
            obra.contratacion.save()
            
        except Exception as e:
            print(e)
    
    #Funciona
    @staticmethod
    def iniciar_obra(id):
        #MODIFICAR LA ETAPA DE OBRA O CREAR CAMPO DE FECHA DE INICI
        try:
            obra = Obra.get(Obra.id==id)
            obra.etapa_obra = EtapaObra.get(EtapaObra.id == 5)
            obra.save()
        except Exception as e:
            print(e)
    
    #funciona
    @staticmethod
    def actualizar_porcentaje_avance(id, porcentaje:int):
        try: 
            obra = Obra.get(Obra.id==id)
            obra.porcentaje_avance = porcentaje
            obra.save()
            print(f'Porcentaje d eobra actualizada: {porcentaje}%')
        except Exception as e:
            print(e)
    
    #funciona
    @staticmethod    
    def incrementar_plazo(id, meses:int): 
        try: 
            obra =Obra.get(Obra.id==id)
            obra.plazo_meses = obra.plazo_meses + meses
            obra.save()
            print(f'Plazo de obra actualizado a: {obra.plazo_meses} meses totales')
        except Exception as e:
            print(e)
    
    @staticmethod
    def incrementar_mano_obra(id, num:int):
        # sumar num a la mano de obra que esta en clase contratacion 
        try: 
            obra= Obra.get(Obra.id==id)
            contratacion_act = Contratacion.get(Contratacion.id== obra.contratacion.id)
            contratacion_act.mano_de_obra = num
            contratacion_act.save()
        except Exception as e:
            print(e)
    
    def finalizar_obra(self):
        #actualizar etapa de obra
        try:
            self.etapa_obra = EtapaObra.get(EtapaObra.nombre == "Finalizado")
            self.save()
        except Exception as e:
            print(e)
    
    def rescindir_obra(self):
        try:
            self.etapa_obra = EtapaObra.get(EtapaObra.nombre == "rescindido")
            self.save()
        except Exception as e:
            print(e)
            
    class Meta:
        db_table = 'obra'
    
    

