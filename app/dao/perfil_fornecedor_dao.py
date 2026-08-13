from app.models.fornecedor import Fornecedor


class Perfil_Fornecedor_DAO:

    def __init__(self, database):
        self._database = database

    def get_fornecedores_por_perfil(self, perfil):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:

            sql = """
                    SELECT
                        F.ID,
                        F.RAZAO_SOCIAL,
                        F.NOME_FANTASIA,
                        F.CNPJ,
                        F.SLA_ATENDIMENTO
                    FROM
                        FORNECEDOR F
                    INNER JOIN
                        PERFIL_FORNECEDOR PF
                        ON PF.ID_FORNECEDOR = F.ID
                    WHERE
                        PF.ID_PERFIL = %s
                    ORDER BY
                        F.NOME_FANTASIA
                  """

            cursor.execute(sql, (perfil.id,))

            registros = cursor.fetchall()

            fornecedores = []

            for registro in registros:

                fornecedores.append(
                    Fornecedor(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        registro[4]
                    )
                )

            return fornecedores

        finally:
            self._database.desconectar(cursor, conexao)

    def substituir_fornecedores_do_perfil(self, perfil, fornecedores):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:

            cursor.execute(
                """
                    DELETE FROM PERFIL_FORNECEDOR
                    WHERE ID_PERFIL = %s
                """,
                (perfil.id,)
            )

            for fornecedor in fornecedores:

                cursor.execute(
                    """
                        INSERT INTO PERFIL_FORNECEDOR
                        (
                            ID_PERFIL,
                            ID_FORNECEDOR
                        )
                        VALUES
                        (
                            %s,
                            %s
                        )
                    """,
                    (perfil.id, fornecedor.id)
                )

            conexao.commit()

        except Exception:
            conexao.rollback()
            raise

        finally:
            self._database.desconectar(cursor, conexao)
