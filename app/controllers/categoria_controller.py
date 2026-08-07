from app.models.categoria import Categoria


class Categoria_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.categoria_selecionada = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome = self.view.ler_dados_categoria()
            categoria = Categoria(
                None,
                nome
            )
            self.dao.save(categoria)
            self.get_all()
            self.view.exibir_mensagem("Categoria cadastrada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def get_all(self):
        categorias = self.dao.get_all()
        self.view.exibir_categorias(categorias)

    def selecionar_categoria(self, event):
        try:
            id_categoria = self.view.get_id_selecionado()
            self.categoria_selecionada = self.dao.get_by_id(
                id_categoria
            )
            self.view.preencher_campos(
                self.categoria_selecionada
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.categoria_selecionada is None:
                self.view.exibir_mensagem("Selecione uma categoria na lista.", False)
                return
            nome = self.view.ler_dados_categoria()
            self.categoria_selecionada.atualizar_dados(nome)
            self.dao.update(self.categoria_selecionada)
            self.get_all()
            self.view.exibir_mensagem("Categoria atualizada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.categoria_selecionada is None:
            self.view.exibir_mensagem("Selecione uma categoria na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.categoria_selecionada.id)
            if sucesso:
                self.categoria_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Categoria excluída com sucesso!")
            else:
                self.view.exibir_mensagem("Categoria não encontrada.", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir categoria", False)
