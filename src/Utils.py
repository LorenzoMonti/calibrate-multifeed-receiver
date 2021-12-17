import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

  
def set_SPA_for_measure(ms2830a):
        """
        This method allows to set the Anritsu MS2830A for the measurements
        """    
        ms2830a.set_reset()
        ms2830a.self_test()
        ms2830a.set_SPA()
        
        # Frequency
        ms2830a.do_set_startfreq(1000000000) # 1Ghz
        ms2830a.do_set_stopfreq(4000000000)
        ms2830a.do_set_centerfreq(2000000000)
        print("Start Frequency: " + str(ms2830a.do_get_startfreq()))
        print("Stop Frequency: " + str(ms2830a.do_get_stopfreq()))
        print("Center Frequency: " + str(ms2830a.do_get_centerfreq()))
        
        # Time sweep
        ms2830a.set_trace_points_sweeptime(5001)
        print("Sweep Trace points: " + str(ms2830a.get_trace_points_sweeptime()))

        # BW
        ms2830a.do_set_resolutionBW(1000000) # 1Mhz
        print("Resolution Bandwith: " + str(ms2830a.do_get_resolutionBW()))
        ms2830a.do_set_videoBW(100)
        print("Visual bandwith:" + str(ms2830a.do_get_videoBW))
        
        # AMPLITUDE
        ms2830a.set_amplitude_scale(1)
        print("Amplitude log scale: " + str(ms2830a.get_amplitude_scale()))
        ms2830a.set_reference_level(-62)
        print("Reference level: " + str(ms2830a.get_reference_level()))

        # MARKER
        ms2830a.set_zoom_spot_marker(1, "SPOT")


def plot_lineplot(trace):
        
        x = np.arange(len(trace)) # x axis
        dataset = pd.DataFrame({"points": x , "dbM": trace})

        sns.set_style("darkgrid")
        sns.lineplot(x="points", y="dbM", data=dataset)
        plt.show()


def save_data_as_csv(trace):
        dataset = pd.DataFrame(trace)
        dataset.to_csv("../data/measure-" + str(datetime.datetime.now()) + ".csv")

