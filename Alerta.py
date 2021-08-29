import tkinter as tk
from constantes import *


class ProdutoNaoEncontrado:
    def __init__(self, master=None):
        super().__init__()
        self.root = tk.Tk()
        self.root.geometry("320x240")
        self.root.title(f"Alerta - {ESTABELECIMENTO}")
        self.root.bind('<Return>', lambda a: self.root.destroy())
        self.root.bind('<Escape>', lambda a: self.root.destroy())
        self.root.focus_force()

        self.mensagem = tk.Label(
            self.root,
            text="Produto não encontrado",
            font=ESTILO_FONT_GRANDE
        )

        self.btnSair = tk.Button(
            self.root,
            text="Ok",
            font=ESTILO_FONT_GRANDE,
            command=self.root.destroy
        )
        
        self.mensagem.pack()
        self.btnSair.pack()
        self.root.mainloop()
