import os
from app.models.fornecedor import Fornecedor

class Fornecedor_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view


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
                
import os
from colorama import init, Fore, Style
from app.core.database import Database

# Componentes de Produtos
from app.dao.produto_dao import Produto_DAO
from app.views.produto_view import Produto_View
from app.controllers.produto_controller import Produto_Controller

# Componentes de Estados
from app.dao.estado_dao import Estado_DAO
from app.views.estado_view import Estado_View
from app.controllers.estado_controller import Estado_Controller

# Componentes de Cidades
from app.dao.cidade_dao import Cidade_DAO
from app.views.cidade_view import Cidade_Terminal_View
from app.controllers.cidade_controller import Cidade_Controller

# Componentes de Fornecedores
from app.dao.fornecedor_dao import Fornecedor_DAO
from app.views.fornecedor_view import Fornecedor_View
from app.controllers.fornecedor_controller import Fornecedor_Controller

# Componentes de Usuários
from app.dao.usuario_dao import Usuario_DAO
from app.views.usuario_view import Usuario_Terminal_View
from app.controllers.usuario_controller import Usuario_Controller

# Componentes de Clientes
from app.dao.cliente_dao import Cliente_DAO
from app.views.cliente_view import Cliente_Terminal_View
from app.controllers.cliente_controller import Cliente_Controller

import tkinter as tk
class ErpApplication:

    def __init__(self):

        init(autoreset=True)

        self._database = Database()

        # ===========================
        # ESTADOS
        # ===========================

        self._dao_estados = Estado_DAO(
            self._database
        )

        self._ctrl_estados = Estado_Controller(
            dao=self._dao_estados,
            view=Estado_View()
        )

        # ===========================
        # CIDADES
        # ===========================

        self._dao_cidades = Cidade_DAO(
            self._database,
            self._dao_estados
        )

        self._ctrl_cidades = Cidade_Controller(
            dao=self._dao_cidades,
            estado_dao=self._dao_estados,
            view=Cidade_Terminal_View()
        )

        # ===========================
        # FORNECEDORES
        # ===========================

        self._dao_fornecedores = Fornecedor_DAO(
            self._database
        )

        self._ctrl_fornecedores = Fornecedor_Controller(
            dao=self._dao_fornecedores,
            view=None
        )



        # ===========================
        # PRODUTOS
        # ===========================

        self._dao_produtos = Produto_DAO(
            self._database,
            self._dao_fornecedores
        )

        self._ctrl_produtos = Produto_Controller(
            dao=self._dao_produtos,
            fornecedor_dao=self._dao_fornecedores,
            view=Produto_View()
        )

        # ===========================
        # USUÁRIOS
        # ===========================

        self._dao_usuarios = Usuario_DAO(
            self._database,
            self._dao_cidades
        )

        self._ctrl_usuarios = Usuario_Controller(
            dao=self._dao_usuarios,
            cidade_dao=self._dao_cidades,
            estado_dao=self._dao_estados,
            view=Usuario_Terminal_View()
        )

        # ===========================
        # CLIENTES
        # ===========================

        self._dao_clientes = Cliente_DAO(
            self._database,
            self._dao_cidades
        )

        self._ctrl_clientes = Cliente_Controller(
            dao=self._dao_clientes,
            cidade_dao=self._dao_cidades,
            estado_dao=self._dao_estados,
            view=Cliente_Terminal_View()
        )

    def _renderizar_menu_principal(self):

        os.system("cls" if os.name == "nt" else "clear")

        print(Fore.GREEN + Style.BRIGHT + "=== SISTEMA CORPORATIVO ERP ===")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Fornecedores")
        print("3 - Gerenciar Usuários")
        print("4 - Gerenciar Clientes")
        print("5 - Gerenciar Estados")
        print("6 - Gerenciar Cidades")
        print("0 - Sair do Sistema")
        print(Fore.GREEN + "=" * 34)

        try:
            return int(input("Escolha o módulo: "))
        except ValueError:
            return -1

    def run(self):
        
          
        while True:

            opcao = self._renderizar_menu_principal()

            if opcao == 0:

                print("\nEncerrando sistema corporativo...")
                break

            elif opcao == 1:

                self._ctrl_produtos.inicializar_sistema()

            elif opcao == 2:
                janela_fornecedores = tk.Tk()
                self._ctrl_fornecedores.view = Fornecedor_View(
                    janela_fornecedores,
                    self._ctrl_fornecedores
                )                
                self._ctrl_fornecedores.view.iniciar()
                

            elif opcao == 3:

                self._ctrl_usuarios.inicializar_sistema()

            elif opcao == 4:

                self._ctrl_clientes.inicializar_sistema()

            elif opcao == 5:

                self._ctrl_estados.inicializar_sistema()

            elif opcao == 6:

                self._ctrl_cidades.inicializar_sistema()

            else:

                print(Fore.RED + "\nOpção inválida!")

                input(
                    Fore.WHITE +
                    "Pressione Enter para continuar..."
                )
    

if __name__ == "__main__":

    app = ErpApplication()

    app.run()