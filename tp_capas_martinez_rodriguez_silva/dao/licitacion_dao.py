from dao import *
from models.licitacion import *

class LicitacionDao(BaseDao):
    def __init__(self):
        super().__init__(Licitacion)