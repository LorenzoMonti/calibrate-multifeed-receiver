import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import json
  
def set_SPA_for_measure(ms2830a, config_file, manual_command):
        """
        This method allows to set the Anritsu MS2830A for the measurements
        """
        log_list = []    
        ms2830a.set_reset()
        ms2830a.self_test()
        ms2830a.set_SPA()
        
        # Frequency
        ms2830a.do_set_startfreq(config_file["start_freq"]) # 1Ghz
        ms2830a.do_set_stopfreq(config_file["stop_freq"])

        log_list.append("Start Frequency: " + str(ms2830a.do_get_startfreq()))
        log_list.append("Stop Frequency: " + str(ms2830a.do_get_stopfreq()))
        log_list.append("Center Frequency: " + str(ms2830a.do_get_centerfreq()))
        
        # Time sweep
        ms2830a.set_trace_points_sweeptime(config_file["sweep_trace_points"])
        log_list.append("Sweep Trace points: " + str(ms2830a.get_trace_points_sweeptime()))

        # BW
        ms2830a.do_set_resolutionBW(config_file["resolution_bandwith"]) # 1Mhz
        log_list.append("Resolution Bandwith: " + str(ms2830a.do_get_resolutionBW()))
        ms2830a.do_set_videoBW(100)
        log_list.append("Video bandwith:" + str(ms2830a.do_get_videoBW()))
        
        # AMPLITUDE
        ms2830a.set_amplitude_scale(config_file["amplitude_log_scale"])
        log_list.append("Amplitude log scale: " + str(ms2830a.get_amplitude_scale()))
        ms2830a.set_reference_level(config_file["reference_level"])
        log_list.append("Reference level: " + str(ms2830a.get_reference_level()))

        # MARKER
        ms2830a.set_zoom_spot_marker(config_file["zoom_spot_marker"][0], config_file["zoom_spot_marker"][1])
        
        # MANUAL COMMAND
        if(len(manual_command) != 0):
                ms2830a.write(manual_command)
        
        return log_list

def plot_lineplot(trace):
        
        x = np.arange(len(trace)) # x axis
        dataset = pd.DataFrame({"points": x , "dbM": trace})

        sns.set_style("darkgrid")
        sns.lineplot(x="points", y="dbM", data=dataset)
        plt.show()


def save_data_as_csv(trace):
        dataset = pd.DataFrame(trace)
        dataset.to_csv("../data/measure-" + str(datetime.datetime.now()) + ".csv")

def read_config_file(filename):
        data = []
        with open(filename, 'r') as file:
                data = file.read()
        return json.loads(data)

def write_config_file(filename, confDict):
        json_obj = json.dumps(confDict, indent=4)
        with open(filename, 'w') as file:
                file.write(json_obj)

def clear_message(self, trace_number):
        if(trace_number == 0):
                self.Message1.configure(background="green", font=("Helvetica",24))
        elif(trace_number == 1):
                self.Message1.configure(background="#d9d9d9", font=("Helvetica",10))
                self.Message2.configure(background="green", font=("Helvetica",24))
        elif(trace_number == 2):
                self.Message2.configure(background="#d9d9d9", font=("Helvetica",10))
                self.Message3.configure(background="green", font=("Helvetica",24))
        elif(trace_number == 3):
                self.Message3.configure(background="#d9d9d9", font=("Helvetica",10))
                self.Message4.configure(background="green", font=("Helvetica",24))
        elif(trace_number == 4):
                self.Message4.configure(background="#d9d9d9", font=("Helvetica",10))
                self.Message5.configure(background="green", font=("Helvetica",24))

def clear_background(self):
        self.Message1.configure(background="#d9d9d9", font=("Helvetica", 10))
        self.Message2.configure(background="#d9d9d9", font=("Helvetica", 10))
        self.Message3.configure(background="#d9d9d9", font=("Helvetica", 10))
        self.Message4.configure(background="#d9d9d9", font=("Helvetica", 10))
        self.Message5.configure(background="#d9d9d9", font=("Helvetica", 10))