from app.models.estado import Estado
from app.core.idioma import Idioma


class Estado_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.estado_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def save(self):

        try:
            nome, sigla = self.view.ler_dados_estado()
            estado = Estado(
                None,
                nome,
                sigla
            )
            self.dao.save(estado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("estado.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        estados = self.dao.get_all()
        self.view.exibir_estados(estados)

    def selecionar_estado(self, event):
        try:
            id_estado = self.view.get_id_selecionado()
            self.estado_selecionado = self.dao.get_by_id(
                id_estado
            )
            self.view.preencher_campos(
                self.estado_selecionado
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.estado_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("estado.selecione_da_lista"), False)
                return
            nome, sigla = self.view.ler_dados_estado()
            self.estado_selecionado.atualizar_dados(nome, sigla)
            self.dao.update(self.estado_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("estado.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.estado_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("estado.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.estado_selecionado.id)
            if sucesso:
                self.estado_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("estado.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("estado.nao_encontrado"), False)
        except Exception as e:
            self.view.exibir_mensagem(Idioma.t("estado.erro_ao_excluir"), False)
