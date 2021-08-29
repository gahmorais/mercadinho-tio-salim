import tkinter as tk
from PIL import ImageTk, Image
from constantes import *
from tkinter import ttk
from Alerta import ProdutoNaoEncontrado
from Manipula_Excel import Excel


class TelaDeConsulta(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.main_frame = tk.Frame(self, bg=COR_FUNDO_SECUNDARIA)
        self.attributes('-fullscreen', True)
        self.criaElementos()
        self.planilha = Excel('inventario-loja.xlsx')
        self.main_frame.pack(expand=1, fill='both')

    def criaElementos(self):
        self.frameBarraDeTitulo = tk.Frame(self.main_frame, bg=COR_FUNDO_PRIMARIA)
        self.framePrincipal = tk.Frame(self.main_frame, bg=COR_FUNDO_SECUNDARIA)
        self.frameBuscaProduto = tk.Frame(self.main_frame, bg=COR_FUNDO_SECUNDARIA)
        self.frameCodigo = tk.Frame(
            self.framePrincipal, bg=COR_FUNDO_SECUNDARIA)
        self.frameDescricao = tk.Frame(
            self.framePrincipal, bg=COR_FUNDO_SECUNDARIA)
        self.frameQuantidade = tk.Frame(
            self.framePrincipal, bg=COR_FUNDO_SECUNDARIA)
        self.framePreco = tk.Frame(
            self.framePrincipal, bg=COR_FUNDO_SECUNDARIA)

        self.titulo = tk.Label(
            self.frameBarraDeTitulo,
            text=f'{ESTABELECIMENTO}',
            font=ESTILO_FONT_TELA_PRINCIPAL_MEDIA,
            bg=COR_FUNDO_TITULO,
            fg=COR_TEXTO_PRIMARIA,
        )

        self.iconeFecharJanela = tk.Button(
            self.frameBarraDeTitulo,
            border=1,
            text='X',
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            command=self.destroy
        )

        self.labelBuscaProduto = tk.Label(
            self.frameBuscaProduto,
            font=ESTILO_FONT_MEDIA,
            fg=COR_TEXTO_PRIMARIA,
            bg=COR_FUNDO_SECUNDARIA,
            text='Insira o código do produto',
            padx=10
        )
        self.campoBuscaProduto = tk.Entry(
            self.frameBuscaProduto,
            font=ESTILO_FONT_MEDIA
        )

        self.labelCodigo = tk.Label(
            self.frameCodigo,
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            text='Codigo'
        )

        self.codigo = tk.Label(
            self.frameCodigo,
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_SECUNDARIA,
            text='-',
            fg=COR_TEXTO_PRIMARIA,
        )

        self.descricao = tk.Label(
            self.frameDescricao,
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_SECUNDARIA,
            text='-',
            fg=COR_TEXTO_PRIMARIA,
        )

        self.quantidade = tk.Label(
            self.frameQuantidade,
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_SECUNDARIA,
            text='-',
            fg=COR_TEXTO_PRIMARIA,
        )

        self.preco = tk.Label(
            self.framePreco,
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_SECUNDARIA,
            text='-',
            fg=COR_TEXTO_PRIMARIA,
        )

        self.labelDescricao = tk.Label(
            self.frameDescricao,
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            text='Descrição'
        )

        self.labelQuantidade = tk.Label(
            self.frameQuantidade,
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            text='Quantidade'
        )

        self.labelPreco = tk.Label(
            self.framePreco,
            font=ESTILO_FONT_MEDIA,
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            text='Preço'
        )

        self.campoBuscaProduto.bind(
            '<Return>',
            lambda e: self.buscaProduto(
                self.campoBuscaProduto.get()
            )
        )

        self.renderizaElementos()

    def buscaProduto(self, codigoProduto):
        produto = self.planilha.buscaProduto(codigoProduto)
        if(produto != ""):
            self.codigo['text'] = produto.codigo
            self.descricao['text'] = produto.descricao
            self.quantidade['text'] = produto.quantidade
            self.preco['text'] = f'R$ {produto.precoVenda}'
        else:
            ProdutoNaoEncontrado()

    def renderizaElementos(self):
        self.frameBarraDeTitulo.pack(fill='x')
        self.frameBuscaProduto.pack(pady=30)
        self.labelBuscaProduto.pack(padx=20, side='left')
        self.campoBuscaProduto.pack(side='right')
        self.framePrincipal.pack(pady=30)
        self.frameCodigo.pack(side='left', padx=30)
        self.frameDescricao.pack(side='left', padx=30)
        self.frameQuantidade.pack(side='left', padx=30)
        self.framePreco.pack(side='left', padx=30)
        self.titulo.pack(expand=1, side='left')
        self.iconeFecharJanela.pack(fill='y', side='right')

        self.labelCodigo.pack()
        self.codigo.pack()

        self.labelDescricao.pack()
        self.descricao.pack()

        self.labelQuantidade.pack()
        self.quantidade.pack()

        self.labelPreco.pack()
        self.preco.pack()

    def mostraBind(self):
        print('bind')
