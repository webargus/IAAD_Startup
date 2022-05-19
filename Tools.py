"""
    Descrição:
        Referência estática à janela principal incluindo método para centrar a janela na tela
    Autor:
        Grupo UFRPE - BSI - IAAD  - 2022.1
    Licença:
        mantenha esse cabeçalho no seu código e sinta-se à vontade pra bagunçar este código
    ISENÇÃO DE RESPONSABILIDADE:
        O risco do uso é todo seu!
"""

class Tools:

    master = None                # static member to retrieve reference to root window
    _screen_width = None
    _screen_height = None

    @staticmethod
    def root(win):
        Tools.master = win
        Tools._screen_width = win.winfo_screenwidth()
        Tools._screen_height = win.winfo_screenheight()

    # centra janela na tela (client view)
    @staticmethod
    def center_window(win, width, height):
        # chama update_idletasks antes de capturar a geometria,
        # para garantir que os resultados retornados estão corretos
        win.update_idletasks()
        x = (Tools._screen_width // 2) - (width // 2)
        y = (Tools._screen_height // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))








