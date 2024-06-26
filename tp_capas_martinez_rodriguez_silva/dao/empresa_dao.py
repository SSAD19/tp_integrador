from dao.dao import *
from models.empresas import Empresa

class EmpresaDao(BaseDao):
    def __init__(self):
        super().__init__(Empresa)
        