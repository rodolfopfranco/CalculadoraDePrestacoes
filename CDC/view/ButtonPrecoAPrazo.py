import tkinter as tk
from tkinter import messagebox

from CDC.controller.Controller import valor_a_prazo


class ButtonPrecoAPrazo:

    def __init__(self, root, main_window):
        self.button = tk.Button(root, text="Obter preço à prazo", command=lambda: self.calculaPrecoAPrazo(main_window),
                                bg='#80c1ff')
        self.button.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)
        self.button.config(font=("Times New Roman", 10))

    def calculaPrecoAPrazo(self,main_window):
        """Obtém os dados do formulário e verifica se estão no formato certo"""
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
            preco_a_vista = float(main_window.preco_a_vista_entry.get())
        except:
            messagebox.showerror("Error", "O preço à vista precisa ser um número real")
            raise Exception("O preço à vista precisa ser um número real")
        preco_a_prazo = valor_a_prazo(juros,parcelas,preco_a_vista)
        main_window.preco_a_prazo_entry.delete(0, "end")
        main_window.preco_a_prazo_entry.insert(0, round(preco_a_prazo, 2))
