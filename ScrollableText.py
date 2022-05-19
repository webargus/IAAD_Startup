"""
    Class ScrollableText
    Widget de área de texto com barra de rolagem vertical e métodos para adição/inserção/edição do texto
    Autor: grupo UFRPE - BSI - IAAD - 2022
    ISENÇÃO DE RESPONSABILIDADE: o risco do uso é totalmente por sua conta!
    Licença: use e mexa no código à vontade, mas inclua esse cabeçalho.
"""

from tkinter import *
import tkinter.ttk as ttk

class ScrollableText(Text):

    def __init__(self, frame, max_height = 5):

        super(ScrollableText, self).__init__(frame)

        #   posiciona widget Text no lado esquerdo do frame
        self.grid({"row": 0, "column": 0, "sticky": EW})
        #  adiciona barra de rolagem vertical
        vscroll = ttk.Scrollbar(frame, orient=VERTICAL, command=self.yview)
        vscroll.grid({"row": 0, "column": 1, "sticky": NS})
        self.configure(yscrollcommand=vscroll.set, height=max_height)
        #  configura a fonte do texto
        self.tag_configure("font", font=('Arial', 10))
        #   torna o widget não-editável, mas sem desabilitá-lo
        self.bind("<Key>", lambda e: "break")

    def append_text(self, text):
        self.insert(END, text + "\n", 'font')
        
    def insert_text(self, text):
        self.insert("0.0", text + "\n", 'font')

    def clear(self):
        self.delete('1.0', END)

    def set_text(self, text):
        self.delete()
        self.append_text(text)





