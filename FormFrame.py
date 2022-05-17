
from tkinter import *

class FormFrame:
    
    def __init__(self, frame, repo):
        self.repo = repo
        self.form = None
        
        # cria frame do formulário com 1 linha e 2 colunas
        self.form_frame = Frame(frame)
        self.form_frame.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.form_frame.columnconfigure(0, weight=3)
        self.form_frame.columnconfigure(1, weight=1)
        # frame dos botões à direita
        btn_frame = Frame(self.form_frame)
        btn_frame.grid(row=0, column=1, sticky="nsew")
        # botão C.
        params = {"text": "INSERIR",
            "width": 10,
            #"command": self._salvar_aluno
            }
        Button(btn_frame, params).grid({"row": 0, "column": 0, "pady": 8})
        # botão U.
        params = {"text": "ATUALIZAR",
            "width": 10,
            #"command": self._salvar_aluno
            }
        Button(btn_frame, params).grid({"row": 1, "column": 0, "pady": 8})
        # botão D.
        params = {"text": "DELETAR",
            "width": 10,
            #"command": self._salvar_aluno
            }
        Button(btn_frame, params).grid({"row": 2, "column": 0, "pady": 8})
        
    def setForm(self, table_name, columns):
        # deleta formulário anterior (se existente)
        if(self.form is not None):
            self.form.destroy()
        
        # frame para incluir os nomes das colunas + edits do formulário
        wrap_frame = Frame(self.form_frame)
        wrap_frame.grid(row=0, column=0, sticky="nsew", padx=8, pady=4)
        # inclui nomes das colunas + edits
        self.edits = []
        for c in range(0, len(columns)):
            # inclui label (== nome da coluna)
            Label(wrap_frame, text="{}: ".format(columns[c])).grid(row=c, column=0, sticky="w", pady=2)
            # inclui edit (salvar no array para ler dps)
            edit = Entry(wrap_frame)
            self.edits.append(edit)
            edit.grid(row=c, column=1, sticky="e", pady=2)
            
    def setFormValues(self, values):
        print(self.edits)
        for ix, edit in enumerate(self.edits):
            edit.delete(0, END)
            edit.insert(0, values[ix])
            
            
        





