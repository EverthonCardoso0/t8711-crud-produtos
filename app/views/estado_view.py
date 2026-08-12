

from app.models.estado import Estado
from app.core.idioma import Idioma

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class Estado_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("estado.janela_titulo"))
        self.root.geometry("800x600")
        self.root.resizable(False, False)


    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = Idioma.t("estado.titulo"),
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = Idioma.t("estado.dados_frame")
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=2,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.frm_dados.grid_columnconfigure(0, weight=0)
        self.frm_dados.grid_columnconfigure(1, weight=1)
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('comum.id')}:"
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
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('comum.nome')}:"
        )
        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width = 30
        )
        self.txt_nome.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_sigla = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('estado.sigla')}:"
        )
        self.lbl_sigla.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_sigla = tk.Entry(
            self.frm_dados,
            width = 5
        )
        self.txt_sigla.grid(
            row = 2,
            column = 1,
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
            row = 3,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 2,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = Idioma.t("comum.novo"),
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
            text = Idioma.t("comum.salvar"),
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
            text = Idioma.t("comum.alterar"),
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
            text = Idioma.t("comum.excluir"),
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
            text = Idioma.t("comum.fechar"),
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
            height = 12
        )
        self.tbl_estados.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_estados["columns"] = (
            "id",
            "nome",
            "sigla"
        )
        self.tbl_estados.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_estados.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_estados.column(
            "nome",
            width = 50
        )
        self.tbl_estados.column(
            "sigla",
            width = 20
        )
        self.tbl_estados.heading(
            "id",
            text = Idioma.t("comum.id")
        )
        self.tbl_estados.heading(
            "nome",
            text = Idioma.t("comum.nome")
        )
        self.tbl_estados.heading(
            "sigla",
            text = Idioma.t("estado.sigla")
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

        self.txt_nome.insert(
            0,
            estado.nome
        )

        self.txt_sigla.insert(
            0,
            estado.sigla
        )

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        self.txt_sigla.delete(0, tk.END)
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_estados.get_children():
            self.tbl_estados.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_estados.selection()[0]

        return self.tbl_estados.item(item)["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("estado.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_estado(self):
        nome = self.txt_nome.get()
        sigla = self.txt_sigla.get()
        return nome, sigla

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem,
                parent=self.root
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem,
                parent=self.root
            )
    def exibir_estados(self, estados):

        self.limpar_treeview()

        for estado in estados:

            self.tbl_estados.insert(
                "",
                tk.END,
                values=(
                    estado.id,
                    estado.nome,
                    estado.sigla
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()
