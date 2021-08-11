import tkinter as tk
from tkinter import ttk
from Alerta import ProdutoNaoEncontrado
from Manipula_Excel import Excel

class TelaDeVendas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.criaElementos()
        self.planilha = Excel('inventario-loja.xlsx')
        self.count = 1
        self.total = 0

    def criaElementos(self):
        self.labelCampoCodigoProduto = tk.Label(text="Digite o código do produto: ")
        self.campoCodigoProduto = tk.Entry(self.master)
        
        self.labelCampoQuantidade = tk.Label(text="Digite a quantidade")
        self.campoQuantidade = tk.Entry(self.master)

        self.labelExcluirProduto = tk.Label(text="Digite o código do produto a ser excluído")
        self.campoExcluirProduto = tk.Entry(self.master)

        self.btnExcluirProduto = tk.Button(text="Excluir produto", command = lambda: self.removeLinha(self.campoExcluirProduto.get()))

        self.btnFinalizaCompra = tk.Button(text="Finalizar", command= self.finalizaCompra)

        self.tabela = tk.Frame(self.master)
        self.campoCodigoProduto.bind('<Return>', lambda e: self.adicionaLinha(self.campoCodigoProduto.get(), self.campoQuantidade.get()))

        self.btnBuscarProduto = tk.Button(text="Buscar", command=lambda: self.adicionaLinha(self.campoCodigoProduto.get(), self.campoQuantidade.get()))

        self.labelValorTotal = tk.Label(text="Total: ")
        self.campoValorTotal = tk.Label(bg='gray',width=12, fg='#fff')

        self.conteudoTabela = ttk.Treeview(self.tabela)
        self.conteudoTabela.bind('<Delete>', lambda e: self.removeLinha( self.campoCodigoProduto.get()))

        self.conteudoTabela['columns']=('Código', 'Descricao', 'Quantidade', 'Preço')
        self.conteudoTabela.column('#0', width=0, stretch='NO')
        self.conteudoTabela.column('Código', anchor='center', width=100)
        self.conteudoTabela.column('Descricao', anchor='center', width=200)
        self.conteudoTabela.column('Quantidade', anchor='center', width=80)
        self.conteudoTabela.column('Preço', anchor='center', width=80)

        self.conteudoTabela.heading('#0', text='', anchor='center')
        self.conteudoTabela.heading('Código', text='Código', anchor='center')
        self.conteudoTabela.heading('Descricao', text='Descricao', anchor='center')
        self.conteudoTabela.heading('Quantidade', text='Quantidade', anchor='center')
        self.conteudoTabela.heading('Preço', text='Preço', anchor='center')
        
        self.labelCampoCodigoProduto.pack()
        self.campoCodigoProduto.pack()
        self.labelCampoQuantidade.pack()
        self.campoQuantidade.pack()
        self.campoQuantidade.insert(0, "1")
        self.labelExcluirProduto.pack()
        self.campoExcluirProduto.pack()
        self.btnBuscarProduto.pack()
        self.btnExcluirProduto.pack()
        self.tabela.pack()
        self.conteudoTabela.pack()
        self.labelValorTotal.pack()
        self.campoValorTotal.pack()
        self.btnFinalizaCompra.pack()
        

    def adicionaLinha(self, codigoProduto, quantidade = 1):
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
                valor = float(self.conteudoTabela.item(child, 'values')[3].replace(",", "."))
                quantidade = int(self.conteudoTabela.item(child, 'values')[2])
                self.total += valor*quantidade

            totalFormatado = "{:.2f}".format(self.total)
            self.campoValorTotal['text'] = f"R$ {totalFormatado}"
            self.campoCodigoProduto.delete(0,'end')

        else:
            ProdutoNaoEncontrado()

    def removeLinha(self, codigoProduto):
        itensDaLista = self.conteudoTabela.get_children()
        for item in itensDaLista:
            produtoNalista = self.conteudoTabela.item(item, 'values')[0]
            if (codigoProduto == produtoNalista):
                valorDoProduto = float(self.conteudoTabela.item(item, 'values')[3].replace(",","."))
                self.total -= valorDoProduto
                totalFormatado = "{:.2f}".format(self.total)
                self.campoValorTotal['text'] = f"R$ {totalFormatado}"
                self.conteudoTabela.delete(item)
        # try:
        #     item = self.conteudoTabela.selection()[0]
        #     valorDoItem = float(self.conteudoTabela.item(item, 'values')[3].replace(",","."))
        #     self.total -= valorDoItem
        #     totalFormatado = "{:.2f}".format(self.total)
        #     self.campoValorTotal['text'] = f"R$ {totalFormatado}"
        #     self.conteudoTabela.delete(item)
        # except:
        #     print("Selecione o item para excluir")

    def finalizaCompra(self):
        self.limpaTabela()
        # itensDaLista = self.conteudoTabela.get_children()
        # for i in itensDaLista:
        #     codigoProduto = self.conteudoTabela.item(i, 'values')[0]
        #     quantidadeProduto = self.conteudoTabela.item(i, 'values')[2]
        #     self.planilha.atualizaQuantidadeProduto(codigoProduto, quantidadeProduto)

    def limpaTabela(self):
        itensDaTabela = self.conteudoTabela.get_children()
        for i in itensDaTabela:
            self.conteudoTabela.delete(i)

root = tk.Tk()
root.geometry("800x600")
# root.attributes('-fullscreen', True)
root.title("Vendas - Mercadinho Sr. Salim")
app = TelaDeVendas(master=root)
app.mainloop()