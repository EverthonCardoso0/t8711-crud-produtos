from app.models.fornecedor import Fornecedor

import tkinter as tk
from tkinter import messagebox



class Fornecedor_View:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD de Fornecedores")
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def criar_componentes(self):
        pass
    def configurar_treeview(self):
        pass
    def configurar_eventos(self):
        pass 

    def iniciar(self):
        self.root.mainloop()

f = Fornecedor_View(tk.Tk())
f.iniciar()