import time
import tkinter as tk
from tkinter import ttk


class InfoFrame(ttk.Frame):
    def __init__(self, window: tk.Tk):
        super().__init__(window)
        self.grid()
        self.lbl = tk.Label(self, text="Введите что-то:", padx=10, pady=10)
        self.lbl.grid(column=0, row=0)
        self.ent = ttk.Entry(self, width=20)
        self.ent.grid(column=0, row=1)

    def get_data(self):
        text = self.ent.get()
        return text


class Parser:
    def __init__(self, frm: InfoFrame, bar: ttk.Progressbar):
        self.cnt = 0
        self.bar = bar
        self.frm = frm

    def parse(self):
        print(self.frm.get_data())
        self.cnt = 0
        for i in range(100):
            self.inc_cnt()
            time.sleep(0.01)

    def inc_cnt(self):
        self.cnt += 1
        self.bar['value'] = self.cnt

