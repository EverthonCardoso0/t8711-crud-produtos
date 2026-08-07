import os
from app.models.fornecedor import Fornecedor

class Fornecedor_Controller:
    def __init__(self, dao, categoria_dao, fornecedor_categoria_dao, view):
        self.dao = dao
        self.categoria_dao = categoria_dao
        self.fornecedor_categoria_dao = fornecedor_categoria_dao
        self.view = view
        self.fornecedor_selecionado = None


    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            razao_social, nome_fantasia, cnpj, sla_atendimento = self.view.ler_dados_fornecedor()
            fornecedor = Fornecedor(
                    None,
                    razao_social, 
                    nome_fantasia, 
                    cnpj, 
                    sla_atendimento
                )
            self.dao.save(fornecedor)
            self.get_all()
            self.view.exibir_mensagem("Fornecedor cadastrado com sucesso!")
        except ValueError:
            self.view.exibir_mensagem("Erro: Entrada inválida. Tente novamente.", False)
        
    def get_all(self):
        fornecedores = self.dao.get_all()
        self.view.exibir_fornecedores(fornecedores)

    def selecionar_fornecedor(self, event):
        try:
            id_fornecedor = self.view.get_id_selecionado()
            self.fornecedor_selecionado = self.dao.get_by_id(
                id_fornecedor
            )
            self.view.preencher_campos(
                self.fornecedor_selecionado
            )

        except IndexError:
            pass        
    def update(self):
        try:
            if self.fornecedor_selecionado is None:
                self.view.exibir_mensagem("Selecione um fornecedor na lista.", False)
                return
            razao_social, nome_fantasia, cnpj, sla_atendimento = self.view.ler_dados_fornecedor()
            self.fornecedor_selecionado.atualizar_dados(razao_social, nome_fantasia, cnpj, sla_atendimento)
            self.dao.update(self.fornecedor_selecionado)
            self.get_all()
            self.view.exibir_mensagem("Fornecedor atualizado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem("Selecione um fornecedor na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.fornecedor_selecionado.id)
            if sucesso:
                self.fornecedor_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Fornecedor excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Fornecedor não encontrado.", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir fornecedor", False)

    def abrir_categorias(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem("Selecione um fornecedor na lista.", False)
            return
        categorias_disponiveis = self.categoria_dao.get_all()
        if not categorias_disponiveis:
            self.view.exibir_mensagem("Cadastre categorias antes de associá-las a um fornecedor.", False)
            return
        categorias_associadas = self.fornecedor_categoria_dao.get_categorias_por_fornecedor(
            self.fornecedor_selecionado.id
        )
        self.view.abrir_categorias(
            self.fornecedor_selecionado,
            categorias_disponiveis,
            categorias_associadas
        )

    def salvar_categorias(self, view_categorias, id_fornecedor, ids_categorias):
        try:
            self.fornecedor_categoria_dao.substituir_categorias_do_fornecedor(
                id_fornecedor,
                ids_categorias
            )
            view_categorias.exibir_mensagem("Categorias do fornecedor atualizadas com sucesso!")
            view_categorias.fechar()
        except Exception as e:
            view_categorias.exibir_mensagem("Não foi possível salvar as categorias do fornecedor.", False)

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
                
