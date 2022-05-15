
"""
    UFRPE - BSI - IAAD - 2ª VA
    Descrição: Interface gráfica para operações CRUD no BD Startups
"""

from textwrap import fill
from tkinter import *
from tkinter.ttk import *
import ScrollableText
import Tools


class Gui(Frame):

    def __init__(self):
        Frame.__init__(self)
        Tools.Tools.root(self.master)
        Tools.Tools.center_window(self.master, 1120, 600)
        # self.master.iconbitmap("brasao32.ico")
        self.master.resizable(0, 0)
        self.master.state('normal')
        self.master.title("IAAD - Startups")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        top_frame = Frame(self)
        top_frame.grid({"row": 0, "column": 0})
        top_frame.pack(padx=8, pady=8)

        combo_label = Label(top_frame, text="Selecione a tabela:")
        combo_label.grid({"row": 0, "column": 0})
        
        combo = Combobox(top_frame, values = ['a', 'b']);
        combo.grid({"row": 0, "column": 1})
        

        # self.nb = Notebook(self)
        # #   add tabs
        # self.nb_files = [("Inserir", Frame(self.nb), "Create"),         # C
        #                  ("Listar", Frame(self.nb), "Read"),            # R
        #                  ("Atualizar", Frame(self.nb), "Update"),       # U
        #                  ("Deletar", Frame(self.nb), "Delete")]         # D
        # for i in self.nb_files:
        #     self.nb.add(i[1], text="    " + i[0] + "    ")
        # self.nb.grid({"row": 0, "column": 0, "sticky": NSEW})
        # self.nb.bind("<<NotebookTabChanged>>", self._tab_switch)

        # CombPanel.CombPanel(self.nb_files[0][1])
        # GraphPanel.GraphPanel(self.nb_files[1][1])

        # frame = Frame(self)
        # frame.grid({"row": 0, "column": 1, "sticky": NSEW, "pady": 4, "padx": 4})
        # frame.grid_rowconfigure(0, weight=1)
        # frame.grid_columnconfigure(0, weight=1)
        # self.text_widget = ScrollableText.ScrollableText(frame)

        self.mainloop()

    def _tab_switch(self, event):
        file = self.nb_files[self.nb.index(self.nb.select())][2] + ".py"
        try:
            handle = open(file, "r", encoding="utf-8")
        except OSError:
            print(OSError.args)
        self.text_widget.clear()
        for line in handle.readlines():
            self.text_widget.append_text(line)
        handle.close()


if __name__ == '__main__':
    gui = Gui()






