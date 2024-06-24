from dao import *
from models.obra import *

class AreaResponsableDao(BaseDao):
    def __init__(self):
        super().__init__(Obra)