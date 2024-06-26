from models.base_model import *

#TODO: clase EtapaObra - COMPLETAR SIGUIENDO ESQUEMA DE LAS CLASES YA HECHAS 

class EtapaObra(BaseModel):
    id_etapa_obra = AutoField(primary_key=True)
    nombre = CharField(unique = True, max_length=100)
    estado = BooleanField(default=True)

    class Meta:
        db_table= 'etapas_obra'