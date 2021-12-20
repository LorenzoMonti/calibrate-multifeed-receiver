import Anritsu_MS2830A as SPA
import Utils

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

def configuration(self, TNotebook1, config_interface, config_file):

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
    # 	          TAB 2	        	 #
    ##################################
    
    self.TNotebook1_t2 = tk.Frame(TNotebook1)
    self.TNotebook1.add(self.TNotebook1_t2, padding=3)
    self.TNotebook1.tab(1, text="Configuration",compound="left",underline="-1",)

    self.Label1 = tk.Label(self.TNotebook1_t2)
    self.Label1.place(relx=x_label, rely=0.042, height=h_label, width=w_label)
    self.Label1.configure(text='''Start frequency''')

    self.Label2 = tk.Label(self.TNotebook1_t2)
    self.Label2.place(relx=x_label, rely=0.113, height=h_label, width=w_label)
    self.Label2.configure(text='''Stop Frequency''')

    self.Label3 = tk.Label(self.TNotebook1_t2)
    self.Label3.place(relx=x_label, rely=0.184, height=h_label, width=w_label)
    self.Label3.configure(text='''Center Frequency''')

    self.Label4 = tk.Label(self.TNotebook1_t2)
    self.Label4.place(relx=x_label, rely=0.255, height=h_label, width=w_label)
    self.Label4.configure(text='''Sweep Trace Points''')

    self.Label5 = tk.Label(self.TNotebook1_t2)
    self.Label5.place(relx=x_label, rely=0.326, height=h_label, width=w_label)
    self.Label5.configure(text='''Resolution Bandwith''')

    self.Label6 = tk.Label(self.TNotebook1_t2)
    self.Label6.place(relx=x_label, rely=0.397, height=h_label, width=w_label)
    self.Label6.configure(text='''Visual Bandwith''')

    self.Label7 = tk.Label(self.TNotebook1_t2)
    self.Label7.place(relx=x_label, rely=0.468, height=h_label, width=w_label)
    self.Label7.configure(text='''Amplitude log scale''')

    self.Label8 = tk.Label(self.TNotebook1_t2)
    self.Label8.place(relx=x_label, rely=0.539, height=h_label, width=w_label)
    self.Label8.configure(text='''Reference Level''')

    self.Label9 = tk.Label(self.TNotebook1_t2)
    self.Label9.place(relx=x_label, rely=0.61, height=h_label, width=w_label)
    self.Label9.configure(text='''Zoom Spot Marker number''')
    
    self.Label10 = tk.Label(self.TNotebook1_t2)
    self.Label10.place(relx=x_label, rely=0.68, height=h_label, width=w_label)
    self.Label10.configure(text='''Zoom Spot Marker type''')

    # entry
    self.Entry1 = tk.Entry(self.TNotebook1_t2)
    self.Entry1.place(relx=x_text, rely=0.042, relheight=h_text, relwidth=w_text)
    self.Entry1.configure(background="white")
    self.Entry1.configure(font="TkTextFont")
    self.Entry1.configure(selectbackground="blue")
    self.Entry1.configure(selectforeground="white")
    self.Entry1.insert(0, config_file["start_freq"])

    self.Entry2 = tk.Entry(self.TNotebook1_t2)
    self.Entry2.place(relx=x_text, rely=0.113, relheight=h_text, relwidth=w_text)
    self.Entry2.configure(background="white")
    self.Entry2.configure(font="TkTextFont")
    self.Entry2.configure(selectbackground="blue")
    self.Entry2.configure(selectforeground="white")
    self.Entry2.insert(0, config_file["stop_freq"])

    self.Entry3 = tk.Entry(self.TNotebook1_t2)
    self.Entry3.place(relx=x_text, rely=0.184, relheight=h_text, relwidth=w_text)
    self.Entry3.configure(background="white")
    self.Entry3.configure(font="TkTextFont")
    self.Entry3.configure(selectbackground="blue")
    self.Entry3.configure(selectforeground="white")
    self.Entry3.insert(0, config_file["center_freq"])


    self.Entry4 = tk.Entry(self.TNotebook1_t2)
    self.Entry4.place(relx=x_text, rely=0.255, relheight=h_text, relwidth=w_text)
    self.Entry4.configure(background="white")
    self.Entry4.configure(font="TkTextFont")
    self.Entry4.configure(selectbackground="blue")
    self.Entry4.configure(selectforeground="white")
    self.Entry4.insert(0, config_file["sweep_trace_points"])


    self.Entry5 = tk.Entry(self.TNotebook1_t2)
    self.Entry5.place(relx=x_text, rely=0.326, relheight=h_text, relwidth=w_text)
    self.Entry5.configure(background="white")
    self.Entry5.configure(font="TkTextFont")
    self.Entry5.configure(selectbackground="blue")
    self.Entry5.configure(selectforeground="white")
    self.Entry5.insert(0, config_file["resolution_bandwith"])

    self.Entry6 = tk.Entry(self.TNotebook1_t2)
    self.Entry6.place(relx=x_text, rely=0.397, relheight=h_text, relwidth=w_text)
    self.Entry6.configure(background="white")
    self.Entry6.configure(font="TkTextFont")
    self.Entry6.configure(selectbackground="blue")
    self.Entry6.configure(selectforeground="white")
    self.Entry6.insert(0, config_file["visual_bandwith"])

    self.Entry7 = tk.Entry(self.TNotebook1_t2)
    self.Entry7.place(relx=x_text, rely=0.468, relheight=h_text, relwidth=w_text)
    self.Entry7.configure(background="white")
    self.Entry7.configure(cursor="fleur")
    self.Entry7.configure(font="TkTextFont")
    self.Entry7.configure(selectbackground="blue")
    self.Entry7.configure(selectforeground="white")
    self.Entry7.insert(0, config_file["amplitude_log_scale"])

    self.Entry8 = tk.Entry(self.TNotebook1_t2)
    self.Entry8.place(relx=x_text, rely=0.539, relheight=h_text, relwidth=w_text)
    self.Entry8.configure(background="white")
    self.Entry8.configure(cursor="fleur")
    self.Entry8.configure(font="TkTextFont")
    self.Entry8.configure(selectbackground="blue")
    self.Entry8.configure(selectforeground="white")
    self.Entry8.insert(0, config_file["reference_level"])

    self.Entry9 = tk.Entry(self.TNotebook1_t2)
    self.Entry9.place(relx=x_text, rely=0.61, relheight=h_text, relwidth=w_text)
    self.Entry9.configure(background="white")
    self.Entry9.configure(cursor="fleur")
    self.Entry9.configure(font="TkTextFont")
    self.Entry9.configure(selectbackground="blue")
    self.Entry9.configure(selectforeground="white")
    self.Entry9.insert(0, config_file["zoom_spot_marker"][0])

    self.Entry10 = tk.Entry(self.TNotebook1_t2)
    self.Entry10.place(relx=x_text, rely=0.68, relheight=h_text, relwidth=w_text)
    self.Entry10.configure(background="white")
    self.Entry10.configure(cursor="fleur")
    self.Entry10.configure(font="TkTextFont")
    self.Entry10.configure(selectbackground="blue")
    self.Entry10.configure(selectforeground="white")
    self.Entry10.insert(0, config_file["zoom_spot_marker"][1])

    # text for log output
    self.Entry11 = tk.Entry(self.TNotebook1_t2)
    self.Entry11.place(relx=0.035, rely=0.818, relheight=0.154, relwidth=0.94)
    self.Entry11.configure(background="white")
    self.Entry11.configure(font="TkTextFont")
    self.Entry11.configure(selectbackground="blue")
    self.Entry11.configure(selectforeground="grey")
    self.Entry11.configure(state="disabled")

    # function for button "Write configuration"
    def write_conf():
        config_file = {
            "start_freq": int(self.Entry1.get()),
            "stop_freq": int(self.Entry2.get()),
            "center_freq": int(self.Entry3.get()),
            "sweep_trace_points": int(self.Entry4.get()),
            "resolution_bandwith": int(self.Entry5.get()),
            "visual_bandwith": int(self.Entry6.get()),
            "amplitude_log_scale": int(self.Entry7.get()),
            "reference_level": int(self.Entry8.get()),
            "zoom_spot_marker": [int(self.Entry9.get()), self.Entry10.get()]
        }
        try:
            Utils.write_config_file("../config/config_MS2830A.json", config_file)
            print("Scrittura del file di configurazione eseguita con successo")
        except:
            print("La scrittura su file non è andata a buon fine")
        


    self.Button1 = tk.Button(self.TNotebook1_t2)
    self.Button1.place(relx=0.035, rely=y_button, height=h_button, width=w_button)
    self.Button1.configure(borderwidth="2")
    self.Button1.configure(command=write_conf)
    self.Button1.configure(text='''Write configuration''')

    def set_conf():
        global instr
        instr = SPA.Anritsu_MS2830A("Anritsu_MS2830A",config_interface[self.selected_interface.get()])
        Utils.set_SPA_for_measure(instr, config_file)

    self.Button2 = tk.Button(self.TNotebook1_t2)
    self.Button2.place(relx=0.350, rely=y_button, height=h_button, width=w_button)
    self.Button2.configure(command=set_conf)
    self.Button2.configure(borderwidth="2")
    self.Button2.configure(text='''Set configuration''')

    def plot_data():
        trace = instr.get_trace(1) # Get trace
        Utils.plot_lineplot(trace)

    self.Button3 = tk.Button(self.TNotebook1_t2)
    self.Button3.place(relx=0.665, rely=y_button, height=h_button, width=w_button)
    self.Button3.configure(command=plot_data)
    self.Button3.configure(borderwidth="2")
    self.Button3.configure(text='''Plot data''')
