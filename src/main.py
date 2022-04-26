#from src import Anritsu_MS2830A as SPA
from src import Utils
import numpy as np
#import datetime
if __name__ == '__main__':
    
    config_interface = Utils.read_config_file("./config/config_interface.json")
    config_file = Utils.read_config_file("./config/config_MS2830A.json")
    
    #instr = SPA.Anritsu_MS2830A("Anritsu_MS2830A", config_interface["remote_eth"])
    #Utils.set_SPA_for_measure(instr, config_file)

    #trace = instr.get_trace(1) # Get trace
    
    #Utils.plot_lineplot(trace)
    #Utils.save_data_as_csv(trace)
    print(list(Utils.getWatts(np.array([64.3, 62.3, 11.78, 44.,0.55]))))
