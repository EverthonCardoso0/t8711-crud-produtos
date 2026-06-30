class Produto:
    def __init__(self, id_produto, nome, estoque, preco):
        self._id_produto = id_produto
        self._nome = nome  
        self._estoque = estoque
        self._preco = preco
    
    def atualizar_dados(self, novo_nome, novo_estoque, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if novo_estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self._nome = novo_nome
        self._estoque = novo_estoque
        self._preco = novo_preco
            
    