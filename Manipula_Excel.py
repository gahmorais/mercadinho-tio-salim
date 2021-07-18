from Produto import Produto
from openpyxl import load_workbook

class Excel:
    def __init__(self, caminhoDoArquivo):
        excelFile = load_workbook(caminhoDoArquivo)
        self._planilhaAtiva = excelFile.active

    def retornaTodaTabela(self):

        #Seta a quantidade de linhas e colunas da tabela
        linhas = self._planilhaAtiva.max_row
        colunas = self._planilhaAtiva.max_column

        #Inicializa variaveis das linhas e do conteúdo da tabela.
        valoresDasLinhas = []
        conteudoDaPlanilha = []

        #Busca conteúdo de toda a tabela
        for i in range(1, linhas + 1):
            valoresDasLinhas = []
            for j in range(1, colunas + 1):
                celula = self._planilhaAtiva.cell(row=i, column=j)
                valoresDasLinhas.append(celula.value)

            codigo      = valoresDasLinhas[0]
            descricao   = valoresDasLinhas[1]
            precoCompra = valoresDasLinhas[2]
            precoVenda  = valoresDasLinhas[3]
            quantidade  = valoresDasLinhas[4]

            produto = Produto(codigo, descricao, precoCompra, precoVenda, quantidade)
            conteudoDaPlanilha.append(produto)
        return conteudoDaPlanilha
    
    def buscaProduto(self, produto):
        tabela = self.retornaTodaTabela()
        produtoEncontrado = ""
        for i in range(len(tabela)):
            if(produto == tabela[i].codigo):
                produtoEncontrado = tabela[i]
        return produtoEncontrado
