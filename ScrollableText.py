"""
    Class ScrollableText
    Authors: group UFRPE - BSI - IAAD - 2022
    Disclaimer: use it on your own risk!
    License: feel free to mess up with it at will, provided you display this header in your code!
"""

from tkinter import *
import tkinter.ttk as ttk


class ScrollableText(Text):

    def __init__(self, frame, max_height = 5):

        super(ScrollableText, self).__init__(frame)

        #   position Text widget on the left side of frame
        self.grid({"row": 0, "column": 0, "sticky": EW})
        #   add vertical scrollbar
        vscroll = ttk.Scrollbar(frame, orient=VERTICAL, command=self.yview)
        vscroll.grid({"row": 0, "column": 1, "sticky": NS})
        self.configure(yscrollcommand=vscroll.set, height=max_height)
        #   configure font for text
        self.tag_configure("font", font=('Arial', 10))
        #   make widget non-editable without disabling it
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





