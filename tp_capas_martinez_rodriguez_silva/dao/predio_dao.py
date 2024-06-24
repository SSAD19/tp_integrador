from dao import *
from models.predio import *

class PredioDao(BaseDao):
    def __init__(self):
        super().__init__(Predio)
        
