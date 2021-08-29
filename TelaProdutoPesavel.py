import tkinter as tk
from Alerta import ProdutoNaoEncontrado
from Manipula_Excel import Excel


class TelaProdutoPesavel(tk.Toplevel):
    def __init__(self, master, pesarProduto):
        tk.Toplevel.__init__(self, master)
        self.main_frame = tk.Frame(self)
        self.criaElementos()
        self.pesarProduto = pesarProduto
        self._produto = None
        self.bancoDeDados = Excel('inventario-loja.xlsx')
        self.main_frame.pack(expand=1, fill='both')

    def criaElementos(self):
        self.labelPeso = tk.Label(self.main_frame, text='Peso')
        self.campoPeso = tk.Entry(self.main_frame)

        self.labelDescricao = tk.Label(self.main_frame, text='Descrição')
        self.descricao = tk.Label(self.main_frame, text='-')

        self.labelPreco = tk.Label(self.main_frame, text='Preço')
        self.preco = tk.Label(self.main_frame, text='-')

        self.btnPesar = tk.Button(
            self.main_frame,
            text='Enviar',
            command=self.enviaParaTelaDeVendas
        )

        self.labelCodigoProduto = tk.Label(
            self.main_frame,
            text='Codigo do produto'
        )
        self.campoCodigoProduto = tk.Entry(self.main_frame)
        self.campoCodigoProduto.bind(
            '<Return>',
            lambda e: self.buscarProdutoPesavel()
        )
        self.renderizaElementos()

    def buscarProdutoPesavel(self):
        codigo = self.campoCodigoProduto.get()
        self._produto = self.bancoDeDados.buscaProduto(codigo)
        if(self._produto != ""):
            self.descricao['text'] = self._produto.descricao
            self.preco['text'] = f'{self._produto.precoVenda}/Kg'
        else:
            ProdutoNaoEncontrado(self)

    def enviaParaTelaDeVendas(self):
        peso = self.campoPeso.get()
        if(peso != ""):
            self._produto.quantidade = peso
            self.pesarProduto(self._produto)
            self.limparCampos()
            self.destroy()
        else:
            print('Por favor digite o peso')
    def limparCampos(self):
        self.campoCodigoProduto.delete(0,'end')
        self.campoPeso.delete(0,'end')
        self.descricao['text'] = '-'
        self.preco['text'] = '-'

    def renderizaElementos(self):
        self.labelCodigoProduto.pack()
        self.campoCodigoProduto.pack()
        self.labelDescricao.pack()
        self.descricao.pack()
        self.labelPreco.pack()
        self.preco.pack()
        self.labelPeso.pack()
        self.campoPeso.pack()
        self.btnPesar.pack()
