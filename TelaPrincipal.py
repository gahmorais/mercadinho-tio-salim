import tkinter as tk
from PIL import ImageTk, Image
from Manipula_Excel import Excel
from TelaDeVendas import TelaDeVendas
from TelaDeConsulta import TelaDeConsulta
from constantes import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.criaElementos()

    def criaElementos(self):
        self.frameTituloELogo = tk.Frame(self.master, bg=COR_FUNDO_SECUNDARIA)
        self.frameBotoes = tk.Frame(self.master, bg=COR_FUNDO_SECUNDARIA)
        self.frameTitulo = tk.Frame(
            self.frameTituloELogo, bg=COR_FUNDO_SECUNDARIA)

        self._tamanhoDaTela = self.winfo_screenheight()
        if(self._tamanhoDaTela < 900):
            self.TAMANHO_DA_IMAGEM = IMAGEM_PEQUENA
        else:
            self.TAMANHO_DA_IMAGEM = IMAGEM_GRANDE

        self.tituloLinhaUm = tk.Label(
            self.frameTitulo,
            text='Mercado',
            font=ESTILO_FONT_TELA_PRINCIPAL_GRANDE,
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO_PRIMARIA
        )

        self.tituloLinhaDois = tk.Label(
            self.frameTitulo,
            text='do bairro',
            font=ESTILO_FONT_TELA_PRINCIPAL_MUITO_GRANDE,
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO_PRIMARIA
        )

        self.logo = tk.Canvas(
            self.frameTituloELogo,
            bg=COR_FUNDO_SECUNDARIA,
            highlightthickness=0
        )

        self.btnFecharAplicacao = tk.Button(
            self.frameBotoes,
            text="Fechar aplicacao",
            font=ESTILO_FONT_GRANDE,
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            command=self.master.destroy
        )

        self.btnTelaDeVendas = tk.Button(
            self.frameBotoes,
            text="Venda",
            font=ESTILO_FONT_GRANDE,
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            command=self.abreTelaDeVendas
        )

        self.btnTelaDeConsulta = tk.Button(
            self.frameBotoes,
            text="Consulta produtos",
            font=ESTILO_FONT_GRANDE,
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            command=self.abreTelaDeConsulta
        )

        self.renderizaFrameBotoes()
        self.renderizaFrameTituloELogo()

    def renderizaFrameBotoes(self):
        self.frameBotoes.pack(
            side='right',
            expand=1,
            fill='both',
            padx=50,
            pady=100
        )
        self.btnTelaDeVendas.pack(
            expand=1, 
            fill='both', 
        )

        self.btnTelaDeConsulta.pack(
            expand=1, 
            fill='both', 
            pady=200
        )
        
        self.btnFecharAplicacao.pack(
            expand=1, 
            fill='both', 
        )

    def renderizaFrameTituloELogo(self):

        self.frameTituloELogo.pack(
            side='left',
            expand=1,
            fill='both',
            pady=100
        )

        self.frameTitulo.pack(expand=1, fill='both')
        self.tituloLinhaUm.pack(fill='x')
        self.tituloLinhaDois.pack(fill='x')
        self.logo.pack(expand=1, fill='both')
        imagemCarrinho = Image.open(LOGO_MERCADO)
        imagemCarrinho = imagemCarrinho.resize(
            self.TAMANHO_DA_IMAGEM,
            Image.ANTIALIAS
        )
        self._image = ImageTk.PhotoImage(imagemCarrinho)
        self.logo.create_image(300, 0, anchor='nw', image=self._image)

    def abreTelaDeVendas(self):
        TelaDeVendas(self)

    def abreTelaDeConsulta(self):
        TelaDeConsulta(self)


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg=COR_FUNDO_SECUNDARIA)
    app = Application(master=root)
    app.mainloop()
