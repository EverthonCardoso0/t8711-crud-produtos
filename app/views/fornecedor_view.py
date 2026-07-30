import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.models.fornecedor import Fornecedor

import tkinter as tk
from tkinter import messagebox


class Fornecedor_View:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Fornecedores")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
  

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Fornecedores",
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = "Dados do fornecedor"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=4
        )
    def configurar_treeview(self):
        pass
    def configurar_eventos(self):
        pass 

    def iniciar(self):
        self.root.mainloop()

f = Fornecedor_View(tk.Tk())
f.iniciar()
