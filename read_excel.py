from Manipula_Excel import Excel
# from openpyxl import load_workbook
from Produto import Produto
from Venda import Venda

CAMINHO_DO_ARQUIVO_EXCEL = 'inventario-loja.xlsx'
planilha = Excel(CAMINHO_DO_ARQUIVO_EXCEL)

produto = planilha.buscaProduto("7891203058614")
print(produto.descricao)
