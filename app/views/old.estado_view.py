from colorama import init, Fore, Style

init(autoreset=True)


class Estado_Terminal_View:

    def __init__(self):
        self.titulo_sistema = "=== CRUD DE ESTADOS (MVC) ==="

    def renderizar_menu(self):

        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print("1 - Cadastrar estado")
        print("2 - Listar estados")
        print("3 - Atualizar estado")
        print("4 - Excluir estado")
        print("0 - Sair")
        print(Fore.CYAN + "=" * 50)

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

    def ler_dados_estado(self, estado_existente=None):

        print(Fore.CYAN + Style.BRIGHT + "=== DADOS DO ESTADO ===")

        nome = self.ler_campo(
            "Nome",
            estado_existente.nome if estado_existente else None
        )

        sigla = self.ler_campo(
            "Sigla",
            estado_existente.sigla if estado_existente else None
        )

        return nome, sigla

    def ler_id(self):

        return input("Digite o ID do estado: ")

    def exibir_estados(self, estados):

        print(Fore.YELLOW + "\n--- TABELA DE ESTADOS ---")

        if not estados:
            print("Nenhum estado cadastrado.")
            return

        print(f"{'ID':<5} | {'NOME':<30} | {'SIGLA':<5}")
        print("-" * 48)

        for estado in estados:

            print(
                f"{estado.id:<5} | "
                f"{estado.nome:<30} | "
                f"{estado.sigla:<5}"
            )

        print("-" * 48)

    def exibir_mensagem(self, mensagem, sucesso=True):

        cor = Fore.GREEN if sucesso else Fore.RED

        print(cor + f"\n[STATUS] {mensagem}\n")

        self.aguardar_entrada()

    def aguardar_entrada(self):

        input(Fore.WHITE + "Pressione Enter para continuar...")