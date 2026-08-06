import os
from app.models.estado import Estado


class Estado_Controller:

    def __init__(self, dao, view):
        self.dao = dao
        self.view = view

    def save(self):
        self.view.limpar_campos()

        try:

            nome, sigla = self.view.ler_dados_estado()

            estado = Estado(
                None,
                nome,
                sigla
            )

            self.dao.save(estado)

            self.view.exibir_mensagem(
                "Estado cadastrado com sucesso!"
            )

        except ValueError as e:

            self.view.exibir_mensagem(
                f"Erro: {str(e)}",
                False
            )

        except KeyboardInterrupt:

            self.view.exibir_mensagem(
                "Operação cancelada pelo usuário.",
                False
            )

    def get_all(self):

        estados = self.dao.get_all()

        self.view.exibir_estados(estados)

        self.view.aguardar_entrada()

    def update(self):

        try:

            estados = self.dao.get_all()

            self.view.exibir_estados(estados)

            id_estado = int(self.view.ler_id())

            estado_existente = self.dao.get_by_id(id_estado)

            if estado_existente is None:

                self.view.exibir_mensagem(
                    "Estado não encontrado.",
                    False
                )

                return

            nome, sigla = self.view.ler_dados_estado(
                estado_existente
            )

            estado_existente.atualizar_dados(
                nome,
                sigla
            )

            self.dao.update(estado_existente)

            self.view.exibir_mensagem(
                "Estado atualizado com sucesso!"
            )

        except ValueError as e:

            self.view.exibir_mensagem(
                f"Erro: {str(e)}",
                False
            )

    def delete(self):

        try:

            estados = self.dao.get_all()

            self.view.exibir_estados(estados)

            id_estado = int(self.view.ler_id())

            sucesso = self.dao.delete(id_estado)

            if sucesso:

                self.view.exibir_mensagem(
                    "Estado excluído com sucesso!"
                )

            else:

                self.view.exibir_mensagem(
                    "Estado não encontrado.",
                    False
                )

        except ValueError:

            self.view.exibir_mensagem(
                "Erro: ID inválido.",
                False
            )

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

                self.view.exibir_mensagem(
                    "Opção inválida.",
                    False
                )