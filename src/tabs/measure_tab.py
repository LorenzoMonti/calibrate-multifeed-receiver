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
from tkinter import messagebox
from tkinter.constants import ACTIVE, DISABLED
from tkinter.font import NORMAL

from src import Utils
import csv
import datetime
from threading import *
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
    self.Message3.configure(text='''Ph + m''', width=171)

    self.Message4 = tk.Message(self.measure_frame)
    self.Message4.grid(row=4, column=0, padx=(150, 150), pady=(50, 50), sticky="ew")
    self.Message4.configure(text='''Ph''', width=171)

    self.Message5 = tk.Message(self.measure_frame)
    self.Message5.grid(row=5, column=0, padx=(150, 150), pady=(50, 50), sticky="ew")
    self.Message5.configure(text='''Pc''', width=171)

    # frame for the setting measure
    self.setting_mea_frame = ttk.LabelFrame(self.TNotebook1_t3, text="Settings", padding=(20, 10))
    self.setting_mea_frame.grid(
        row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="new"
    )
    
    #label
    self.Label1 = ttk.Label(self.setting_mea_frame)
    self.Label1.grid(row=1, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label1.configure(text='''Channel''')

    self.Label2 = ttk.Label(self.setting_mea_frame)
    self.Label2.grid(row=2, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label2.configure(text='''Polarization''')

    self.Label3 = ttk.Label(self.setting_mea_frame)
    self.Label3.grid(row=3, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label3.configure(text='''Tc''')
    
    self.Label4 = ttk.Label(self.setting_mea_frame)
    self.Label4.grid(row=4, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label4.configure(text='''Th''')

    # entry
    self.MeasureEntry1 = ttk.Entry(self.setting_mea_frame)
    self.MeasureEntry1.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")

    self.MeasureEntry2 = ttk.Entry(self.setting_mea_frame)
    self.MeasureEntry2.grid(row=2, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")

    self.MeasureEntry3 = ttk.Entry(self.setting_mea_frame)
    self.MeasureEntry3.grid(row=3, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")

    self.MeasureEntry4 = ttk.Entry(self.setting_mea_frame)
    self.MeasureEntry4.grid(row=4, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")
    
    # frame for the bound measure
    self.bound_mea_frame = ttk.LabelFrame(self.TNotebook1_t3, text="Bounds", padding=(20, 10))
    self.bound_mea_frame.grid(
        row=0, column=1, padx=(20, 10), pady=(50, 10), sticky="ew"
    )
    #label
    self.LabelBound1 = ttk.Label(self.bound_mea_frame)
    self.LabelBound1.grid(row=1, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.LabelBound1.configure(text='''Lower bound''')

    self.Label2 = ttk.Label(self.bound_mea_frame)
    self.Label2.grid(row=2, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.Label2.configure(text='''Upper bound''')

    # entry
    self.BoundEntry1 = ttk.Entry(self.bound_mea_frame)
    self.BoundEntry1.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")

    self.BoundEntry2 = ttk.Entry(self.bound_mea_frame)
    self.BoundEntry2.grid(row=2, column=1, padx=(20, 10), pady=(20, 0), sticky="ew")

    # frame for the buttons measure
    self.button_mea_frame = ttk.LabelFrame(self.TNotebook1_t3, text="Actions", padding=(20, 10))
    self.button_mea_frame.grid(
        row=0, column=1, padx=(20, 10), pady=(500, 10), sticky="ew"
    )
    
    # function for button take_trace
    def take_trace():
        # disable button frame during get_threading_trace
        #for child in self.button_mea_frame.winfo_children():
        #    child.configure(state='disable')
        trace_handler()
        
        
    def trace_handler():
        if(len(self._traces) < num_measures):
            try:
                self.TextMeasure1.insert(tk.END, "\nTaking trace...")
                thread_trace=Thread(target=get_threading_trace, args=(1,))
                thread_trace.start()   
            except:
                self.TextMeasure1.insert(tk.END, "\nConnection problem\n")    
        else:
            
            # convert dBm in watts
            watt_traces = list()
            for trace in self._traces:
                watt_traces.append(np.array(list(Utils.getWatts(trace))))
            # get frequency
            self.frequency = Utils.calcFrequency() 
            # get calculus
            self.dMeasure, self.drMeasure, self.Pc, self.PcPlusM, self.PhPlusM, self.Ph, self.Yvalue, self.Trx, self.Tm, self.Thm = Utils.getCalculus(watt_traces, float(self.MeasureEntry3.get()), float(self.MeasureEntry4.get()))
            # traspose rows in columns
            self.columns_trace = zip(self.frequency, self._traces[0], self._traces[1], self._traces[2], 
                                self._traces[3], self._traces[4], self.dMeasure, self.drMeasure, 
                                self.Pc, self.PcPlusM, self.PhPlusM, self.Ph, self.Yvalue, self.Trx, self.Tm, self.Thm) 


            Utils.plot_results(self.Trx, self.Tm, self.drMeasure, (self.Tm/self.Thm), float(self.BoundEntry1.get()), float(self.BoundEntry2.get()))
            self.ButtonMeasure2.config(state=NORMAL)
            self.TextMeasure1.insert(tk.END, "\nAll measurements were successful\n")
            self.Message5.configure(background="#d9d9d9", font=("Helvetica",10))

    def get_threading_trace(trace_SA):
        trace_thread = self.instr.get_trace(trace_SA)
        Utils.clear_message(self, len(self._traces)) # only for UI            
        self._traces.append(trace_thread)
        self.TextMeasure1.insert(tk.END, "\nData taken\n")
        #for child in self.button_mea_frame.winfo_children():
        #    child.configure(state='enable')
        bp.beep(sound=1)

    # buttons
    self.ButtonMeasure = ttk.Button(self.button_mea_frame)
    self.ButtonMeasure.grid(row=6, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.ButtonMeasure.configure(text='''Take measurement''', command = take_trace)
    
    def clear_measures():
        self._traces.clear()
        self.ButtonMeasure2.config(state=DISABLED)
        self.TextMeasure1.insert(tk.END, "\nMeasures cleared\n")
        Utils.clear_background(self)

    self.ButtonMeasure1 = ttk.Button(self.button_mea_frame)
    self.ButtonMeasure1.grid(row=7, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
    self.ButtonMeasure1.configure(text='''Clear measurements''', command = clear_measures)

    def save_measures():

        # acceptable drift
        if(Utils.acceptable_drift(self.drMeasure, self.Tm, self.Thm, float(self.BoundEntry1.get()), float(self.BoundEntry2.get()))):    
            # open file dialog
            file = filedialog.asksaveasfile(mode="w", defaultextension=".csv")
            if file is None:
                return

            # write CSV
            writer = csv.writer(file)        
            # Channel and Polarization
            writer.writerow(["Date/hour: " + str(datetime.datetime.now()),"Channel: " + str(self.MeasureEntry1.get()), "Polarization: " + str(self.MeasureEntry2.get())])
            # titles
            writer.writerow(["Frequency","RAW:Pc", "RAW:Pc + m", "RAW:Ph + m", "RAW:Ph", "RAW:Pc'", "dMeasure", "drMeasure", "Pc", "PcPlusM", "PhPlusM", "Ph", "Yvalue", "Trx", "Tm", "Thm"])  
            # traces and calculus
            for column_trace in self.columns_trace:
                writer.writerow(column_trace) 
            file.close()
            
            # write in log output
            self.TextMeasure1.insert(tk.END, "\nFile written succesfully\n")
        else:
            messagebox.showwarning("Warning","Based on bounds setted, drift has been detected")

    self.ButtonMeasure2 = ttk.Button(self.button_mea_frame)
    self.ButtonMeasure2.grid(row=8, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")
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

    # function for event take_trace
    def take_trace(event):
        if event.char == ' ':
            trace_handler()    
    # EVENTS
    self.TNotebook1_t3.bind_all("<space>", take_trace)
