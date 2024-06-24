from dao import *
from models.area_responsable import *

class AreaResponsableDao(BaseDao):
    def __init__(self):
        super().__init__(AreaResponsable)