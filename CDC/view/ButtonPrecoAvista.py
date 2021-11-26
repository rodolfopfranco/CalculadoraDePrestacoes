import tkinter as tk
from tkinter import messagebox

from CDC.controller.Controller import valor_presente_no_tempo_0


class ButtonPrecoAVista:

    def __init__(self, root, main_window):
        self.button = tk.Button(root, text="Obter preço à vista", command=lambda: self.calculaPrecoAVista(main_window),
                                bg='#80c1ff')
        self.button.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.1)
        self.button.config(font=("Times New Roman", 10))

    def calculaPrecoAVista(self,main_window):
        try:
            parcelas = int(main_window.parcelas_entry.get())
        except:
            messagebox.showerror("Error", "As parcelas precisam ser um número inteiro")
            raise Exception("As parcelas precisam ser um número inteiro")
        try:
            juros = float(main_window.juros_entry.get())
        except:
            messagebox.showerror("Error", "Os Juros precisam ser um número real")
            raise Exception("Os Juros precisam ser um número real")
        try:
            preco_a_prazo = float(main_window.preco_a_prazo_entry.get())
        except:
            messagebox.showerror("Error", "O preço à prazo precisa ser um número real")
            raise Exception("O preço à prazo precisa ser um número real")
        entrada = bool(main_window.entrada_boolean.get())
        preco_a_vista = valor_presente_no_tempo_0(preco_a_prazo,parcelas,juros,entrada)
        main_window.preco_a_vista_entry.delete(0,"end")
        main_window.preco_a_vista_entry.insert(0, round(preco_a_vista, 2))
