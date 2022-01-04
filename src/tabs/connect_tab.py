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

from tkinter import font
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
    
    # fonts
    font_label = ("Arial",10)
    font_title = ("Arial",12)

    ##################################
    # 	          TAB 1	        	 #
    ##################################    
    
    self.TNotebook1.add(self.TNotebook1_t1, padding=3)
    self.TNotebook1.tab(0, text="Connection",compound="left",underline="-1",)

    # label
    self.LabelTitle1 = tk.Label(self.TNotebook1_t1)
    self.LabelTitle1.place(relx=0.005, rely=0.004, height=h_label, width=w_label)
    self.LabelTitle1.configure(text='''Select interface''', font=font_title)

    self.LabelConnect = tk.Label(self.TNotebook1_t1)
    self.LabelConnect.place(relx=x_label, rely=0.042, height=h_label, width=w_label)
    self.LabelConnect.configure(text='''Interface''', font=font_label)

    self.LabelEntryMenu =  tk.Label(self.TNotebook1_t1)
    self.LabelEntryMenu.place(relx=x_label, rely=0.113, height=h_label, width=w_label)
    self.LabelEntryMenu.configure(text='''Interface selected''', font=font_label)

    options = [interface_key for interface_key, interface_value in config_interface.items()]
    self.selected_interface = tk.StringVar() # Dropmenu variable (store option choice)
    self.selected_interface.set(options[0]) # first element (GPIB) is selected as default
    
       
    self.EntryMenu = tk.Entry(self.TNotebook1_t1, textvariable= self.selected_interface)
    self.EntryMenu.place(relx=x_text, rely=0.113, relheight=h_text, relwidth=w_text) 
    self.EntryMenu.configure(background='#d9d9d9')
    self.EntryMenu.configure(font=font_label)

    self.drop = tk.OptionMenu( self.TNotebook1_t1 , self.selected_interface, *options)
    self.drop.place(relx=x_text, rely=0.042, relheight=h_text, relwidth=w_text)

    self.LabelTitle2 = tk.Label(self.TNotebook1_t1)
    self.LabelTitle2.place(relx=0.005, rely=0.204, height=h_label, width=w_label)
    self.LabelTitle2.configure(text='''Configure interfaces''', font=font_title)

    self.Label1Connect = tk.Label(self.TNotebook1_t1)
    self.Label1Connect.place(relx=x_label, rely=0.255, height=h_label, width=w_label)
    self.Label1Connect.configure(text='''GPIB''', font=font_label)

    self.Label2Connect = tk.Label(self.TNotebook1_t1)
    self.Label2Connect.place(relx=x_label, rely=0.326, height=h_label, width=w_label)
    self.Label2Connect.configure(text='''Remote ETH connection''', font=font_label)

    self.Label3Connect = tk.Label(self.TNotebook1_t1)
    self.Label3Connect.place(relx=x_label, rely=0.397, height=h_label, width=w_label)
    self.Label3Connect.configure(text='''Local ETH connection''', font=font_label)

    self.Entry1Connect = tk.Entry(self.TNotebook1_t1)
    self.Entry1Connect.place(relx=x_text, rely=0.255, relheight=h_text, relwidth=w_text)
    self.Entry1Connect.configure(background="white")
    self.Entry1Connect.configure(font=font_label)
    self.Entry1Connect.configure(selectbackground="blue")
    self.Entry1Connect.configure(selectforeground="white")
    self.Entry1Connect.insert(0, config_interface["gpib"])

    self.Entry2Connect = tk.Entry(self.TNotebook1_t1)
    self.Entry2Connect.place(relx=x_text, rely=0.326, relheight=h_text, relwidth=w_text)
    self.Entry2Connect.configure(background="white")
    self.Entry2Connect.configure(font=font_label)
    self.Entry2Connect.configure(selectbackground="blue")
    self.Entry2Connect.configure(selectforeground="white")
    self.Entry2Connect.insert(0, config_interface["remote_eth"])

    self.Entry3Connect = tk.Entry(self.TNotebook1_t1)
    self.Entry3Connect.place(relx=x_text, rely=0.397, relheight=h_text, relwidth=w_text)
    self.Entry3Connect.configure(background="white")
    self.Entry3Connect.configure(font=font_label)
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
            self.EntryLog.insert(tk.END, "Configuration file written successfully \n")
            logging.info(__name__ + ' : Configuration file written successfully')

        except:
            self.EntryLog.insert(tk.END, "Error writing configuration file \n")
            logging.error(__name__ + ' : Error writing configuration file')

    self.ButtonConnect = tk.Button(self.TNotebook1_t1)
    self.ButtonConnect.place(relx=0.035, rely=y_button, height=h_button, width=w_button)
    self.ButtonConnect.configure(borderwidth="2")
    self.ButtonConnect.configure(command=write_config)
    self.ButtonConnect.configure(text='''Write configuration''', font=font_label)

    # text for log output    
    self.EntryLog = tk.Text(self.TNotebook1_t1)
    self.scrollLog1 = tk.Scrollbar(self.TNotebook1_t1)
    self.EntryLog.configure(yscrollcommand=self.scrollLog1.set)
    self.EntryLog.place(relx=0.035, rely=0.818, relheight=0.154, relwidth=0.94) 
    self.EntryLog.configure(background='#d9d9d9')
    self.EntryLog.configure(font="TkTextFont")