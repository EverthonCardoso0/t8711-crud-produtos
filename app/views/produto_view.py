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
        
    def ler_dados_produto(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE PRODUTO ===")
        nome = input("Digite o nome do produto: ")
        estoque = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço do produto: "))
        return nome, estoque, preco

    def ler_id(self):
        return input("Digite o ID do produto: ")
    
    def exibir_produtos(self, produtos):
        print(Fore.YELLOW + "\n--- TABELA DE PRODUTOS ---")
        if not produtos:
            print("Nenhum produto cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<20} | {'ESTOQUE':<7} | {'PREÇO':<10}")
        print("-"*50)
        for p in produtos:
            print(f"{p._id:<4} | {p._nome:<20} | {p._estoque:<7} | {p._preco:<10.2f}")
        print("-"*50)
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")


