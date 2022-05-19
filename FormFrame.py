"""
    Class FormFrame
    Cria formulário dinâmicamente para as operações CRUD em uma tabela do BD
    Autor: grupo UFRPE - BSI - IAAD - 2022
    ISENÇÃO DE RESPONSABILIDADE: o risco do uso é todo seu!
    Licença: use e/ou modifique o código à vontade, mas não apague esse cabeçalho.
"""

from tkinter import *

class FormFrame:
    
    def __init__(self, frame, repo, callback):
        self.repo = repo
        self.form = None
        self.callback = callback    # callback para retorno das operações CRUD
        
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
            "command": self.crudInsert
            }
        Button(btn_frame, params).grid({"row": 0, "column": 0, "pady": 8})
        # botão U.
        params = {"text": "ATUALIZAR",
            "width": 10,
            "command": self.crudUpdate
            }
        Button(btn_frame, params).grid({"row": 1, "column": 0, "pady": 8})
        # botão D.
        params = {"text": "DELETAR",
            "width": 10,
            "command": self.crudDelete
            }
        Button(btn_frame, params).grid({"row": 2, "column": 0, "pady": 8})
        
    def setForm(self, table_name, columns, pks):
        # salva nome da tabela, colunas e pks para operações CRUD
        self.table_name = table_name
        self.columns = columns
        self.pks = pks
        self.values = None      # usado em CRUD UPDATE
        
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
            
    # insere valores (@values) nos edits do formulário
    def setFormValues(self, values):
        # salvar dados originais pra usar em CRUD UPDATE
        self.values = self.addQuotes(values)
        for ix, edit in enumerate(self.edits):
            edit.delete(0, END)
            edit.insert(0, values[ix])
            
    # Operação CRUD - inserção
    def crudInsert(self):
        data = self.readFormData()
        query = "INSERT INTO {} VALUES({})".format(self.table_name, ",".join(data))
        if self.repo.execute(query) is False:
            return
        self.callback(self.table_name)
    
    def crudUpdate(self):
        # aborta se nenhuma seleção feita
        if self.values is None:
            return;
        data = self.readFormData()
        # pega os campos e valores que mudaram e constrói os pares campo = valor para a cláusula SET
        print(self.values)
        set = list(("{} = {}".format(self.columns[x], data[x]) for x in range(0, len(data)) if data[x] != self.values[x]))
        # aborta se nada mudou
        if len(set) == 0:
            return
        set = ", ".join(set)
        if len(self.pks) > 0:   # a tabela tem Primary Keys
            # constrói cláusula WHERE com PKs
            # pega os valores correspondentes às PKs
            """
                OBS.:   o update dá em nada se o usuário mudou o valor da PK para um valor inexistente na tabela;
                        atualiza a entrada correspondente à PK, se o usuário mudou o valor da PK para uma outra chave
                        primária existente
            """
            where = list((self.values[x] for x in range(0, len(self.columns)) if self.columns[x] in self.pks))
            # cria os pares pk = valor
            where = list(("{} = {}".format(self.pks[x], where[x]) for x in range(0, len(self.pks))))
        else:   # a tabela não tem Primary Keys
            # constrói a cláusula WHERE com os valores originais
            where = list(("{} = {}".format(self.columns[x], self.values[x]) for x in range(0, len(self.values))))
                
        where = " AND ".join(where)
        query = "UPDATE {} SET {} WHERE {}".format(self.table_name, set, where)
        if self.repo.execute(query) is False:
            return
        self.callback(self.table_name)
    
    def crudDelete(self):
        # aborta se formulário em branco
        if self.values is None:
            return
        data = self.readFormData()
        if len(self.pks) == 0:
            # use todos os valores das colunas na cláusula WHERE se a tabela não tem PKs
            where = list(("{} = {}".format(self.columns[x], data[x]) for x in range(0, len(data))))
        else:
            # pega os valores correspondentes às PKs (valores originais)
            column_values = list((self.values[x] for x in range(0, len(self.columns)) if self.columns[x] in self.pks))
            # use os pares (pk, valor) se a tabela tem PKs
            where = list(("{} = {}".format(self.pks[x], column_values[x]) for x in range(0, len(self.pks))))

        where = " AND ".join(where)
        query = "DELETE FROM {} WHERE {}".format(self.table_name, where)
        if self.repo.execute(query) is False:
            return
        self.callback(self.table_name)
        
    # lê dados dos edits
    def readFormData(self):
        data = []
        for edit in self.edits:
            data.append(edit.get())
        data = self.addQuotes(data)
        print(data)
        return data

    # adiciona aspas simples aos elementos da lista @dataList
    def addQuotes(self, dataList):
        return list((r"""'{}'""".format(element) for element in dataList))


