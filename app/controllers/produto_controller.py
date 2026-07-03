import os
from app.models.produto import Produto

class Produto_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
    
    def inicializar_sistema(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.view.renderizar_menu()
            if opcao == 0:
                break
            elif opcao == 1:
                try:
                    nome, estoque, preco = self.view.ler_dados_produto()
                    produto = Produto(None,nome, estoque, preco)
                    self.dao.save(produto)
                    self.view.exibir_mensagem("Produto cadastrado com sucesso!")
                except ValueError:
                    self.view.exibir_mensagem("Erro: Entrada inválida. Tente novamente.", False)
                
            
            elif opcao == 2:
                produtos = self.dao.get_all()
                self.view.exibir_produtos(produtos)
                self.view.aguardar_entrada()
            
            elif opcao == 3:
                try:
                    produtos = self.dao.get_all()
                    self.view.exibir_produtos(produtos)
                    id_produto = int(self.view.ler_id())
                    produto_existente = self.dao.get_by_id(id_produto)
                    if produto_existente:
                        nome, estoque, preco = self.view.ler_dados_produto()
                        produto_existente.atualizar_dados(nome, estoque, preco)
                        self.dao.update(produto_existente)
                        self.view.exibir_mensagem("Produto atualizado com sucesso!")
                    else:
                        self.view.exibir_mensagem("Produto não encontrado.", False) 
                except ValueError as e:
                    self.view.exibir_mensagem(f"Erro: {str(e)}", False)
                
            
            elif opcao == 4:
                try:
                    produtos = self.dao.get_all()
                    self.view.exibir_produtos(produtos)
                    id_produto = int(self.view.ler_id())
                    sucesso = self.dao.delete(id_produto)
                    if sucesso:
                        self.view.exibir_mensagem("Produto excluído com sucesso!")
                    else:
                        self.view.exibir_mensagem("Produto não encontrado.", False)
                except ValueError:
                    self.view.exibir_mensagem("Erro: ID inválido", False)
                
            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.", False)
                
