from colorama import init, Fore, Style

init(autoreset=True)


class Cidade_Terminal_View:

    def __init__(self):
        self.titulo_sistema = "=== CRUD DE CIDADES (MVC) ==="

    def renderizar_menu(self):

        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print("1 - Cadastrar cidade")
        print("2 - Listar cidades")
        print("3 - Atualizar cidade")
        print("4 - Excluir cidade")
        print("0 - Sair")
        print(Fore.CYAN + "=" * 60)

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

    def ler_dados_cidade(self, cidade_existente=None):

        print(Fore.CYAN + Style.BRIGHT + "=== DADOS DA CIDADE ===")

        nome = self.ler_campo(
            "Nome da cidade",
            cidade_existente.nome if cidade_existente else None
        )

        return nome

    def exibir_estados(self, estados):

        print(Fore.YELLOW + "\n--- ESTADOS DISPONÍVEIS ---")

        print(f"{'ID':<4} | {'SIGLA':<5} | {'NOME':<30}")

        print("-" * 50)

        for estado in estados:

            print(
                f"{estado.id:<4} | "
                f"{estado.sigla:<5} | "
                f"{estado.nome:<30}"
            )

        print("-" * 50)

    def ler_estado(self, estado_atual=None):

        if estado_atual is None:
            return input("Informe o ID do Estado: ")

        valor = input(
            f"Estado [{Fore.GREEN}{estado_atual}{Style.RESET_ALL}]: "
        )

        if valor == "":
            return estado_atual

        return valor

    def ler_id(self):

        return input("Digite o ID da cidade: ")

    def exibir_cidades(self, cidades):

        print(Fore.YELLOW + "\n--- TABELA DE CIDADES ---")

        if not cidades:
            print("Nenhuma cidade cadastrada.")
            return

        print(
            f"{'ID':<4} | "
            f"{'CIDADE':<25} | "
            f"{'UF':<4} | "
            f"{'ESTADO':<25}"
        )

        print("-" * 70)

        for cidade in cidades:

            print(
                f"{cidade.id:<4} | "
                f"{cidade.nome:<25} | "
                f"{cidade.estado.sigla:<4} | "
                f"{cidade.estado.nome:<25}"
            )

        print("-" * 70)

    def exibir_mensagem(self, mensagem, sucesso=True):

        cor = Fore.GREEN if sucesso else Fore.RED

        print(cor + f"\n[STATUS] {mensagem}\n")

        self.aguardar_entrada()

    def aguardar_entrada(self):

        input(Fore.WHITE + "Pressione Enter para continuar...")
