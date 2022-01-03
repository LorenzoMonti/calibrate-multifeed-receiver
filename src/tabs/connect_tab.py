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

import Utils
import logging

def connect(self, TNotebook1, config_interface, config_file):

    # Elements coordinates
    x_label = 0.035
    h_label = 15
    w_label = 160

    x_text = 0.323
    h_text = 0.029
    w_text = 0.291

    y_button = 0.699
    h_button = 40
    w_button = 150
    
    ##################################
    # 	          TAB 1	        	 #
    ##################################    
    
    self.TNotebook1.add(self.TNotebook1_t1, padding=3)
    self.TNotebook1.tab(0, text="Connection",compound="left",underline="-1",)

    # label
    self.LabelConnect = tk.Label(self.TNotebook1_t1)
    self.LabelConnect.place(relx=x_label, rely=0.042, height=h_label, width=w_label)
    self.LabelConnect.configure(text='''Interface''')

    self.LabelEntryMenu =  tk.Label(self.TNotebook1_t1)
    self.LabelEntryMenu.place(relx=0.008, rely=0.795, height=h_label, width=w_label)
    self.LabelEntryMenu.configure(text='''Interface selected''')

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

    self.Label1Connect = tk.Label(self.TNotebook1_t1)
    self.Label1Connect.place(relx=x_label, rely=0.255, height=h_label, width=w_label)
    self.Label1Connect.configure(text='''GPIB''')

    self.Label2Connect = tk.Label(self.TNotebook1_t1)
    self.Label2Connect.place(relx=x_label, rely=0.326, height=h_label, width=w_label)
    self.Label2Connect.configure(text='''Remote ETH connection''')

    self.Label3Connect = tk.Label(self.TNotebook1_t1)
    self.Label3Connect.place(relx=x_label, rely=0.397, height=h_label, width=w_label)
    self.Label3Connect.configure(text='''Local ETH connection''')

    self.Entry1Connect = tk.Entry(self.TNotebook1_t1)
    self.Entry1Connect.place(relx=x_text, rely=0.255, relheight=h_text, relwidth=w_text)
    self.Entry1Connect.configure(background="white")
    self.Entry1Connect.configure(font="TkTextFont")
    self.Entry1Connect.configure(selectbackground="blue")
    self.Entry1Connect.configure(selectforeground="white")
    self.Entry1Connect.insert(0, config_interface["gpib"])

    self.Entry2Connect = tk.Entry(self.TNotebook1_t1)
    self.Entry2Connect.place(relx=x_text, rely=0.326, relheight=h_text, relwidth=w_text)
    self.Entry2Connect.configure(background="white")
    self.Entry2Connect.configure(font="TkTextFont")
    self.Entry2Connect.configure(selectbackground="blue")
    self.Entry2Connect.configure(selectforeground="white")
    self.Entry2Connect.insert(0, config_interface["remote_eth"])

    self.Entry3Connect = tk.Entry(self.TNotebook1_t1)
    self.Entry3Connect.place(relx=x_text, rely=0.397, relheight=h_text, relwidth=w_text)
    self.Entry3Connect.configure(background="white")
    self.Entry3Connect.configure(font="TkTextFont")
    self.Entry3Connect.configure(selectbackground="blue")
    self.Entry3Connect.configure(selectforeground="white")
    self.Entry3Connect.insert(0, config_interface["local_eth"])

    def write_config():
        config_interface = {
            "gpib": str(self.Entry1Connect.get()),
            "remote_eth": str(self.Entry2Connect.get()),
            "local_eth": str(self.Entry3Connect.get())
        }
        try:
            Utils.write_config_file("../config/config_interface.json", config_interface)
            #self.Text1.insert(tk.END, "Configuration file written successfully \n")
            logging.info(__name__ + ' : Configuration file written successfully')

        except:
            #self.Text1.insert(tk.END, "Error writing configuration file \n")
            logging.error(__name__ + ' : Error writing configuration file')

    self.ButtonConnect = tk.Button(self.TNotebook1_t1)
    self.ButtonConnect.place(relx=0.035, rely=y_button, height=h_button, width=w_button)
    self.ButtonConnect.configure(borderwidth="2")
    self.ButtonConnect.configure(command=write_config)
    self.ButtonConnect.configure(text='''Write configuration''')