from colorama import init
from app.core.database import Database

# Componentes de Produtos
from app.dao.produto_dao import Produto_DAO
from app.views.produto_view import Produto_View
from app.controllers.produto_controller import Produto_Controller

# Componentes de Categorias
from app.dao.categoria_dao import Categoria_DAO
from app.views.categoria_view import Categoria_View
from app.controllers.categoria_controller import Categoria_Controller

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
from app.views.usuario_view import Usuario_View
from app.controllers.usuario_controller import Usuario_Controller

# Componentes de Clientes
from app.dao.cliente_dao import Cliente_DAO
from app.views.cliente_view import Cliente_View
from app.controllers.cliente_controller import Cliente_Controller

import tkinter as tk


class ErpApplication:

    def __init__(self):

        init(autoreset=True)

        self._database = Database()

        self._root = tk.Tk()

        self._janela_estados = None
        self._janela_cidades = None
        self._janela_fornecedores = None
        self._janela_produtos = None
        self._janela_categorias = None
        self._janela_usuarios = None
        self._janela_clientes = None

        self._configurar_janela()

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
        # CATEGORIAS
        # ===========================

        self._dao_categorias = Categoria_DAO(
            self._database
        )

        self._ctrl_categorias = Categoria_Controller(
            dao=self._dao_categorias,
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
            view=None
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
            view=None
        )

        self._criar_menu()

    def _configurar_janela(self):
        self._root.title("Sistema Corporativo ERP")
        self._root.state("zoomed")

    def _criar_menu(self):

        menu_principal = tk.Menu(self._root)

        menu_cadastros_basicos = tk.Menu(menu_principal, tearoff=0)
        menu_cadastros_basicos.add_command(
            label="Estados",
            command=self._abrir_estados
        )
        menu_cadastros_basicos.add_command(
            label="Cidades",
            command=self._abrir_cidades
        )
        menu_principal.add_cascade(
            label="Cadastros básicos",
            menu=menu_cadastros_basicos
        )

        menu_acessos = tk.Menu(menu_principal, tearoff=0)
        menu_acessos.add_command(
            label="Usuários",
            command=self._abrir_usuarios
        )
        menu_principal.add_cascade(
            label="Acessos",
            menu=menu_acessos
        )

        menu_gestao_estoque = tk.Menu(menu_principal, tearoff=0)
        menu_gestao_estoque.add_command(
            label="Clientes",
            command=self._abrir_clientes
        )
        menu_gestao_estoque.add_command(
            label="Fornecedores",
            command=self._abrir_fornecedores
        )
        menu_gestao_estoque.add_command(
            label="Produtos",
            command=self._abrir_produtos
        )
        menu_gestao_estoque.add_command(
            label="Categorias",
            command=self._abrir_categorias
        )
        menu_principal.add_cascade(
            label="Gestão de estoque",
            menu=menu_gestao_estoque
        )

        menu_principal.add_command(
            label="Sair",
            command=self._root.destroy
        )

        self._root.config(menu=menu_principal)

    def _abrir_janela(self, atributo_janela, classe_view, controller):

        janela_existente = getattr(self, atributo_janela)

        if janela_existente is not None and janela_existente.winfo_exists():
            janela_existente.lift()
            janela_existente.focus_force()
            return

        janela = tk.Toplevel(self._root)
        setattr(self, atributo_janela, janela)

        controller.view = classe_view(janela, controller)
        controller.view.iniciar()

    def _abrir_estados(self):
        self._abrir_janela("_janela_estados", Estado_View, self._ctrl_estados)

    def _abrir_cidades(self):
        self._abrir_janela("_janela_cidades", Cidade_View, self._ctrl_cidades)

    def _abrir_fornecedores(self):
        self._abrir_janela("_janela_fornecedores", Fornecedor_View, self._ctrl_fornecedores)

    def _abrir_produtos(self):
        self._abrir_janela("_janela_produtos", Produto_View, self._ctrl_produtos)

    def _abrir_categorias(self):
        self._abrir_janela("_janela_categorias", Categoria_View, self._ctrl_categorias)

    def _abrir_usuarios(self):
        self._abrir_janela("_janela_usuarios", Usuario_View, self._ctrl_usuarios)

    def _abrir_clientes(self):
        self._abrir_janela("_janela_clientes", Cliente_View, self._ctrl_clientes)

    def run(self):
        self._root.mainloop()


if __name__ == "__main__":

    app = ErpApplication()

    app.run()
