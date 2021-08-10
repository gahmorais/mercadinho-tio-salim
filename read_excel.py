from Manipula_Excel import Excel
# from openpyxl import load_workbook
from Produto import Produto
from Venda import Venda

CAMINHO_DO_ARQUIVO_EXCEL = 'inventario-loja.xlsx'
planilha = Excel(CAMINHO_DO_ARQUIVO_EXCEL)

produto = planilha.buscaProduto("7891203058614")
print(produto.descricao)


# print(planilha.buscaProduto('7896029007112').quantidade)
# atualizaProduto = planilha.atualizaQuantidadeProduto('7896029007112', 2)
# if(atualizaProduto):
#     print("Produto atualizado com sucesso")
#     print(planilha.buscaProduto('7896029007112').codigo)
#     print(planilha.buscaProduto('7896029007112').descricao)
#     print(planilha.buscaProduto('7896029007112').precoCompra)
#     print(planilha.buscaProduto('7896029007112').precoVenda)
#     print(planilha.buscaProduto('7896029007112').quantidade)
# else:
#     quantidade = planilha.buscaProduto('7896029007112').quantidade
#     print("Não há quantidade suficiente para executar esta ação. Quantidade em estoque: " + str(quantidade))


# while(opcaoDesejada != "c"):
#     opcaoDesejada = input("O que deseja fazer?\n1) Iniciar venda\n2) Consultar Produto\nc) Encerrar programa\n")
#     if(opcaoDesejada == "1"):
#         print("Modo venda")
#     elif(opcaoDesejada == "2"):
#         database = Excel(CAMINHO_DO_ARQUIVO_EXCEL)
#         codigoProduto = input("Escaneie o código do produto ou pressione \"C\" para cancelar\n")
#         produto = database.buscaProduto(codigoProduto)
#         if(produto != ""):
#             print("\n\n" + produto.codigo + " | " + produto.descricao + " | R$ " + produto.precoVenda + "\n\n")
#         else:
#             print("\n\nProduto não encontrado\n")

# print("Programa encerrado!!")

# def venda():
#     venda = True
#     carrinho = []
#     planilha = Excel(CAMINHO_DO_ARQUIVO_EXCEL)
#     produto = ""
#     while(venda & (produto != "c")):
#         produto = input("Escaneie o código do produto, \"c\" para cancelar \"f\" para finalizar a compra\n")
#         buscaProduto = planilha.buscaProduto(produto)
#         if(buscaProduto != ""):
#             carrinho.append(buscaProduto)
#         else:
#             print("Produto não encontrado")
