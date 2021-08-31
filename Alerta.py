import tkinter as tk
from constantes import *


class Mensagem(tk.Toplevel):
    def __init__(self, master, mensagem):
        tk.Toplevel.__init__(self, master)
        self.main_frame = tk.Frame(
            self,
            bg=COR_FUNDO_SECUNDARIA,
            highlightthickness=2,
            highlightcolor=CINZA_CHUMBO
        )
        espacamentoSuperior = int(self.winfo_screenheight() * .4)
        espacamentoLadoEsquerdo = int(self.winfo_screenwidth() * .4)
        self.geometry(
            f"320x240+{espacamentoLadoEsquerdo}+{espacamentoSuperior}")
        self.title("")
        self.resizable(False, False)
        self.overrideredirect(1)
        self.bind('<Return>', lambda a: self.destroy())
        self.bind('<Escape>', lambda a: self.destroy())
        self.focus_force()
        self.main_frame.pack(expand=1, fill='both')

        self.mensagem = tk.Label(
            self.main_frame,
            text=mensagem,
            font=ESTILO_FONT_MEDIA,
            fg=COR_TEXTO_PRIMARIA,
            bg=COR_FUNDO_SECUNDARIA
        )

        self.btnSair = tk.Button(
            self.main_frame,
            text="Fechar",
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO_PRIMARIA,
            border=1,
            font=ESTILO_FONT_MEDIA,
            command=self.destroy
        )

        self.mensagem.pack(expand=1, fill='x')
        self.btnSair.pack(expand=1, fill='x', padx=40)
