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

from tkinter import ttk

from src import Utils
import logging

def connect(self, TNotebook1, config_interface):

    ##################################
    # 	          TAB 1	        	 #
    ##################################    
    
    self.TNotebook1.add(self.TNotebook1_t1, padding=3)
    self.TNotebook1.tab(0, text="Connection",compound="left",underline="-1",)

    # label
    
    # frame for the Select Interface
    self.select_frame = ttk.LabelFrame(self.TNotebook1_t1, text="Select interface", padding=(20, 10))
    self.select_frame.grid(
        row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
    )

    self.LabelConnect = ttk.Label(self.select_frame)
    self.LabelConnect.grid(row=1, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.LabelConnect.configure(text='''Interface''')

    self.LabelEntryMenu =  ttk.Label(self.select_frame)
    self.LabelEntryMenu.grid(row=2, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.LabelEntryMenu.configure(text='''Interface selected''')

    options = [interface_key for interface_key, interface_value in config_interface.items()]
    self.selected_interface = tk.StringVar() # Dropmenu variable (store option choice)
    #self.selected_interface.set(options[0]) # first element (GPIB) is selected as default
    
    self.drop = ttk.OptionMenu(self.select_frame, self.selected_interface, *options)
    self.drop.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="nsew")

    self.EntryMenu = ttk.Entry(self.select_frame, textvariable= self.selected_interface)
    self.EntryMenu.grid(row=2, column=1, padx=(20, 10), pady=(20, 0), sticky="ew") 

    self.config_frame = ttk.LabelFrame(self.TNotebook1_t1, text="Configure interface", padding=(20, 10))
    self.config_frame.grid(
        row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="new"
    )

    self.Label1Connect = ttk.Label(self.config_frame)
    self.Label1Connect.grid(row=3, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label1Connect.configure(text='''GPIB''')

    self.Label2Connect = ttk.Label(self.config_frame)
    self.Label2Connect.grid(row=4, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label2Connect.configure(text='''Remote ETH connection''')

    self.Label3Connect = ttk.Label(self.config_frame)
    self.Label3Connect.grid(row=5, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label3Connect.configure(text='''Local ETH connection''')

    self.Entry1Connect = ttk.Entry(self.config_frame)
    self.Entry1Connect.grid(row=3, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry1Connect.insert(0, config_interface["gpib"])

    self.Entry2Connect = ttk.Entry(self.config_frame)
    self.Entry2Connect.grid(row=4, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry2Connect.insert(0, config_interface["remote_eth"])

    self.Entry3Connect = ttk.Entry(self.config_frame)
    self.Entry3Connect.grid(row=5, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry3Connect.insert(0, config_interface["local_eth"])
    
    # frame for the button
    self.button_conn_frame = ttk.LabelFrame(self.TNotebook1_t1, text="Actions", padding=(20, 10))
    self.button_conn_frame.grid(
        row=0, column=1, padx=(20, 10), pady=(150, 10), sticky="ew"
    )

    def write_config():
        config_interface = {
            "" : str(""),
            "gpib": str(self.Entry1Connect.get()),
            "remote_eth": str(self.Entry2Connect.get()),
            "local_eth": str(self.Entry3Connect.get())
        }
        try:
            Utils.write_config_file(Utils.HOME_DIRECTORY + "/config_interface.json", config_interface)
            self.EntryLog.insert(tk.END, "\nConfiguration file written successfully \n")
            logging.info(__name__ + ' : Configuration file written successfully')

        except:
            self.EntryLog.insert(tk.END, "\nError writing configuration file \n")
            logging.error(__name__ + ' : Error writing configuration file')


    self.ButtonConnect = ttk.Button(self.button_conn_frame)
    self.ButtonConnect.grid(row=7, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.ButtonConnect.configure(command=write_config)
    self.ButtonConnect.configure(text='''Write configuration''')
 
    # frame for the Log output
    self.log_conn_frame = ttk.LabelFrame(self.TNotebook1_t1, text="Log", padding=(20, 10))
    self.log_conn_frame.grid(
        row=0, column=2, padx=(20, 10), pady=(20, 10), sticky="nsew"
    )

    # text for log output    
    self.EntryLog = tk.Text(self.log_conn_frame)
    self.scrollLog1 = ttk.Scrollbar(self.log_conn_frame)
    self.scrollLog1.pack(side="right", fill="y")
    self.EntryLog.configure(yscrollcommand=self.scrollLog1.set)
    self.EntryLog.pack(expand=True, fill="both")

