from app.models.categoria import Categoria


class Fornecedor_Categoria_DAO:

    def __init__(self, database):
        self._database = database

    def get_categorias_por_fornecedor(self, id_fornecedor):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:

            sql = """
                    SELECT
                        C.ID,
                        C.NOME
                    FROM
                        CATEGORIA C
                    INNER JOIN
                        FORNECEDOR_CATEGORIA FC
                        ON FC.ID_CATEGORIA = C.ID
                    WHERE
                        FC.ID_FORNECEDOR = %s
                    ORDER BY
                        C.NOME
                  """

            cursor.execute(sql, (id_fornecedor,))

            registros = cursor.fetchall()

            categorias = []

            for registro in registros:

                categorias.append(
                    Categoria(
                        registro[0],
                        registro[1]
                    )
                )

            return categorias

        finally:
            self._database.desconectar(cursor, conexao)

    def substituir_categorias_do_fornecedor(self, id_fornecedor, ids_categorias):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:

            cursor.execute(
                """
                    DELETE FROM FORNECEDOR_CATEGORIA
                    WHERE ID_FORNECEDOR = %s
                """,
                (id_fornecedor,)
            )

            for id_categoria in ids_categorias:

                cursor.execute(
                    """
                        INSERT INTO FORNECEDOR_CATEGORIA
                        (
                            ID_FORNECEDOR,
                            ID_CATEGORIA
                        )
                        VALUES
                        (
                            %s,
                            %s
                        )
                    """,
                    (id_fornecedor, id_categoria)
                )

            conexao.commit()

        except Exception:
            conexao.rollback()
            raise

        finally:
            self._database.desconectar(cursor, conexao)
