class Fornecedor_DAO:
    def __init__(self):
        self.__fornecedores = []
        self.__novo_id = 1

    def save(self, fornecedor):
        fornecedor._id = self.__novo_id
        self.__fornecedores.append(fornecedor)
        self.__novo_id += 1
        return fornecedor

    def get_all(self):
        return list(self.__fornecedores)

    def get_by_id(self, id):
        for p in self.__fornecedores:
            if p._id == id:
                return p
        return None
    
    def delete(self, id):
        fornecedor = self.get_by_id(id)
        if fornecedor:
            self.__fornecedores.remove(fornecedor)
            return True
        return False
    
    def update(self, fornecedor_atualizado):
        return True