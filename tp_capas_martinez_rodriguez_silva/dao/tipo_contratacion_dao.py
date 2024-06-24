from dao import *
from models.tipo_contratacion import *

class TipoContratacionDao(BaseDao):
    def __init__(self):
        super().__init__(TipoContratacion)