import time
import threading
import tkinter as tk
from tkinter import ttk

from parse import InfoFrame, Parser


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x250')
        self.info_frame = InfoFrame(self)

        self.bar = ttk.Progressbar(self, length=130)
        self.bar.grid(column=0, row=2, pady=10, padx=30)

        self.btn_start = ttk.Button(self, command=self.start_action, text="Начать")
        self.btn_start.grid(column=0, row=3, pady=20, padx=30)

        self.btn_quit = ttk.Button(self, command=self.destroy, text="Выйти")
        self.btn_quit.grid(column=0, row=4, pady=0, padx=30)

        self.prs = Parser(self.info_frame, self.bar)

    def start_action(self):
        self.btn_start.config(state=tk.DISABLED)
        thread = threading.Thread(target=self.run_action)
        # print(threading.main_thread().name)
        # print(thread.name)
        thread.start()
        self.check_thread(thread)

    def check_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.check_thread(thread))
        else:
            self.btn_start.config(state=tk.NORMAL)

    def run_action(self):
        print("Запуск длительного действия...")
        self.prs.parse()
        print("Длительное действие завершено!")


if __name__ == "__main__":
    app = App()
    app.mainloop()

