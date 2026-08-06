from colorama import init, Fore, Style

init(autoreset=True)

class Produto_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE PRODUTOS (MVC) ==="
    
    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar produto")
        print(f"2 - Listar produtos")
        print(f"3 - Atualizar produto")
        print(f"4 - Excluir produto")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
    def ler_campo(self, rotulo, valor_atual=None):
        if valor_atual is not None:
            prompt = f"{rotulo} [{Fore.GREEN}{valor_atual}{Style.RESET_ALL}]: "
        else:
            prompt = f"{rotulo}: "
        valor = input(prompt)
        if valor == "" and valor_atual is not None:
            return valor_atual
        return valor

    def ler_dados_produto(self, produto_existente=None):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE PRODUTO ===")
        nome = self.ler_campo("Nome do produto", produto_existente.nome if produto_existente else None)
        estoque = int(self.ler_campo("Quantidade em estoque", str(produto_existente.estoque) if produto_existente else None))
        preco = float(self.ler_campo("Preço do produto", str(produto_existente.preco) if produto_existente else None))
        return nome, estoque, preco

    def ler_id(self):
        return input("Digite o ID do produto: ")
    
    def exibir_fornecedores(self, fornecedores):
        print(Fore.YELLOW + "\n--- FORNECEDORES DISPONÍVEIS ---")
        print(f"{'ID':<4} | {'NOME FANTASIA':<30}")
        print("-" * 40)
        for fornecedor in fornecedores:
            print(
                f"{fornecedor.id:<4} | {fornecedor.nome_fantasia:<30}"
            )
        print("-" * 40)
    
    def ler_fornecedor(self, fornecedor_existente = None):
        if fornecedor_existente is None:
            return input("Informe o ID do fornecedor: ")
        valor = input(
            f"Fornecedor [{Fore.GREEN}{fornecedor_existente}{Style.RESET_ALL}]: "
        )
        if valor == "":
            return fornecedor_existente
        return valor







    def exibir_produtos(self, produtos):
        print(Fore.YELLOW + "\n--- TABELA DE PRODUTOS ---")
        if not produtos:
            print("Nenhum produto cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<20} | {'ESTOQUE':<7} | {'PREÇO':<10} | {'VALOR EM ESTOQUE':<16} | {'FORNECEDOR':<30}")
        print("-"*99)
        for p in produtos:
            print(f"{p.id:<4} | {p.nome:<20} | {p.estoque:<7} | {p.preco:<10.2f} | {p.valor_estoque:<16.2f} | {p.fornecedor.nome_fantasia:<30}")
        print("-"*99)
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")


