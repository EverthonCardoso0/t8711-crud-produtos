from app.dao.dao import DAO
from app.models.cliente import Cliente


class Cliente_DAO(DAO):

    def __init__(self, database, cidade_dao):
        super().__init__(database)
        self._cidade_dao = cidade_dao

    def save(self, cliente):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO CLIENTE
                    (
                        NOME,
                        DATA_NASCIMENTO,
                        LIMITE_CREDITO,
                        CIDADE_ID
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s
                    )
                  """

            cursor.execute(
                sql,
                (
                    cliente.nome,
                    cliente.data_nascimento,
                    cliente.limite_credito,
                    cliente.cidade.id
                )
            )

            conexao.commit()

            cliente.id = cursor.lastrowid

            return cliente

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
                        DATA_NASCIMENTO,
                        LIMITE_CREDITO,
                        CIDADE_ID
                    FROM
                        CLIENTE
                    ORDER BY
                        NOME
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            clientes = []

            for registro in registros:

                cidade = self._cidade_dao.get_by_id(
                    registro[4]
                )

                clientes.append(

                    Cliente(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        cidade
                    )

                )

            return clientes

        finally:

            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME,
                        DATA_NASCIMENTO,
                        LIMITE_CREDITO,
                        CIDADE_ID
                    FROM
                        CLIENTE
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            cidade = self._cidade_dao.get_by_id(
                registro[4]
            )

            return Cliente(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                cidade
            )

        finally:

            self.desconectar(cursor, conexao)

    def update(self, cliente):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    UPDATE CLIENTE
                    SET
                        NOME = %s,
                        DATA_NASCIMENTO = %s,
                        LIMITE_CREDITO = %s,
                        CIDADE_ID = %s
                    WHERE
                        ID = %s
                  """

            cursor.execute(
                sql,
                (
                    cliente.nome,
                    cliente.data_nascimento,
                    cliente.limite_credito,
                    cliente.cidade.id,
                    cliente.id
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
                    FROM CLIENTE
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