from app.dao.dao import DAO
from app.models.perfil import Perfil


class Perfil_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)

    def save(self, perfil):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO PERFIL
                    (
                        NOME,
                        DESCRICAO
                    )
                    VALUES
                    (
                        %s,
                        %s
                    )
                  """

            cursor.execute(
                sql,
                (
                    perfil.nome,
                    perfil.descricao
                )
            )

            conexao.commit()

            perfil.id = cursor.lastrowid

            return perfil

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
                        NOME,
                        DESCRICAO
                    FROM
                        PERFIL
                    ORDER BY
                        NOME
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            perfis = []

            for registro in registros:

                perfis.append(

                    Perfil(
                        registro[0],
                        registro[1],
                        registro[2]
                    )

                )

            return perfis

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME,
                        DESCRICAO
                    FROM
                        PERFIL
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Perfil(
                registro[0],
                registro[1],
                registro[2]
            )

        finally:
            self.desconectar(cursor, conexao)

    def update(self, perfil):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    UPDATE PERFIL
                    SET
                        NOME = %s,
                        DESCRICAO = %s
                    WHERE
                        ID = %s
                  """

            cursor.execute(
                sql,
                (
                    perfil.nome,
                    perfil.descricao,
                    perfil.id
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
                    FROM PERFIL
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
