import tkinter as tk
from constantes import *
from Alerta import Mensagem
from Manipula_Excel import Excel


class TelaProdutoPesavel(tk.Toplevel):
    def __init__(self, master, pesarProduto):
        tk.Toplevel.__init__(self, master)
        self.main_frame = tk.Frame(
            self,
            bg=COR_FUNDO_SECUNDARIA,
            highlightthickness=2,
            highlightcolor=CINZA_CHUMBO
        )
        self.resizable(False, False)
        self.criaElementos()
        espacamentoSuperior = int(self.winfo_screenheight() * .25)
        espacamentoLadoEsquerdo = int(self.winfo_screenwidth() * .35)
        self.geometry(
            f"400x480+{espacamentoLadoEsquerdo}+{espacamentoSuperior}")
        self.overrideredirect(1)
        self.pesarProduto = pesarProduto
        self._produto = None
        self.bancoDeDados = Excel('inventario-loja.xlsx')
        self.bind('<Escape>', lambda e: self.destroy())
        self.main_frame.pack(expand=1, fill='both')

    def criaElementos(self):
        self.titulo = tk.Label(
            self.main_frame,
            text='Pesagem',
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO_PRIMARIA,
            font=ESTILO_FONT_MEDIA
        )

        self.labelCodigoProduto = tk.Label(
            self.main_frame,
            text='Codigo do produto',
            fg=COR_TEXTO_PRIMARIA,
            bg=COR_FUNDO_PRIMARIA,
            font=ESTILO_FONT_MEDIA
        )
        self.campoCodigoProduto = tk.Entry(
            self.main_frame,
            font=ESTILO_FONT_MEDIA
        )
        self.campoCodigoProduto.bind(
            '<Return>',
            lambda e: self.buscarProdutoPesavel()
        )
        self.campoCodigoProduto.focus()

        self.labelDescricao = tk.Label(
            self.main_frame,
            text='Descrição',
            fg=COR_TEXTO_PRIMARIA,
            bg=COR_FUNDO_PRIMARIA,
            font=ESTILO_FONT_MEDIA
        )
        self.descricao = tk.Label(
            self.main_frame,
            text='-',
            font=ESTILO_FONT_MEDIA
        )

        self.labelPreco = tk.Label(
            self.main_frame,
            text='Preço',
            fg=COR_TEXTO_PRIMARIA,
            bg=COR_FUNDO_PRIMARIA,
            font=ESTILO_FONT_MEDIA
        )
        self.preco = tk.Label(
            self.main_frame,
            text='-',
            font=ESTILO_FONT_MEDIA
        )

        self.labelPeso = tk.Label(
            self.main_frame,
            text='Peso',
            fg=COR_TEXTO_PRIMARIA,
            bg=COR_FUNDO_PRIMARIA,
            font=ESTILO_FONT_MEDIA
        )
        self.campoPeso = tk.Entry(
            self.main_frame,
            font=ESTILO_FONT_MEDIA
        )

        self.btnEnviar = tk.Button(
            self.main_frame,
            text='Enviar',
            fg=COR_TEXTO_PRIMARIA,
            bg=COR_FUNDO_PRIMARIA,
            font=ESTILO_FONT_PEQUENA,
            command=self.enviaParaTelaDeVendas
        )

        self.renderizaElementos()

    def buscarProdutoPesavel(self):
        codigo = self.campoCodigoProduto.get()
        self._produto = self.bancoDeDados.buscaProduto(codigo)
        if(self._produto != ""):
            self.descricao['text'] = self._produto.descricao
            self.preco['text'] = f'{self._produto.precoVenda}/Kg'
            self.campoPeso.focus()
        else:
            Mensagem(self, "Produto não encontrado")

    def enviaParaTelaDeVendas(self):
        peso = self.campoPeso.get()
        if(peso != ""):
            self._produto.quantidade = peso
            self.pesarProduto(self._produto)
            self.limparCampos()
            self.destroy()
        else:
            Mensagem(self, "Por favor digite o peso")

    def limparCampos(self):
        self.campoCodigoProduto.delete(0, 'end')
        self.campoPeso.delete(0, 'end')
        self.descricao['text'] = '-'
        self.preco['text'] = '-'

    def renderizaElementos(self):
        self.titulo.pack(fill='x', pady=10)
        self.labelCodigoProduto.pack(fill='x', padx=10)
        self.campoCodigoProduto.pack(fill='x', padx=10)
        self.labelDescricao.pack(fill='x', padx=10)
        self.descricao.pack(fill='x', padx=10)
        self.labelPreco.pack(fill='x', padx=10)
        self.preco.pack(fill='x', padx=10)
        self.labelPeso.pack(fill='x', padx=10)
        self.campoPeso.pack(fill='x', padx=10)
        self.btnEnviar.pack(fill='x', padx=30, pady=(40, 0))
