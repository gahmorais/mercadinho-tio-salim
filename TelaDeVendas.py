import tkinter as tk
from Alerta import ProdutoNaoEncontrado
from Manipula_Excel import Excel

class TelaDeVendas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.criaElementos()
        self.planilha = Excel('inventario-loja.xlsx')
        self.listaDeProdutos = [("Descrição", "Quantidade", "Preço")]

    def criaElementos(self):
        self.labelCampoCodigoProduto = tk.Label(text="Digite o código do produto: ")
        self.campoCodigoProduto = tk.Entry(self.master)
        self.tabela = tk.Frame(self.master)
        self.campoCodigoProduto.bind('<Return>', lambda e: self.adicionaLinha(self.campoCodigoProduto.get()))
        self.btnBuscarProduto = tk.Button(text="Buscar", command=lambda: self.adicionaLinha(self.campoCodigoProduto.get()))
        
        self.labelCampoCodigoProduto.pack()
        self.campoCodigoProduto.pack()
        self.btnBuscarProduto.pack()
        self.tabela.pack()

    def adicionaLinha(self, codigoProduto, quantidade=1):
        produto = self.planilha.buscaProduto(codigoProduto)
        if(produto != ""):
            self.listaDeProdutos.append((produto.descricao, quantidade, produto.precoVenda ))
            self.geraTabela()
        else:
            ProdutoNaoEncontrado()
    
    def geraTabela(self):
        QuantidadeLinhas = len(self.listaDeProdutos)
        QuantidadeColunas = 3

        for i in range(QuantidadeLinhas):
            for j in range(QuantidadeColunas):
                self.linhas = tk.Entry(self.tabela)
                self.linhas.grid(row = i, column = j)
                self.linhas.configure(state='normal')
                self.linhas.insert(0,self.listaDeProdutos[i][j])
                self.linhas.configure(state='disabled')
        soma = 0
        for i in range(QuantidadeLinhas):
            if(i > 0):
                soma += float(self.listaDeProdutos[i][2].replace(",","."))

        self.total = tk.Label(self.tabela, text=f"Total: {soma}")
        self.total.grid(row=i+1, column=j)
        self.campoCodigoProduto.delete(0,'end')

root = tk.Tk()
root.geometry("800x600")
root.title("Vendas - Mercadinho Sr. Salim")
app = TelaDeVendas(master=root)
app.mainloop()