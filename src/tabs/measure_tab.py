try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def measure(self, TNotebook1):

    ##################################
    # 	          TAB 3     		 #
    ##################################
	
    self.TNotebook1_t3 = tk.Frame(TNotebook1)
    self.TNotebook1.add(self.TNotebook1_t3, padding=3)
    self.TNotebook1.tab(2, text="Measure",compound="left",underline="-1",)

    self.Message1 = tk.Message(self.TNotebook1_t3)
    self.Message1.place(relx=0.351, rely=0.13, relheight=0.154, relwidth=0.3)

    self.Message1.configure(text='''Message''')
    self.Message1.configure(width=171)