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
from app.views.cidade_view import Cidade_View
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
            view=None
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
            view=None
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
            view=None
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
                janela_produtos = tk.Tk()
                self._ctrl_produtos.view = Produto_View(
                    janela_produtos,
                    self._ctrl_produtos
                )
                self._ctrl_produtos.view.iniciar()

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
                janela_estados = tk.Tk()
                self._ctrl_estados.view = Estado_View(
                    janela_estados,
                    self._ctrl_estados
                )
                self._ctrl_estados.view.iniciar()

            elif opcao == 6:
                janela_cidades = tk.Tk()
                self._ctrl_cidades.view = Cidade_View(
                    janela_cidades,
                    self._ctrl_cidades
                )
                self._ctrl_cidades.view.iniciar()

            else:

                print(Fore.RED + "\nOpção inválida!")

                input(
                    Fore.WHITE +
                    "Pressione Enter para continuar..."
                )
    

if __name__ == "__main__":

    app = ErpApplication()

    app.run()