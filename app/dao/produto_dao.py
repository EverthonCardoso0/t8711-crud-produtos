from app.dao.dao import DAO
from app.models.produto import Produto
class Produto_DAO(DAO):
    def __init__(self, database):
        self._database = database

    def save(self, produto):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                    INSERT INTO PRODUTO
                    (NOME, ESTOQUE, PRECO)
                    VALUES (%s, %s, %s)
                """
        cursor.execute(sql, (
            produto.nome,
            produto.estoque,
            produto.preco
        ))
        conexao.commit()
        produto.id = cursor.lastrowid
        self._database.desconectar(cursor, conexao)
        return produto
    
    def get_all(self):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                    SELECT
                        ID,
                        NOME,
                        ESTOQUE,
                        PRECO
                    FROM
                        PRODUTO
                    ORDER BY 
                        NOME
                """
        cursor.execute(sql)
        registros = cursor.fetchall()
        produtos = []
        for registro in registros:
            produtos.append(
                Produto(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3]
                )
            )
        self._database.desconectar(cursor, conexao)
        return produtos
    
    def get_by_id(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                    SELECT
                        ID,
                        NOME,
                        ESTOQUE,
                        PRECO
                    FROM
                        PRODUTO
                    WHERE
                        ID = %s
                """        
        cursor.execute(sql,(id,))
        registro = cursor.fetchone()
        self._database.desconectar(cursor, conexao)
        if registro is None:
            return None
        return Produto(
            registro[0],
            registro[1],
            registro[2],
            registro[3]
        )


    def update(self, produto):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                    UPDATE PRODUTO SET
                        NOME    = %s,
                        ESTOQUE = %s,
                        PRECO   = %s
                    WHERE
                        ID = %s
                """
        cursor.execute(sql,(
                                produto.nome,
                                produto.estoque,
                                produto.preco,
                                produto.id
        ))
        conexao.commit()
        sucesso = cursor.rowcount > 0
        self._database.desconectar(cursor, conexao)
        return sucesso
    
    def delete(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                    DELETE FROM PRODUTO
                    WHERE ID = %s
                """
        cursor.execute(sql,(id,))
        conexao.commit()
        sucesso = cursor.rowcount > 0
        self._database.desconectar(cursor, conexao)
        return sucesso