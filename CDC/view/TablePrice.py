from tkinter import messagebox

from CDC.controller.Controller import priceTable
import tkinter as tk


class TablePrice:

    def __init__(self, root, main_window):
        # Cria tabela em um Entry do Tkinter com os dados:
        self.gera_tabela_price(main_window)
        linhas = len(self.tabela_price)
        colunas = len(self.tabela_price[0])
        janelaPrice = tk.Toplevel(root)
        for i in range(linhas):
            for j in range(colunas):
                self.entry = tk.Entry(janelaPrice, width=20)
                self.entry.grid(row=i, column=j)
                # Deixando com 2 casas decimais os valores em Reais:
                if (i>0 and j>0):
                    self.entry.insert("end", round(float(self.tabela_price[i][j]),2))
                else:
                    self.entry.insert("end", self.tabela_price[i][j])

    def gera_tabela_price(self, main_window):
        try:
            parcelas = int(main_window.parcelas_entry.get())
        except:
            messagebox.showerror("Error", "As parcelas precisam ser um número inteiro")
            raise Exception("As parcelas precisam ser um número inteiro")

        try:
            preco_a_vista = float(main_window.preco_a_vista_entry.get())
        except:
            messagebox.showerror("Error", "O preço à vista precisa ser um número real")
            raise Exception("O preço à vista precisa ser um número real")

        try:
            juros = float(main_window.juros_entry.get())
        except:
            messagebox.showerror("Error", "Os Juros precisam ser um número real")
            raise Exception("Os Juros precisam ser um número real")
        self.tabela_price = priceTable(parcelas, preco_a_vista, juros)