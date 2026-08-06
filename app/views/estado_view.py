import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from app.models.estado import Estado

class Estado_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()
    
    def configurar_janela(self):
        self.root.title("CRUD de Estados")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
    
    def criar_componentes(self):
        
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Estado",
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
            text = "Dados do Estado"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=4,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = "ID:"
        )
        self.lbl_id.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0,
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_nome_estado = tk.Label(
            self.frm_dados,
            text = "Nome Estado:"
        )
        self.lbl_nome_estado.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome_estado = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_nome_estado.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_UF = tk.Label(
            self.frm_dados,
            text = "UF:"
        )
        self.lbl_UF.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_UF = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_UF.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = "Novo",
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = "Salvar",
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = "Alterar",
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = "Excluir",
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = "Fechar",
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
        )
        self.tbl_estados = ttk.Treeview(
            self.root,
            height = 10
        )
        self.tbl_estados.grid(
            row = 3,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):


        self.tbl_estados["columns"] = (
            "id",
            "nome_estado",
            "UF"
        )
        self.tbl_estados.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_estados.column(
            "id",
            width = 10
        )
        self.tbl_estados.column(
            "nome_estado",
            width = 50
        )
        self.tbl_estados.column(
            "UF",
            width = 10
        )
        self.tbl_estados.heading(
            "id",
            text = "ID"
        )
        self.tbl_estados.heading(
            "nome_estado",
            text = "Nome Estado"
        )
        self.tbl_estados.heading(
            "UF",
            text = "UF"
        )
    
    def configurar_eventos(self):

        self.btn_novo.config(
            command = self.controller.new
        )
        self.btn_salvar.config(
            command = self.controller.save
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_fechar.config(
            command = self.fechar
        )
        self.tbl_estados.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_estado
        )
    
    def preencher_campos(self, estado):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(estado.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome_estado.insert(
            0,
            estado.nome_estado
        )

        self.txt_UF.insert(
            0,
            estado.UF
        )
    
    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome_estado.delete(0, tk.END)
        self.txt_UF.delete(0, tk.END)
        self.txt_nome_estado.focus()
        
    def limpar_treeview(self):
        for item in self.tbl_estados.get_children():
            self.tbl_estados.delete(item)

    def get_id_selecionado(self):

        item = self.tbl_estados.selection()[0]

        return self.tbl_estados.item(item)["values"][0]
    
    def confirmar_exclusao(self):
        
        return messagebox.askyesmo(
            "Confirmação",
            "Deseja realmente excluir este estado?"
        )
        
    def ler_dados_estado(self):
        nome_estado = self.txt_nome_estado.get()
        UF = self.txt_UF.get()
        return nome_estado, UF
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem
            )
    
    def exibir_estados(self, estados):

        self.limpar_treeview()

        for estado in estados:

            self.tbl_estados.insert(
                "",
                tk.END,
                values=(
                    estado.id,
                    estado.nome_estado,
                    estado.UF
                )
            )
    
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()
        self.root.mainloop()

