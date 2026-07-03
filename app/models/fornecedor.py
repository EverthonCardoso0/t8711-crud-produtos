class Fornecedor:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento):
        self._id = id
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cnpj
        self._sla_atendimento = sla_atendimento
    
    def validar_sla(self, sla):
        if sla < 0:
            raise ValueError("O SLA de atendimento não pode ser negativo.")

    def atualizar_dados(self, nova_razao_social, novo_nome_fantasia, novo_cnpj, novo_sla):
        self.validar_sla(novo_sla)
        self._razao_social = nova_razao_social
        self._nome_fantasia = novo_nome_fantasia
        self._cnpj = novo_cnpj
        self._sla_atendimento = novo_sla