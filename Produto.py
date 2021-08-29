class Produto:
    def __init__(self, codigo, descricao, precoCompra, precoVenda, quantidade, pesavel=False):
        self.codigo = codigo
        self.descricao = descricao
        self.precoCompra = precoCompra
        self.precoVenda = precoVenda
        self.quantidade = quantidade
        self.pesavel = pesavel

        