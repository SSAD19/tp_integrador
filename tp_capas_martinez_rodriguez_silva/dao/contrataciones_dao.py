from dao import *
from models.contrataciones import *

class ContrataciondesDao(BaseDao):
    def __init__(self):
        super().__init__(Contratacion)
