

from app.models.fornecedor import Fornecedor

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class Fornecedor_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
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
        self.lbl_razao_social = tk.Label(
            self.frm_dados,
            text = "Razão social:"
        )
        self.lbl_razao_social.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_razao_social = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_razao_social.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_nome_fantasia = tk.Label(
            self.frm_dados,
            text = "Nome fantasia:"
        )
        self.lbl_nome_fantasia.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome_fantasia = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_nome_fantasia.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_cnpj = tk.Label(
            self.frm_dados,
            text = "CNPJ:"
        )
        self.lbl_cnpj.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_cnpj = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_cnpj.grid(
            row = 2,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_sla = tk.Label(
            self.frm_dados,
            text = "SLA de atendimento:"
        )
        self.lbl_sla.grid(
            row = 2,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_sla = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_sla.grid(
            row = 2,
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
        self.tbl_fornecedores = ttk.Treeview(
            self.root,
            height = 10
        )  
        self.tbl_fornecedores.grid(
            row = 3,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_fornecedores["columns"] = (
            "id",
            "razao_social",
            "cnpj"
        )
        self.tbl_fornecedores.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_fornecedores.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_fornecedores.column(
            "razao_social",
            width = 50
        )
        self.tbl_fornecedores.column(
            "cnpj",
            width = 20
        )
        self.tbl_fornecedores.heading(
            "id",
            text = "ID"
        )
        self.tbl_fornecedores.heading(
            "razao_social",
            text = "Razão Social"
        )
        self.tbl_fornecedores.heading(
            "cnpj",
            text = "CNPJ"
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
        self.tbl_fornecedores.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_fornecedor

        )
    def preencher_campos(self, fornecedor):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(fornecedor.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_razao_social.insert(
            0,
            fornecedor.razao_social
        )

        self.txt_nome_fantasia.insert(
            0,
            fornecedor.nome_fantasia
        )

        self.txt_cnpj.insert(
            0,
            fornecedor.cnpj
        )

        self.txt_sla.insert(
            0,
            str(fornecedor.sla_atendimento)
        )        

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_razao_social.delete(0, tk.END)
        self.txt_nome_fantasia.delete(0,tk.END)
        self.txt_cnpj.delete(0, tk.END)
        self.txt_sla.delete(0, tk.END)
        self.txt_razao_social.focus()

    def limpar_treeview(self):
        for item in self.tbl_fornecedores.get_children():
            self.tbl_fornecedores.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_fornecedores.selection()[0]

        return self.tbl_fornecedores.item(item)["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir este fornecedor?"
        )

    def ler_dados_fornecedor(self):
        razao_social = self.txt_razao_social.get()
        nome_fantasia = self.txt_nome_fantasia.get()
        cnpj = self.txt_cnpj.get()
        sla = int(self.txt_sla.get())
        return razao_social, nome_fantasia, cnpj, sla
    
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
    def exibir_fornecedores(self, fornecedores):

        self.limpar_treeview()

        for fornecedor in fornecedores:

            self.tbl_fornecedores.insert(
                "",
                tk.END,
                values=(
                    fornecedor.id,
                    fornecedor.razao_social,
                    fornecedor.cnpj
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()