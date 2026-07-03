import os
from app.models.fornecedor import Fornecedor

class Fornecedor_Controller:
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
                    razao_social, nome_fantasia, cnpj, sla_atendimento = self.view.ler_dados_fornecedor()
                    fornecedor = Fornecedor(None,razao_social, nome_fantasia, cnpj, sla_atendimento)
                    self.dao.save(fornecedor)
                    self.view.exibir_mensagem("Fornecedor cadastrado com sucesso!")
                except ValueError:
                    self.view.exibir_mensagem("Erro: Entrada inválida. Tente novamente.", False)
                
            
            elif opcao == 2:
                fornecedores = self.dao.get_all()
                self.view.exibir_fornecedores(fornecedores)
                self.view.aguardar_entrada()
            
            elif opcao == 3:
                try:
                    fornecedores = self.dao.get_all()
                    self.view.exibir_fornecedores(fornecedores)
                    id_fornecedor = int(self.view.ler_id())
                    fornecedor_existente = self.dao.get_by_id(id_fornecedor)
                    if fornecedor_existente:
                        razao_social, nome_fantasia, cnpj, sla_atendimento = self.view.ler_dados_fornecedor()
                        fornecedor_existente.atualizar_dados(razao_social, nome_fantasia, cnpj, sla_atendimento)
                        self.dao.update(fornecedor_existente)
                        self.view.exibir_mensagem("Fornecedor atualizado com sucesso!")
                    else:
                        self.view.exibir_mensagem("Fornecedor não encontrado.", False) 
                except ValueError as e:
                    self.view.exibir_mensagem(f"Erro: {str(e)}", False)
                
            
            elif opcao == 4:
                try:
                    fornecedores = self.dao.get_all()
                    self.view.exibir_fornecedores(fornecedores)
                    id_fornecedor = int(self.view.ler_id())
                    sucesso = self.dao.delete(id_fornecedor)
                    if sucesso:
                        self.view.exibir_mensagem("Fornecedor excluído com sucesso!")
                    else:
                        self.view.exibir_mensagem("Fornecedor não encontrado.", False)
                except ValueError:
                    self.view.exibir_mensagem("Erro: ID inválido", False)
                
            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.", False)
                
