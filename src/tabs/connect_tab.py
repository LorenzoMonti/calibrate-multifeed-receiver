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


def connect(self, TNotebook1, config_interface, config_file):

    # Elements coordinates
    x_label = 0.035
    h_label = 15
    w_label = 160

    x_text = 0.323
    h_text = 0.029
    w_text = 0.291

    y_button = 0.739
    h_button = 40
    w_button = 150
    
    ##################################
    # 	          TAB 1	        	 #
    ##################################    
    
    self.TNotebook1.add(self.TNotebook1_t1, padding=3)
    self.TNotebook1.tab(0, text="Connection",compound="left",underline="-1",)

    # label
    self.Label0 = tk.Label(self.TNotebook1_t1)
    self.Label0.place(relx=x_label, rely=0.042, height=h_label, width=w_label)
    self.Label0.configure(text='''Interface''')

    options = [interface_key for interface_key, interface_value in config_interface.items()]
    self.selected_interface = tk.StringVar() # Dropmenu variable (store option choice)
    self.selected_interface.set(options[0]) # first element (GPIB) is selected as default

    # text for log output    
    self.EntryMenu = tk.Entry(self.TNotebook1_t1, textvariable= self.selected_interface)
    self.EntryMenu.place(relx=0.035, rely=0.818, relheight=0.154, relwidth=0.94)
    self.EntryMenu.configure(background='#d9d9d9')
    self.EntryMenu.configure(font="TkTextFont")

    self.drop = tk.OptionMenu( self.TNotebook1_t1 , self.selected_interface, *options)
    self.drop.place(relx=x_text, rely=0.042, relheight=h_text, relwidth=w_text)