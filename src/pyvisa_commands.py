# pyvisa-shell in order to use a terminal shell
# pyvisa-info for information about Backends, PyVISA version and Python stuffs

# Ubuntu drivers: https://www.ni.com/it-it/support/downloads/drivers/download.ni-linux-device-drivers.html#427909
# GPIB-USB-HS+ drivers: https://github.com/fmhess/hsplus_load
# Documentation about drivers: 
# https://www.ni.com/it-it/support/documentation/supplemental/18/downloading-and-installing-ni-driver-software-on-linux-desktop.html
import pyvisa
#import time
#import numpy as np

resource_man = pyvisa.ResourceManager("@py")
print(resource_man.list_resources("?*")) # all resources
inst = resource_man.open_resource("TCPIP0::192.168.60.41::49153::SOCKET", write_termination = '\n',read_termination='\n')
print("Who am i? " + inst.query("*IDN?"))

inst.write("*RST") # Preset
print("Self Test: " + inst.query("*TST?"))
print("SW: " + inst.query("swe:time?"))
#inst.write("INST SPECT") # set Spectrum Analyzer


"""
######################################
#           FREQUENCY                #
######################################
inst.write("STF 1000000000") #1GhZ
inst.write("SOF 4000000000")
inst.write("CNF 2000000000")
print("Start Frequency: " + inst.query("STF?"))
print("Stop Frequency: " + inst.query("SOF?"))
print("Center Frequency: " + inst.query("CNF?"))

######################################
#           TIME SWEEP               #
######################################
inst.write("SWE:POIN 5001")
print("Sweep Trace points: " + inst.query("SWE:POIN?"))


######################################
#                BW                  #
######################################
inst.write("RB 1000000") #1MhZ
print("Resolution Bandwith: " + inst.query("RB?"))
inst.write("VB 100")
print("Video Bandwith: " + inst.query("VB?"))
######################################
#           AMPLITUDE                #
######################################
inst.write("LOGSCALEDIV 1")
print("Amplitude log scale: " + inst.query("LOGSCALEDIV?"))

inst.write("RLV -62DBM")
print("Reference level: " + inst.query("RLV?"))
######################################
#              MARKER                #
######################################
inst.write("CALC:MARK:WIDT:TYPE 1,SPOT")

######################################
#          DONWLOAD TRACK            #
######################################
#inst.write("STORAGEMODE MIN")
print(inst.query("STORAGEMODE?")) # Time Trace Point

#inst.write("STORAGECOUNT 1750")
print(inst.query("STORAGECOUNT?")) # Storage count

time.sleep(25) 
track = inst.query_ascii_values("TRAC? TRAC1", container = np.array) # Trace A

print(track)
#inst.write(f"MMEM:STOR:TRAC:CHAN ALL,'example.csv', UNF, LOGP, POIN, COMM")
#inst.write("*WAI")
#print("Measurement status query: " + inst.query("MSTAT?"))

"""