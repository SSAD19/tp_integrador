from dao import *
from models.etapa_obra import *

class EtapaOnraDao(BaseDao):
    def __init__(self):
        super().__init__(EtapaObra)