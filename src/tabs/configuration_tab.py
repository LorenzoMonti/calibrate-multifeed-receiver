from logging import disable
from tkinter import Tk
from tkinter.constants import DISABLED
from tkinter.font import NORMAL
from tokenize import Double
from src import Anritsu_MS2830A as SPA
from src import Utils
import logging

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

def configuration(self, TNotebook1, config_interface, config_file):

    ##################################
    # 	          TAB 2	        	 #
    ##################################
    
    self.TNotebook1_t2 = ttk.Frame(TNotebook1)
    self.TNotebook1.add(self.TNotebook1_t2, padding=3)
    self.TNotebook1.tab(1, text="Configuration",compound="left",underline="-1",)

    # frame for the Select Interface
    self.configuration_frame = ttk.LabelFrame(self.TNotebook1_t2, text="Configuration", padding=(20, 10))
    self.configuration_frame.grid(
        row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
    )

    self.Label1 = ttk.Label(self.configuration_frame)
    self.Label1.grid(row=1, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label1.configure(text='''Start frequency''')

    self.Label2 = ttk.Label(self.configuration_frame)
    self.Label2.grid(row=2, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label2.configure(text='''Stop Frequency''')

    self.Label3 = ttk.Label(self.configuration_frame)
    self.Label3.grid(row=3, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label3.configure(text='''Sweep Trace Points''')

    self.Label4 = ttk.Label(self.configuration_frame)
    self.Label4.grid(row=4, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label4.configure(text='''Resolution Bandwith''')

    self.Label5 = ttk.Label(self.configuration_frame)
    self.Label5.grid(row=5, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label5.configure(text='''Video Bandwith''')

    self.Label6 = ttk.Label(self.configuration_frame)
    self.Label6.grid(row=6, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label6.configure(text='''Amplitude log scale''')

    self.Label7 = ttk.Label(self.configuration_frame)
    self.Label7.grid(row=7, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label7.configure(text='''Reference Level''')

    self.Label8 = ttk.Label(self.configuration_frame)
    self.Label8.grid(row=8, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label8.configure(text='''Zoom Spot Marker number''')
    
    self.Label9 = ttk.Label(self.configuration_frame)
    self.Label9.grid(row=9, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label9.configure(text='''Zoom Spot Marker type''')

    self.Label10 = ttk.Label(self.configuration_frame)
    self.Label10.grid(row=10, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label10.configure(text='''Manual commands''')

    # entry
    self.Entry1 = ttk.Entry(self.configuration_frame)
    self.Entry1.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry1.insert(0, config_file["start_freq"])

    self.Entry2 = ttk.Entry(self.configuration_frame)
    self.Entry2.grid(row=2, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry2.insert(0, config_file["stop_freq"])

    self.Entry3 = ttk.Entry(self.configuration_frame)
    self.Entry3.grid(row=3, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry3.insert(0, config_file["sweep_trace_points"])

    self.Entry4 = ttk.Entry(self.configuration_frame)
    self.Entry4.grid(row=4, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry4.insert(0, config_file["resolution_bandwith"])

    self.Entry5 = ttk.Entry(self.configuration_frame)
    self.Entry5.grid(row=5, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry5.insert(0, config_file["video_bandwith"])

    self.Entry6 = ttk.Entry(self.configuration_frame)
    self.Entry6.grid(row=6, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry6.insert(0, config_file["amplitude_log_scale"])

    self.Entry7 = ttk.Entry(self.configuration_frame)
    self.Entry7.grid(row=7, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry7.insert(0, config_file["reference_level"])

    self.Entry8 = ttk.Entry(self.configuration_frame)
    self.Entry8.grid(row=8, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry8.insert(0, config_file["zoom_spot_marker"][0])

    self.Entry9 = ttk.Entry(self.configuration_frame)
    self.Entry9.grid(row=9, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Entry9.insert(0, config_file["zoom_spot_marker"][1])

    self.Entry10 = ttk.Entry(self.configuration_frame)
    self.Entry10.grid(row=10, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")

    # frame for the buttons configuration
    self.button_config_frame = ttk.LabelFrame(self.TNotebook1_t2, text="Actions", padding=(20, 10))
    self.button_config_frame.grid(
        row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
    )

    # function for button "Write configuration"
    def write_conf():
        config_file = {
            "start_freq": float(self.Entry1.get()),
            "stop_freq": float(self.Entry2.get()),
            "sweep_trace_points": int(self.Entry3.get()),
            "resolution_bandwith": float(self.Entry4.get()),
            "video_bandwith": float(self.Entry5.get()),
            "amplitude_log_scale": int(self.Entry6.get()),
            "reference_level": int(self.Entry7.get()),
            "zoom_spot_marker": [int(self.Entry8.get()), self.Entry9.get()]
        }
        try:
            Utils.write_config_file(Utils.HOME_DIRECTORY + "/config_MS2830A.json", config_file)
            self.Text1.insert(tk.END, "\nConfiguration file written successfully \n")
            logging.info(__name__ + ' : Configuration file written successfully')

        except:
            self.Text1.insert(tk.END, "\nError writing configuration file \n")
            logging.error(__name__ + ' : Error writing configuration file')
        
    self.Button1 = ttk.Button(self.button_config_frame)
    self.Button1.grid(row=0, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Button1.configure(command=write_conf)
    self.Button1.configure(text='''Write configuration''')

    def set_conf():
        try:
            config_file = Utils.read_config_file(Utils.HOME_DIRECTORY + "config_MS2830A.json")
            config_interface = Utils.read_config_file(Utils.HOME_DIRECTORY + "config_interface.json")
            self.instr = SPA.Anritsu_MS2830A("Anritsu_MS2830A",config_interface[self.selected_interface.get()])
            log_list = Utils.set_SPA_for_measure(self.instr, config_file, self.Entry10.get())
            self.Text1.insert(tk.END, "\nConfiguration\n")
            for log in log_list:
                self.Text1.insert(tk.END, "\t" + log + "\n")
            
            self.TNotebook1.tab(2, state=NORMAL)
            self.Button3.config(state=NORMAL)
        except:
            self.Text1.insert(tk.END, "\nConnection problem\n")

    self.Button2 = ttk.Button(self.button_config_frame)
    self.Button2.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Button2.configure(command=set_conf)
    self.Button2.configure(text='''Set configuration''')

    def plot_data():
        trace = self.instr.get_trace(1) # Get trace
        Utils.plot_lineplot(trace)
        self.Text1.insert(tk.END, "\nData plotted\n")

    self.Button3 = ttk.Button(self.button_config_frame)
    self.Button3.grid(row=2, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Button3.configure(command=plot_data)
    self.Button3.configure(state=DISABLED)
    self.Button3.configure(text='''Plot data''')

    # frame for the Log output
    self.log_conf_frame = ttk.LabelFrame(self.TNotebook1_t2, text="Log", padding=(20, 10))
    self.log_conf_frame.grid(
        row=0, column=2, padx=(20, 10), pady=(20, 10), sticky="nsew"
    )

    # text for log output
    self.Text1 = tk.Text(self.log_conf_frame)
    self.scrollLog2 = ttk.Scrollbar(self.log_conf_frame)
    self.scrollLog2.pack(side="right", fill="y")
    self.Text1.configure(yscrollcommand=self.scrollLog2.set)
    self.Text1.pack(expand=True, fill="both")