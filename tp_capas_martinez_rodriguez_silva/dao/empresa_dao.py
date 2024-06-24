from tp_capas_martinez_rodriguez_silva.dao.dao import Dao
from tp_capas_martinez_rodriguez_silva.models.empresas import Empresa


class EmpresaDao(Dao):
    def __init__(self):
        super.__init__(Empresa)