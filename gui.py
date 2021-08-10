import tkinter as tk
from Manipula_Excel import Excel
from TelaDeVendas import TelaDeVendas
from openpyxl import load_workbook


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        CAMINHO_DO_ARQUIVO_EXCEL = 'inventario-loja.xlsx'
        self.master = master
        self.pack()
        self.create_widgets()
        self.planilha = Excel(CAMINHO_DO_ARQUIVO_EXCEL)

    def create_widgets(self):
        self.label_digiteOCodigo = tk.Label(
        self.master, text="Digite o código: ")
        self.label_descricao = tk.Label(self.master)
        self.label_codigoProduto = tk.Label(self.master)
        self.label_preco = tk.Label(self.master)
        self.label_quantidade = tk.Label(self.master)

        self.digiteOCodigo = tk.Entry(self.master)
        self.btnBuscaProduto = tk.Button(self.master, text="Busca produto", fg="red",
                                         command=lambda: self.setaDadosNaTela(self.digiteOCodigo.get()))

        self.quit = tk.Button(self.master, text="Sair", fg="red",
                              command=self.master.destroy)

        self.btnAbreTelaDeVendas = tk.Button(
            self.master, text="Vendas", command=self.abreTelaDeVendas)

        self.label_digiteOCodigo.place(x=0, y=0)
        self.digiteOCodigo.place(x=100, y=0)
        self.btnBuscaProduto.place(x=250, y=0)
        self.btnAbreTelaDeVendas.place(x=400, y=100)
        self.quit.place(x=700, y=0)

    def setaDadosNaTela(self, codigo):
        produto = self.planilha.buscaProduto(codigo)
        if(produto != ""):
            self.label_descricao["text"] = produto.descricao
            self.label_codigoProduto["text"] = produto.codigo
            self.label_preco["text"] = "R$ " + produto.precoVenda
            self.label_quantidade["text"] = produto.quantidade

            self.label_codigoProduto.place(y=100, x=0)
            self.label_descricao.place(y=100, x=100)
            self.label_preco.place(y=100, x=300)
            self.label_quantidade.place(y=100, x=400)
        else:
            self.label_codigoProduto["text"] = ""
            self.label_preco["text"] = ""
            self.label_quantidade["text"] = ""
            self.label_descricao["text"] = "Produto não encontrado"
            self.label_descricao.pack()

    def abreTelaDeVendas(self):
        root = tk.Tk()
        root.geometry("800x600")
        root.title("Vendas - Mercadinho Sr. Salim")
        app = TelaDeVendas(master=root)
        app.mainloop()


root = tk.Tk()
root.geometry("800x600")
root.title("Mercadinho Sr. Salim")
app = Application(master=root)
app.mainloop()
