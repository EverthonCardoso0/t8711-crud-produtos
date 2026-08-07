from app.dao.dao import DAO
from app.models.cidade import Cidade


class Cidade_DAO(DAO):

    def __init__(self, database, estado_dao):
        super().__init__(database)
        self._estado_dao = estado_dao

    def save(self, cidade):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO CIDADE
                    (
                        NOME,
                        ESTADO_ID
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
                    cidade.nome,
                    cidade.estado.id
                )
            )

            conexao.commit()

            cidade.id = cursor.lastrowid

            return cidade

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
                        ESTADO_ID
                    FROM
                        CIDADE
                    ORDER BY
                        NOME
                  """
            cursor.execute(sql)

            registros = cursor.fetchall()
            cidades = []
            for registro in registros:
                estado = self._estado_dao.get_by_id(
                    registro[2]
                )
                cidades.append(
                    Cidade(
                        registro[0],
                        registro[1],
                        estado
                    )
                )
            return cidades

        finally:

            self.desconectar(cursor, conexao)

    def get_by_estado(self, id_estado):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        ESTADO_ID
                    FROM
                        CIDADE
                    WHERE
                        ESTADO_ID = %s
                    ORDER BY
                        NOME
                  """
            cursor.execute(
                sql,
                (id_estado,)
            )
            registros = cursor.fetchall()
            cidades = []
            for registro in registros:
                estado = self._estado_dao.get_by_id(
                    registro[2]
                )
                cidades.append(
                    Cidade(
                        registro[0],
                        registro[1],
                        estado
                    )
                )
            return cidades
        finally:

            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        ESTADO_ID
                    FROM
                        CIDADE
                    WHERE
                        ID = %s
                  """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

            if registro is None:
                return None
            
            estado = self._estado_dao.get_by_id(
                registro[2]
            )
            return Cidade(
                registro[0],
                registro[1],
                estado
            )

        finally:
            self.desconectar(cursor, conexao)

    def update(self, cidade):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    UPDATE CIDADE
                    SET
                        NOME = %s,
                        ESTADO_ID = %s
                    WHERE
                        ID = %s
                  """

            cursor.execute(
                sql,
                (
                    cidade.nome,
                    cidade.estado.id,
                    cidade.id
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
                    FROM CIDADE
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