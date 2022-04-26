import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import json
from math import log10
import os
from pathlib import Path
import wget
import shutil

"""
Python module that contains utily functions for the Anritsu MS2830A Signal Source Analyzer and measurements

"""

HOME_DIRECTORY = str(Path.home()) + "/.calibrate_receiver/"

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
    #log_list.append("Center Frequency: " + str(ms2830a.do_get_centerfreq()))

    # Time sweep
    ms2830a.set_trace_points_sweeptime(config_file["sweep_trace_points"])
    log_list.append("Sweep Trace points: " + str(ms2830a.get_trace_points_sweeptime()))

    # BW
    ms2830a.do_set_resolutionBW(config_file["resolution_bandwith"]) # 1Mhz
    log_list.append("Resolution Bandwith: " + str(ms2830a.do_get_resolutionBW()))
    ms2830a.do_set_videoBW(config_file["video_bandwith"])
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

#########################
#         PLOT          #
#########################

def plot_lineplot(trace):
    """
    Utily function to plot trace retrieved from Anritsu MS2830A Signal Source Analyzer
      
    """
    x = calcFrequency() # x axis
    dataset = pd.DataFrame({"points": x , "dbM": trace})

    sns.set_style("darkgrid")
    sns.lineplot(x="points", y="dbM", data=dataset)
    plt.show()

def plot_results(trx, tm, dr, mr, upperBound, lowerBound):
    """
    Utily function to plot calculated data (trx, tm, dr, mr and bounds)

    """
    dataset1 = pd.DataFrame({ "Trx": trx, "Tm": tm})
    dataset2 = pd.DataFrame({ "Dr": dr, "Mr": mr, "Upperbound": upperBound, "Lowerbound": lowerBound})

    fig, axs = plt.subplots(ncols=2, figsize=(18, 10))
    fig.suptitle('Measure results')
    axs[0].set_title('Trx and Tm')
    axs[1].set_title('Dr and Mr')
    sns.set_style("darkgrid")
    sns.lineplot(ax=axs[0], data=dataset1)
    sns.lineplot(ax=axs[1], data=dataset2)
    plt.show()

#########################
#     FILE MANAGER      #
#########################

def save_data_as_csv(trace):
    """
    Utility function for saving data in csv extension

    """
    dataset = pd.DataFrame(trace)
    dataset.to_csv("measure-" + str(datetime.datetime.now()) + ".csv")

def read_config_file(filename):
    """
    Utility function for reading configuration file (JSON)

    """
    data = []
    with open(filename, 'r') as file:
        data = file.read()
    return json.loads(data)

def write_config_file(filename, confDict):
    """
    Utility function for writing configuration file (JSON)
 
    """
    json_obj = json.dumps(confDict, indent=4)
    with open(filename, 'w') as file:
        file.write(json_obj)

def create_home_directory():
    """
    Utily function used to create an external folder to setup configuration files 
    """
    if not os.path.exists(HOME_DIRECTORY):
        os.makedirs(HOME_DIRECTORY)
        download_config_files()        

def download_config_files():
    """
    Utily function used to download and unzip config files 
    """
    wget.download('https://docs.google.com/uc?export=download&id=13OqmkVfld7d2N-y6kaMWhnme1aJLIzSO', HOME_DIRECTORY)
    shutil.unpack_archive(HOME_DIRECTORY + 'calibrate_receiver.zip', HOME_DIRECTORY)

#########################
#       FORMULAS        #
#########################

def W2dBm(W):
    """
    Function to convert from W to dBm
    
    """
    return 10. * log10(W) + 30

def dBm2W(dBm):
    """
    Function to convert from dBm to W
    
    """
    return 10**((dBm)/10.) / 1000

def getWatts(dBm):
    """
    Function to return a list of watts values
    
    """
    return map(dBm2W, dBm)

def calcFrequency():
    """
    Function used to calculate the x-axis of the trace (frequencies)
    
    """
    config_file = read_config_file(HOME_DIRECTORY + "config_MS2830A.json")
    
    tmp_freq = ((config_file["stop_freq"] - config_file["start_freq"]) / (config_file["sweep_trace_points"] - 1))
    frequency = [(config_file["start_freq"] + (tmp_freq * i)) for i in range(0, config_file["sweep_trace_points"]) ]
    
    return frequency

def getCalculus(traces, Tc = 77, Th = 297):
    """
    Function that returns useful calculus from trace data
    
    """
    Tc = np.full(len(traces[0]), Tc)
    Th = np.full(len(traces[0]), Th)
    ones = np.ones(len(traces[0]))

    dMeasure = traces[4] - traces[0]
    drMeasure = traces[4] / traces[0]
    
    Pc = traces[0] + (0 * (dMeasure / 4))
    PcPlusM = traces[1] + (1 * (dMeasure / 4))
    PhPlusM = traces[2] + (2 * (dMeasure / 4))
    Ph = traces[3] + (3 * (dMeasure / 4))
    Yvalue = Ph / Pc
    Yvalue[Yvalue == 1.] = 1.00001 # if Yvalue = 1. then set 1.00001
    
    Trx = (Th - (Yvalue * Tc)) / (Yvalue - ones)
    Tm = ((Th - Tc) / (Ph - Pc)) * (PcPlusM - Pc)
    Thm = ((Th - Tc) / (Ph - Pc)) * (PhPlusM - Ph)
    
    return dMeasure, drMeasure, Pc, PcPlusM, PhPlusM, Ph, Yvalue, Trx, Tm, Thm

def acceptable_drift(drMeasure, Tm, Thm, lowerBound, upperBound):
    """
    Function that return true if drift is acceptable (based on lowerBound and upperBound), false otherwise
    """
    mrMeasure = Tm/Thm
    mrMeasure = preprocess_mr(mrMeasure)
    drMean = np.mean(drMeasure)
    drSTD = np.std(drMeasure)
    mrMean = np.mean(mrMeasure)
    mrSTD = np.std(mrMeasure)
    print("drMean: " + str(drMean) + " drSTD: " + str(drSTD) + " mrMean: " + str(mrMean) + " mrSTD: " + str(mrSTD))
    if((lowerBound < drMean < upperBound) and (lowerBound < mrMean < upperBound)):
        return True
    return False

def preprocess_mr(mrMeasure):
    
    mrMeasure = mrMeasure[~np.isposinf(mrMeasure)] # remove inf values using numpy.isposinf() and numpy.logical_not
    mrMeasure = mrMeasure[~np.isneginf(mrMeasure)] # remove -inf values using numpy.isneginf() and numpy.logical_not
    mrMeasure = mrMeasure[~np.isnan(mrMeasure)] # remove nan values using numpy.isnan() and numpy.logical_not
    
    return mrMeasure

############################
#           UI             #
############################

def clear_message(self, trace_number):
    """
    UI function

    """
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
    """
    UI function

    """
    self.Message1.configure(background="#ffffff", font=("Helvetica", 10))
    self.Message2.configure(background="#ffffff", font=("Helvetica", 10))
    self.Message3.configure(background="#ffffff", font=("Helvetica", 10))
    self.Message4.configure(background="#ffffff", font=("Helvetica", 10))
    self.Message5.configure(background="#ffffff", font=("Helvetica", 10))