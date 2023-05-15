import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    
    PAD = 10
    
    def __init__(self, controller) -> None:
        super().__init__()  # initialise superclass e.g. an instance of Tk class
        self.title("PyCalc 1.0")
        self.controller = controller
        self.value_var = tk.StringVar()
        self._make_main_frame()
        self._make_entry()
        
    def main(self):
        self.mainloop()
        
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
                    
        
    def _make_entry(self):
        ent = ttk.Entry(self.main_frm, textvariable=self.value_var)
        ent.pack()
        
        
        