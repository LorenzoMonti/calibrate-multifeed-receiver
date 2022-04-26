import logging
from time import sleep
import numpy as np
import pyvisa


class Anritsu_MS2830A():
    """
    Python class for the Anritsu MS2830A Signal Source Analyzer
    
    """

    def __init__(self, name, address = 'GPIB::18::INSTR'):
        """
        Initializes 
        Input:
            name (string)    : name of the instrument
            address (string) : GPIB or ETH address
        """
        
        logging.info(__name__ + ' : Initializing instrument')
        
        self._name = name
        self._address = address
        
        try:
            # initialize instrument
            _resource_man = pyvisa.ResourceManager()
            self._list_res = _resource_man.list_resources()
            self._visainstrument = _resource_man.open_resource(self._address, write_termination = '\n',read_termination='\n')
            self._visainstrument.encoding = "latin-1" # encoding 
        except:
            logging.error(__name__ + ' : Initializing instrument exception. Make sure that your instrument is connected')
            exit()

    def who_am_i(self):
        """
        default comand in order to know which is the instrument connected
        """
        return str(self._visainstrument.query('*IDN?'))

    def set_reset(self):
        """
        reset command
        """
        return self._visainstrument.write('*RST')

    def self_test(self):
        """
        self test command
        """
        return int(self._visainstrument.query('*TST?'))

    def set_SPA(self):
        """
        command to set Spectrum Analyzer 
        """
        return self._visainstrument.write('INST SPECT')

    def get_resourcelist(self, resource_man):
        """
        gets the list of available resources
        """
        return self._list_res

    ######################################
    #                BW                  #
    ######################################
   
    def do_set_resolutionBW(self, BW):
        """
        sets the resolution bandwidth
        """
        self._visainstrument.write('RB %f'%(BW))

    def do_get_resolutionBW(self):
        """
        gets the resolution bandwidth
        """
        return float(self._visainstrument.query('RB?'))

    def do_set_videoBW(self, BW):
        """
        sets the video bandwidth
        """
        self._visainstrument.write('VB %f'%(BW))

    def do_get_videoBW(self):
        """
        gets the video bandwidth
        """
        return float(self._visainstrument.query('VB?'))
    
    ######################################
    #           TIME SWEEP               #
    ######################################

    def get_sweeptime(self):
        """
        query the sweep time
        """
        return float(self._visainstrument.query('swe:time?'))

    def set_trace_points_sweeptime(self, points):
        """
        sets the trace point for time sweep
        """
        self._visainstrument.write('SWE:POIN %i' % (points))

    def get_trace_points_sweeptime(self):
        """
        query the trace point for time sweep
        """
        return int(self._visainstrument.query('SWE:POIN?'))

    #def do_get_sweeptime_averages(self):
    #    if self.get_Average():
    #        return self.get_sweeptime() * self.get_averages()
    #    else:
    #        return self.get_sweeptime()     
    
    def set_continuous_sweep_mode(self,value):
        """
        value='ON' Continuous sweep
        value='OFF' Single sweep
        """
        self._visainstrument.write('INIT:CONT %s'%(value))   

    def sweep(self):
        """
        perform a sweep and wait for it to finish
        """
        self._visainstrument.write('INIT; *WAI')    

    ######################################
    #           FREQUENCY                #
    ######################################

    def do_set_centerfreq(self, centerfreq):
        """
        sets the center frequency
        """
        self._visainstrument.write('CNF %f' % (centerfreq))


    def do_get_centerfreq(self):
        """
        gets the center frequency
        """
        return float(self._visainstrument.query('CNF?'))

    def do_set_freqspan(self, freqspan):
        """
        sets the frequency span
        """
        self._visainstrument.write('freq:span %f'%(freqspan))
    
    def do_get_freqspan(self):
        """
        gets the frequency span
        
        """
        return float(self._visainstrument.query('freq:span?'))

    def do_set_startfreq(self, freq):
        """
        sets the start frequency
        
        """

        self._visainstrument.write('STF %f'%(freq))

    def do_get_startfreq(self):
        """
        gets the start frequency
        
        """
        return float(self._visainstrument.query('STF?'))

    def do_set_stopfreq(self, freq):
        """
        sets the stop frequency
        
        """
        self._visainstrument.write('SOF %f'%(freq))

    def do_get_stopfreq(self):
        """
        gets the stop frequency
        
        """
        return float(self._visainstrument.query('SOF?'))
        
    ######################################
    #           POWER UNIT               #
    ######################################

    def do_set_powerunit(self,unit):
        """
        sets the unit for powers
        provide unit as a string! ("DBm")
        """
        self._visainstrument.write('unit:pow %s'%(unit))
        
    def do_get_powerunit(self):
        """
        gets the power unit for powers
        """
        return self._visainstrument.query('unit:pow')
        
    def do_get_averages(self):
        """
        Get number of averages
        Input:
            None
        Output:
            number of averages
        """
        
        return int(self._visainstrument.query(':AVER:COUNT?'))

    ######################################
    #               MARKER               #
    ######################################

    def set_zoom_spot_marker(self,number = 1,type = "SPOT"):
        """
        sets the zoom spot
        """
        self._visainstrument.write('CALC:MARK:WIDT:TYPE %i,%s'%(number,type))

    def set_marker(self,marker,frequency):
        """
        sets marker number marker to frequency
        
        """
        self._visainstrument.write('calc:mark%i:x %e'%(marker, frequency))
        self.enable_marker(marker)
    
    def get_marker(self,marker):
        """
        gets frequency of marker
        
        """
        return float(self._visainstrument.query('calc:mark%i:x?'%(marker)))
    
    def get_marker_level(self,marker):
        """
        gets power level of indicated marker
        
        """
        return float(self._visainstrument.query('calc:mark%i:y?'%(marker)))

    def enable_marker(self,marker,state='ON'):
        """
        marker: ON or OFF
        """
        self._visainstrument.write('CALC:MARK%i %s'%(marker,state))           

    ######################################
    #           AMPLITUDE                #
    ######################################  

    def set_amplitude_scale(self, scale):
        """
        sets amplitude scale (log)
        
        """
        self._visainstrument.write('LOGSCALEDIV %i' %(scale))

    def get_amplitude_scale(self):
        """
        gets amplitude scale
        
        """
        return self._visainstrument.query('LOGSCALEDIV?')

    def set_reference_level(self, db):
        """
        sets reference level
        
        """
        self._visainstrument.write('RLV %iDBM' %(db))

    def get_reference_level(self):
        """
        gets reference level
        
        """
        return self._visainstrument.query('RLV?')

    ######################################
    #               TRACE                #
    ######################################
            
    def get_trace(self, tracenumber=1):
        """
        gets trace data
        """
        # in ASCII form (slow, but human readable) and binary (fast, but more difficult to debug)
        sleep(self.get_sweeptime() + 1)
        trace = self._visainstrument.query_ascii_values("TRAC? TRAC%i" %(tracenumber) , container = np.array) # Trace A (default)

        return trace
    
    def get_frequencies(self):
        """
        returns an array with the frequencies of the points returned by get_trace()
        ideally suitable as x-axis for plots
        """
        return np.linspace(self.get_startfreq(),self.get_stopfreq(),self.set_trace_points_sweeptime())

    def get_storagemode(self):
        """
        gets the storage mode
        """
        return self._visainstrument.query("STORAGEMODE?") # Storage mode

    def get_storagecount(self):
        """
        gets the storage count
        """
        return self._visainstrument.query("STORAGECOUNT?") # Storage count

    ##########################################
    # ENABLE FOR DEBUG AND TEST NEW FUNCTION #
    ##########################################
    
    def write(self, command):
        """
        test function used for debug
        """
        self._visainstrument.write(command)
    
    def query(self,command):
        """
        test function used for debug
        """
        return self._visainstrument.query(command)