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
    def ler_campo(self, rotulo, valor_atual=None):
        if valor_atual is not None:
            prompt = f"{rotulo} [{Fore.GREEN}{valor_atual}{Style.RESET_ALL}]: "
        else:
            prompt = f"{rotulo}: "
        valor = input(prompt)
        if valor == "" and valor_atual is not None:
            return valor_atual
        return valor  
            
    def ler_dados_fornecedor(self, fornecedor_existente=None):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE FORNECEDOR ===")
        razao_social = self.ler_campo("Razão social", fornecedor_existente.razao_social if fornecedor_existente else None)
        nome_fantasia = self.ler_campo("Nome fantasia", fornecedor_existente.nome_fantasia if fornecedor_existente else None)
        cnpj = self.ler_campo("CNPJ", fornecedor_existente.cnpj if fornecedor_existente else None)
        sla_atendimento = int(self.ler_campo("SLA de atendimento", str(fornecedor_existente.sla_atendimento) if fornecedor_existente else None))
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
            print(f"{p.id:<4} | {p.razao_social:<20} | {p.nome_fantasia:<20} | {p.cnpj:<15} | {p.sla_atendimento:<5}")
        print("-"*80)
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")


