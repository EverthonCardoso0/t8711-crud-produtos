from colorama import init, Fore, Style

init(autoreset=True)

class Fornecedor_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE FORNECEDORES (MVC) ==="
    
    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar fornecedor")
        print(f"2 - Listar fornecedores")
        print(f"3 - Atualizar fornecedor")
        print(f"4 - Excluir fornecedor")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def ler_dados_fornecedor(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE FORNECEDOR ===")
        razao_social = input("Digite a razão social: ")
        nome_fantasia = input("Digite o nome fantasia: ")
        cnpj = input("Digite o CNPJ: ")
        sla_atendimento = int(input("Digite o SLA de atendimento: "))
        return razao_social, nome_fantasia, cnpj, sla_atendimento

    def ler_id(self):
        return input("Digite o ID do fornecedor: ")
    
    def exibir_fornecedores(self, fornecedores):
        print(Fore.YELLOW + "\n--- TABELA DE FORNECEDORES ---")
        if not fornecedores:
            print("Nenhum fornecedor cadastrado")
            return
        print(f"{'ID':<4} | {'RAZÃO SOCIAL':<20} | {'NOME FANTASIA':<20} | {'CNPJ':<15} | {'SLA':<5}")
        print("-"*80)
        for p in fornecedores:
            print(f"{p._id:<4} | {p._razao_social:<20} | {p._nome_fantasia:<20} | {p._cnpj:<15} | {p._sla_atendimento:<5}")
        print("-"*80)
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")


