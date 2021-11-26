import tkinter as tk

from CDC.view.ButtonJuros import ButtonJuros
from CDC.view.ButtonPrecoAPrazo import ButtonPrecoAPrazo
from CDC.view.ButtonPrecoAvista import ButtonPrecoAVista
from CDC.view.ButtonTabelaPrice import ButtonTabelaPrice


class MainWindow:

    def __init__(self):
        canvas_height = 250
        canvas_width = 800

        # Inicializa a tela
        root = tk.Tk()
        root.config(width=canvas_width, height=canvas_height)

        # Preenche os labels e campos
        self.parcelas_label = tk.Label(root, text="Parcelas:")
        self.parcelas_label.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)
        self.parcelas_entry = tk.Entry(root, bd =5)
        self.parcelas_entry.place(relx=0.25, rely=0.1, relwidth=0.3, relheight=0.1)

        self.juros_label = tk.Label(root, text="Taxa de Juros:")
        self.juros_label.place(relx=0.1, rely=0.2, relwidth=0.1, relheight=0.1)
        self.juros_entry = tk.Entry(root, bd =5)
        self.juros_entry.place(relx=0.25, rely=0.2, relwidth=0.3, relheight=0.1)

        self.preco_a_vista_label = tk.Label(root, text="Preço à Vista:")
        self.preco_a_vista_label.place(relx=0.1, rely=0.3, relwidth=0.1, relheight=0.1)
        self.preco_a_vista_entry = tk.Entry(root, bd = 5)
        self.preco_a_vista_entry.place(relx=0.25, rely=0.3, relwidth=0.3, relheight=0.1)

        self.preco_a_prazo_label = tk.Label(root, text="Preço à Prazo:")
        self.preco_a_prazo_label.place(relx=0.1, rely=0.4, relwidth=0.1, relheight=0.1)
        self.preco_a_prazo_entry = tk.Entry(root, bd = 5)
        self.preco_a_prazo_entry.place(relx=0.25, rely=0.4, relwidth=0.3, relheight=0.1)

        self.entrada_boolean = tk.BooleanVar()
        self.entrada_boolean.set(False)
        self.entrada_checkbutton = tk.Checkbutton(root, text = "Entrada:", variable= self.entrada_boolean)
        self.entrada_checkbutton.place(relx=0.1, rely=0.5)

        # Gera os botões
        ButtonJuros(root,self)
        ButtonPrecoAPrazo(root,self)
        ButtonPrecoAVista(root,self)
        ButtonTabelaPrice(root,self)

        root.mainloop()


main = MainWindow()