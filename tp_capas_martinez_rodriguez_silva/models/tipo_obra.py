from models.base_model import *

class TipoObra(BaseModel):
   
    id_tipo_obra = AutoField(primary_key=True)
    nombre = CharField()
    
    
    class Meta:
        db_table = 'tipos_obra'
