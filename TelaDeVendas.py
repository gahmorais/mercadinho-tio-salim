import tkinter as tk
from PIL import ImageTk, Image
from constantes import *
from tkinter import ttk
from Alerta import ProdutoNaoEncontrado
from Manipula_Excel import Excel


class TelaDeVendas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.criaElementos()
        self.planilha = Excel('inventario-loja.xlsx')
        self.count = 1
        self.total = 0
        

    def criaElementos(self):
        self.campos = tk.Frame(self.master, bg=COR_SECUNDARIA)
        self.produtos = tk.Frame(self.master, bg=COR_SECUNDARIA)
        self.frameValorTotal = tk.Frame(self.produtos)
        self.frameQuantidade = tk.Frame(self.campos)

        self._tamanhoDaTela = root.winfo_screenheight()
        if(self._tamanhoDaTela < 900):
            self.TAMANHO_DA_IMAGEM = IMAGEM_PEQUENA
        else:
            self.TAMANHO_DA_IMAGEM = IMAGEM_GRANDE

        self.logo = tk.Canvas(
            self.campos, bg=COR_SECUNDARIA, highlightthickness=0)

        self.titulo = tk.Label(
            self.master,
            text=ESTABELECIMENTO,
            font=ESTILO_FONT_GRANDE,
            bg=COR_FUNDO_TITULO,
            fg=COR_TEXTO_PRIMARIA
        )

        self.labelCampoCodigoProduto = tk.Label(
            self.campos,
            text="Digite o código do produto: ",
            font=(ESTILO_FONT_MEDIA),
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA
        )
        self.campoCodigoProduto = tk.Entry(
            self.campos,
            font=(ESTILO_FONT_MEDIA)
        )

        self.labelCampoQuantidade = tk.Label(
            self.frameQuantidade,
            text="Digite a quantidade",
            font=(ESTILO_FONT_MEDIA),
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA
        )
        self.campoQuantidade = tk.Entry(
            self.frameQuantidade,
            font=(ESTILO_FONT_MEDIA)
        )

        self.labelExcluirProduto = tk.Label(
            self.campos,
            text="Digite o código do produto a ser excluído",
            font=(ESTILO_FONT_MEDIA),
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA
        )
        self.campoExcluirProduto = tk.Entry(
            self.campos,
            font=(ESTILO_FONT_MEDIA)
        )

        self.frameTabela = tk.Frame(self.produtos, bg='gray')

        self.campoCodigoProduto.bind(
            '<Return>',
            lambda e: self.adicionaLinha(
                self.campoCodigoProduto.get(),
                self.campoQuantidade.get()
            )
        )

        self.campoQuantidade.bind(
            '<Return>',
            lambda e: self.adicionaLinha(
                self.campoCodigoProduto.get(),
                self.campoQuantidade.get()
            )
        )

        self.campoExcluirProduto.bind(
            '<Return>',
            lambda e: self.removeLinha(self.campoExcluirProduto.get())
        )

        self.btnExcluirProduto = tk.Button(
            self.campos,
            text="Excluir produto",
            command=lambda: self.removeLinha(self.campoExcluirProduto.get()),
            font=(ESTILO_FONT_MEDIA),
        )

        self.btnFinalizaCompra = tk.Button(
            self.campos,
            text="Finalizar",
            command=self.finalizaCompra,
            font=('Arial Black', 25),
            bg=COR_FUNDO_TITULO,
            fg='#fff'
        )

        self.btnBuscarProduto = tk.Button(
            self.campos,
            text="Buscar",
            command=lambda: self.adicionaLinha(
                self.campoCodigoProduto.get(),
                self.campoQuantidade.get()),
            font=(ESTILO_FONT_MEDIA)
        )

        self.labelValorTotal = tk.Label(
            self.frameValorTotal,
            text="Total: ",
            bg=COR_SECUNDARIA,
            fg='#fff',
            font=(ESTILO_FONT_GRANDE),
        )
        self.campoValorTotal = tk.Label(
            self.frameValorTotal,
            bg='#fff',
            width=14,
            font=(ESTILO_FONT_GRANDE)
        )

        self.criaTabela()
        self.renderizaElementos()

    def criaTabela(self):
        self.conteudoTabela = ttk.Treeview(self.frameTabela)
        self.conteudoTabela.bind(
            '<Delete>',
            lambda e: self.removeLinha(self.campoCodigoProduto.get())
        )

        self.conteudoTabela['columns'] = (
            'Código',
            'Descricao',
            'Quantidade',
            'Preço'
        )

        style = ttk.Style()
        style.configure('Treeview.Heading', font=ESTILO_FONT_PEQUENA)

        self.conteudoTabela.column('#0', width=0, stretch='NO')
        self.conteudoTabela.column(
            'Código',
            anchor='center',
            minwidth=100,
            width=100
        )
        self.conteudoTabela.column(
            'Descricao',
            anchor='center',
            minwidth=200,
            width=200
        )
        self.conteudoTabela.column(
            'Quantidade',
            anchor='center',
            minwidth=80,
            width=80
        )
        self.conteudoTabela.column(
            'Preço',
            anchor='center',
            minwidth=80,
            width=80
        )

        self.conteudoTabela.heading(
            '#0',
            text='',
            anchor='center'
        )
        self.conteudoTabela.heading(
            'Código',
            text='Código',
            anchor='center'
        )
        self.conteudoTabela.heading(
            'Descricao',
            text='Descricao',
            anchor='center'
        )
        self.conteudoTabela.heading(
            'Quantidade',
            text='Quantidade',
            anchor='center'
        )
        self.conteudoTabela.heading(
            'Preço',
            text='Preço',
            anchor='center'
        )

    def renderizaElementos(self):
        self.titulo.pack(fill='x')

        self.campos.pack(
            side='right',
            expand=1,
            fill='both',
            padx=40,
            pady=40
        )

        self.produtos.pack(
            side='left',
            expand=1,
            fill='both',
            padx=40,
            pady=40
        )

        self.labelCampoCodigoProduto.pack(fill='x')
        self.campoCodigoProduto.pack(fill='x')
        self.frameQuantidade.pack(fill='x', pady=40)

        self.labelCampoQuantidade.pack(fill='x')
        self.campoQuantidade.pack(fill='x')

        self.campoQuantidade.insert(0, "1")

        self.labelExcluirProduto.pack(fill='x')
        self.campoExcluirProduto.pack(fill='x')

        # self.btnBuscarProduto.pack(fill='x')
        # self.btnExcluirProduto.pack(fill='x')

        self.frameTabela.pack(expand=1, fill='both')
        self.conteudoTabela.pack(expand=1, fill='both')

        self.frameValorTotal.pack(side='right', pady=10)
        self.labelValorTotal.pack(side='left')
        self.campoValorTotal.pack(side='right')

        self.btnFinalizaCompra.pack(fill='x', pady=40)
        self.logo.pack(expand=1, fill='both')
        cartImage = Image.open("grocery-cart.png")

        print(self.TAMANHO_DA_IMAGEM)
        cartImage = cartImage.resize(self.TAMANHO_DA_IMAGEM, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(cartImage)
        self.logo.create_image(200, 0, anchor='nw', image=self.image)

    def adicionaLinha(self, codigoProduto, quantidade=1):
        produto = self.planilha.buscaProduto(codigoProduto)
        if(produto != ""):

            id = self.count
            self.conteudoTabela.insert(parent='', index=id, iid=id, text='', values=(
                produto.codigo,
                produto.descricao,
                quantidade,
                produto.precoVenda
            ))

            self.count += 1
            self.total = 0

            children = self.conteudoTabela.get_children()
            for child in children:
                valor = float(self.conteudoTabela.item(
                    child, 'values')[3].replace(",", "."))
                quantidade = int(self.conteudoTabela.item(child, 'values')[2])
                self.total += valor*quantidade

            totalFormatado = "{:.2f}".format(self.total)
            self.campoValorTotal['text'] = f"R$ {totalFormatado}"
            self.campoCodigoProduto.delete(0, 'end')
            self.campoQuantidade.delete(0, 'end')
            self.campoQuantidade.insert(0, "1")

        else:
            ProdutoNaoEncontrado()

    def removeLinha(self, codigoProduto):
        itensDaLista = self.conteudoTabela.get_children()
        for item in itensDaLista:
            produtoNalista = self.conteudoTabela.item(item, 'values')[0]
            if (codigoProduto == produtoNalista):
                valorDoProduto = float(self.conteudoTabela.item(
                    item, 'values')[3].replace(",", "."))
                self.total -= valorDoProduto
                totalFormatado = "{:.2f}".format(self.total)
                self.campoValorTotal['text'] = f"R$ {totalFormatado}"
                self.conteudoTabela.delete(item)
                self.campoExcluirProduto.delete(0, 'end')

    def finalizaCompra(self):
        itensDaLista = self.conteudoTabela.get_children()
        for item in itensDaLista:
            codigoProduto = self.conteudoTabela.item(item, 'values')[0]
            quantidade = int(self.conteudoTabela.item(item, 'values')[2])
            statusAtualizacao = self.planilha.atualizaQuantidadeProduto(
                codigoProduto, quantidade)
            if(statusAtualizacao):
                pass
            else:
                print(f'Verifique o item: {codigoProduto}')

        self.limpaTabela()
        self.campoValorTotal['text'] = ""

    def limpaTabela(self):
        itensDaTabela = self.conteudoTabela.get_children()
        for i in itensDaTabela:
            self.conteudoTabela.delete(i)


root = tk.Tk()
# root.geometry("800x600")
root.attributes('-fullscreen', True)
root.title(f'Vendas - {ESTABELECIMENTO}')
root.configure(bg=COR_SECUNDARIA)
app = TelaDeVendas(master=root)
app.mainloop()
