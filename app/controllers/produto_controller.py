import os
from app.models.produto import Produto

class Produto_Controller:
    def __init__(self, dao, fornecedor_dao, view):
        self.dao = dao
        self.fornecedor_dao = fornecedor_dao
        self.view = view
        self.produto_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def carregar_fornecedores(self):
        fornecedores = self.fornecedor_dao.get_all()
        self.view.carregar_fornecedores(fornecedores)

    def save(self):
        try:
            nome, estoque, preco, fornecedor = self.view.ler_dados_produto()
            produto = Produto(None, nome, estoque, preco, fornecedor)
            self.dao.save(produto)
            self.get_all()
            self.view.exibir_mensagem("Produto cadastrado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def get_all(self):
        produtos = self.dao.get_all()
        self.view.exibir_produtos(produtos)

    def selecionar_produto(self, event):
        try:
            id_produto = self.view.get_id_selecionado()
            self.produto_selecionado = self.dao.get_by_id(
                id_produto
            )
            self.view.preencher_campos(
                self.produto_selecionado
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.produto_selecionado is None:
                self.view.exibir_mensagem("Selecione um produto na lista.", False)
                return
            nome, estoque, preco, fornecedor = self.view.ler_dados_produto()
            self.produto_selecionado.atualizar_dados(nome, estoque, preco, fornecedor)
            self.dao.update(self.produto_selecionado)
            self.get_all()
            self.view.exibir_mensagem("Produto atualizado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.produto_selecionado is None:
            self.view.exibir_mensagem("Selecione um produto na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.produto_selecionado.id)
            if sucesso:
                self.produto_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Produto excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Produto não encontrado.", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir produto", False)

    def inicializar_sistema(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.view.renderizar_menu()
            if opcao == 0:
                break
            elif opcao == 1:
                self.save()

            elif opcao == 2:
                self.get_all()

            elif opcao == 3:
                self.update()

            elif opcao == 4:
                self.delete()

            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.", False)
