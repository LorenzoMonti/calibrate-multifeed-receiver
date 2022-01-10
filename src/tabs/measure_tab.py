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
from tkinter import filedialog
from tkinter.constants import ACTIVE, DISABLED
from tkinter.font import NORMAL

import Utils
import csv
import time
import numpy as np
import beepy as bp

def measure(self, TNotebook1):

    ##################################
    # 	          TAB 3     		 #
    ##################################
	# Elements coordinates
    x_message = 0.351
    h_message = 0.054
    w_message = 0.3

    y_button = 0.739
    h_button = 40
    w_button = 150

    self._traces = list()
    num_measures = 5

    self.TNotebook1_t3 = tk.Frame(TNotebook1)
    self.TNotebook1.add(self.TNotebook1_t3, padding=3)
    self.TNotebook1.tab(2, text="Measure", compound="left", underline="-1")
    
    # frame for the Measure
    self.measure_frame = ttk.LabelFrame(self.TNotebook1_t3, text="Measures", padding=(20, 10))
    self.measure_frame.grid(
        row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
    )

    self.Message1 = tk.Message(self.measure_frame)
    self.Message1.grid(row=1, column=0, padx=(150, 150), pady=(50, 50), sticky="ew")
    self.Message1.configure(text='''Pc''', width=371)

    self.Message2 = tk.Message(self.measure_frame)
    self.Message2.grid(row=2, column=0, padx=(150, 150), pady=(50, 50), sticky="ew")
    self.Message2.configure(text='''Pc + m''', width=171)

    self.Message3 = tk.Message(self.measure_frame)
    self.Message3.grid(row=3, column=0, padx=(150, 150), pady=(50, 50), sticky="ew")
    self.Message3.configure(text='''Ph''', width=171)

    self.Message4 = tk.Message(self.measure_frame)
    self.Message4.grid(row=4, column=0, padx=(150, 150), pady=(50, 50), sticky="ew")
    self.Message4.configure(text='''Ph + m''', width=171)

    self.Message5 = tk.Message(self.measure_frame)
    self.Message5.grid(row=5, column=0, padx=(150, 150), pady=(50, 50), sticky="ew")
    self.Message5.configure(text='''Pc''', width=171)

    # function for event take_trace
    def take_trace(event):
        if event.char == ' ':
            if(len(self._traces) < num_measures):
                
                Utils.clear_message(self, len(self._traces)) # only for UI
                try:
                    self.TextMeasure1.insert(tk.END, "\nTaking trace...")
                    self._traces.append(self.instr.get_trace(1)) # Get trace
                    self.TextMeasure1.insert(tk.END, "\nData taken\n")
                    bp.beep(sound=1)
                except:
                    self.TextMeasure1.insert(tk.END, "\nConnection problem\n")                
            else:
                self.ButtonMeasure2.config(state=NORMAL)
                self.TextMeasure1.insert(tk.END, "\nAll measurements were successful\n")
                self.Message5.configure(background="#d9d9d9", font=("Helvetica",10))

    # frame for the buttons measure
    self.button_mea_frame = ttk.LabelFrame(self.TNotebook1_t3, text="Actions", padding=(20, 10))
    self.button_mea_frame.grid(
        row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
    )
    
    self.ButtonMeasure = ttk.Button(self.button_mea_frame)
    self.ButtonMeasure.grid(row=1, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.ButtonMeasure.configure(text='''Take measurement''', command = take_trace)
    
    def clear_measures():
        self._traces.clear()
        self.TextMeasure1.insert(tk.END, "\nMeasures cleared\n")
        Utils.clear_background(self)

    self.ButtonMeasure1 = ttk.Button(self.button_mea_frame)
    self.ButtonMeasure1.grid(row=2, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.ButtonMeasure1.configure(text='''Clear measurements''', command = clear_measures)

    def save_measures():

        # convert dBm in watts
        watt_traces = list()
        for trace in self._traces:
            watt_traces.append(np.array(list(Utils.getWatts(trace))))

        # get calculus
        dMeasure, drMeasure, Pc, PcPlusM, HpPlusM, Ph, Yvalue = Utils.getCalculus(watt_traces)
        # traspose rows in columns
        columns_trace = zip(self._traces[0], self._traces[1], self._traces[2], self._traces[3], self._traces[4], dMeasure, drMeasure, Pc, PcPlusM, HpPlusM, Ph, Yvalue) 

        # open file dialog
        file = filedialog.asksaveasfile(mode="w", defaultextension=".csv")
        if file is None:
            return

        # write CSV
        writer = csv.writer(file)        
        # titles
        writer.writerow(["RAW:Pc", "RAW:Pc + m", "RAW:Ph", "RAW:Ph + m", "RAW:Pc'", "dMeasure", "drMeasure", "Pc", "PcPlusM", "HpPlusM", "Ph", "Yvalue"]) 
        # traces and calculus
        for column_trace in columns_trace:
            writer.writerow(column_trace) 
        file.close()
        
        # write in log output
        self.TextMeasure1.insert(tk.END, "\nFile written succesfully\n")

    self.ButtonMeasure2 = ttk.Button(self.button_mea_frame)
    self.ButtonMeasure2.grid(row=3, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.ButtonMeasure2.configure(command=save_measures, text='''Save measurements''')
    self.ButtonMeasure2.config(state=DISABLED)

    # frame for the Log output
    self.log_mea_frame = ttk.LabelFrame(self.TNotebook1_t3, text="Log", padding=(20, 10))
    self.log_mea_frame.grid(
        row=0, column=2, padx=(20, 10), pady=(20, 10), sticky="nsew"
    )

    # text for log output
    self.TextMeasure1 = tk.Text(self.log_mea_frame)
    self.scrollLog3 = ttk.Scrollbar(self.log_mea_frame)
    self.scrollLog3.pack(side="right", fill="y")
    self.TextMeasure1.configure(yscrollcommand=self.scrollLog3.set)
    self.TextMeasure1.pack(expand=True, fill="both")


    # EVENTS
    self.TNotebook1_t3.bind_all("<space>", take_trace)
