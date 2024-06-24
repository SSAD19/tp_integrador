from dao import *
from models.tipo_obra import *

class TipoObraDao(BaseDao):
    def __init__(self):
        super().__init__(TipoObra)