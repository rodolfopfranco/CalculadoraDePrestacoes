import tkinter as tk
from tkinter import messagebox

from CDC.controller.Controller import getInterest


class ButtonJuros:

    def __init__(self, root, main_window):
        self.button = tk.Button(root, text="Obter taxa de juros", command=lambda: self.calculaJuros(main_window),bg='#80c1ff')
        self.button.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)
        self.button.config(font=("Times New Roman", 10))

    def calculaJuros(self,main_window):
        try:
            parcelas = int(main_window.parcelas_entry.get())
        except:
            messagebox.showerror("Error", "As parcelas precisam ser um número inteiro")
            raise Exception("As parcelas precisam ser um número inteiro")
        try:
            preco_a_prazo = float(main_window.preco_a_prazo_entry.get())
        except:
            messagebox.showerror("Error", "O preço à prazo precisa ser um número real")
            raise Exception("O preço à prazo precisa ser um número real")
        try:
            preco_a_vista = float(main_window.preco_a_vista_entry.get())
        except:
            messagebox.showerror("Error", "O preço à vista precisa ser um número real")
            raise Exception("O preço à vista precisa ser um número real")
        juros, interacoes = getInterest(preco_a_prazo,preco_a_vista,parcelas)
        main_window.juros_entry.delete(0, "end")
        main_window.juros_entry.insert(0, round(juros, 4))

