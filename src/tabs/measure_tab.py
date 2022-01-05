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
    self.TNotebook1.tab(2, text="Measure",compound="left",underline="-1",)

    self.Message1 = tk.Message(self.TNotebook1_t3)
    self.Message1.place(relx=x_message, rely=0.08, relheight=h_message, relwidth=w_message)
    self.Message1.configure(text='''Pc''', width=171)

    self.Message2 = tk.Message(self.TNotebook1_t3)
    self.Message2.place(relx=x_message, rely=0.18, relheight=h_message, relwidth=w_message)
    self.Message2.configure(text='''Pc + m''', width=171)

    self.Message3 = tk.Message(self.TNotebook1_t3)
    self.Message3.place(relx=x_message, rely=0.28, relheight=h_message, relwidth=w_message)
    self.Message3.configure(text='''Ph''', width=171)

    self.Message4 = tk.Message(self.TNotebook1_t3)
    self.Message4.place(relx=x_message, rely=0.38, relheight=h_message, relwidth=w_message)
    self.Message4.configure(text='''Ph + m''', width=171)

    self.Message5 = tk.Message(self.TNotebook1_t3)
    self.Message5.place(relx=x_message, rely=0.48, relheight=h_message, relwidth=w_message)
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

    
    def clear_measures():
        self._traces.clear()
        self.TextMeasure1.insert(tk.END, "\nMeasures cleared\n")
        Utils.clear_background(self)

    self.ButtonMeasure1 = tk.Button(self.TNotebook1_t3)
    self.ButtonMeasure1.place(relx=0.035, rely=y_button, height=h_button, width=w_button)
    self.ButtonMeasure1.configure(borderwidth="2", text='''Clear measurements''', command = clear_measures)

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

    self.ButtonMeasure2 = tk.Button(self.TNotebook1_t3)
    self.ButtonMeasure2.place(relx=0.335, rely=y_button, height=h_button, width=w_button)
    self.ButtonMeasure2.configure(borderwidth="2")
    self.ButtonMeasure2.configure(command=save_measures)
    self.ButtonMeasure2.config(state=DISABLED)
    self.ButtonMeasure2.configure(text='''Save measurements''')

    # text for log output
    self.TextMeasure1 = tk.Text(self.TNotebook1_t3)
    self.scrollMeasure1 = tk.Scrollbar(self.TNotebook1_t3)
    self.TextMeasure1.configure(yscrollcommand=self.scrollMeasure1.set)
    self.TextMeasure1.place(relx=0.035, rely=0.818, relheight=0.154, relwidth=0.94)
    self.TextMeasure1.configure(background='#d9d9d9')
    self.TextMeasure1.configure(font="TkTextFont")


    # EVENTS
    self.TNotebook1_t3.bind_all("<space>", take_trace)
