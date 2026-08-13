class Idioma:

    ATUAL = "pt"

    TEXTOS = {
        "pt": {

            # Comuns a várias telas
            "comum.id": "ID",
            "comum.nome": "Nome",
            "comum.novo": "Novo",
            "comum.salvar": "Salvar",
            "comum.alterar": "Alterar",
            "comum.excluir": "Excluir",
            "comum.fechar": "Fechar",
            "comum.cancelar": "Cancelar",
            "comum.confirmacao": "Confirmação",
            "comum.erro_prefixo": "Erro: ",

            # Tela de Estados
            "estado.janela_titulo": "CRUD de Estados",
            "estado.titulo": "Cadastro de Estados",
            "estado.dados_frame": "Dados do estado",
            "estado.sigla": "Sigla",
            "estado.confirmar_exclusao": "Deseja realmente excluir este estado?",
            "estado.cadastrado_sucesso": "Estado cadastrado com sucesso!",
            "estado.atualizado_sucesso": "Estado atualizado com sucesso!",
            "estado.excluido_sucesso": "Estado excluído com sucesso!",
            "estado.nao_encontrado": "Estado não encontrado.",
            "estado.selecione_da_lista": "Selecione um estado na lista.",
            "estado.erro_ao_excluir": "Problemas ao excluir estado",
            "estado.erro_sigla_tamanho": "A sigla deve possuir exatamente 2 caracteres.",

            # Menu principal
            "menu.cadastros_basicos": "Cadastros básicos",
            "menu.estados": "Estados",
            "menu.cidades": "Cidades",
            "menu.acessos": "Acessos",
            "menu.usuarios": "Usuários",
            "menu.perfis": "Perfis",
            "menu.gestao_estoque": "Gestão de estoque",
            "menu.clientes": "Clientes",
            "menu.fornecedores": "Fornecedores",
            "menu.produtos": "Produtos",
            "menu.categorias": "Categorias",
            "menu.idioma": "Idioma",
            "menu.sair": "Sair",
        },
        "en": {

            # Common to several screens
            "comum.id": "ID",
            "comum.nome": "Name",
            "comum.novo": "New",
            "comum.salvar": "Save",
            "comum.alterar": "Edit",
            "comum.excluir": "Delete",
            "comum.fechar": "Close",
            "comum.cancelar": "Cancel",
            "comum.confirmacao": "Confirmation",
            "comum.erro_prefixo": "Error: ",

            # States screen
            "estado.janela_titulo": "State Management",
            "estado.titulo": "State Registration",
            "estado.dados_frame": "State data",
            "estado.sigla": "Abbreviation",
            "estado.confirmar_exclusao": "Do you really want to delete this state?",
            "estado.cadastrado_sucesso": "State registered successfully!",
            "estado.atualizado_sucesso": "State updated successfully!",
            "estado.excluido_sucesso": "State deleted successfully!",
            "estado.nao_encontrado": "State not found.",
            "estado.selecione_da_lista": "Select a state from the list.",
            "estado.erro_ao_excluir": "Problem deleting state",
            "estado.erro_sigla_tamanho": "The abbreviation must have exactly 2 characters.",

            # Main menu
            "menu.cadastros_basicos": "Basic registrations",
            "menu.estados": "States",
            "menu.cidades": "Cities",
            "menu.acessos": "Access",
            "menu.usuarios": "Users",
            "menu.perfis": "Roles",
            "menu.gestao_estoque": "Inventory management",
            "menu.clientes": "Customers",
            "menu.fornecedores": "Suppliers",
            "menu.produtos": "Products",
            "menu.categorias": "Categories",
            "menu.idioma": "Language",
            "menu.sair": "Exit",
        }
    }

    @classmethod
    def definir(cls, codigo):
        cls.ATUAL = codigo

    @classmethod
    def t(cls, chave):
        return cls.TEXTOS[cls.ATUAL].get(chave, chave)
