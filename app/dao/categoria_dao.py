from app.dao.dao import DAO
from app.models.categoria import Categoria


class Categoria_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)

    def save(self, categoria):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO CATEGORIA
                    (
                        NOME
                    )
                    VALUES
                    (
                        %s
                    )
                  """

            cursor.execute(
                sql,
                (
                    categoria.nome,
                )
            )

            conexao.commit()

            categoria.id = cursor.lastrowid

            return categoria

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME
                    FROM
                        CATEGORIA
                    ORDER BY
                        NOME
                  """

            cursor.execute(sql)

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
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME
                    FROM
                        CATEGORIA
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Categoria(
                registro[0],
                registro[1]
            )

        finally:
            self.desconectar(cursor, conexao)

    def update(self, categoria):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    UPDATE CATEGORIA
                    SET
                        NOME = %s
                    WHERE
                        ID = %s
                  """

            cursor.execute(
                sql,
                (
                    categoria.nome,
                    categoria.id
                )
            )

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def delete(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    DELETE
                    FROM CATEGORIA
                    WHERE ID = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)
