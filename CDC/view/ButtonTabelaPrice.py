import tkinter as tk

from CDC.view.TablePrice import TablePrice


class ButtonTabelaPrice:

    def __init__(self, root, main_window):
        self.button = tk.Button(root, text="Gerar tabela Price", command=lambda: TablePrice(root, main_window),bg='#80c1ff')
        self.button.place(relx=0.3, rely=0.8, relwidth=0.3, relheight=0.1)
        self.button.config(font=("Times New Roman", 10))

    # Depois preciso validar os dados antes de chamar como lambda