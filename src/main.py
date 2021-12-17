import Anritsu_MS2830A as SPA
import Utils

if __name__ == '__main__':
    
    gpib = "GPIB::18::INSTR"
    remote_eth = "TCPIP0::localhost::49153::SOCKET"
    #local_eth =
    config_file = Utils.read_config_file("../config/config_MS2830A.json")
    
    instr = SPA.Anritsu_MS2830A("Anritsu_MS2830A", remote_eth)
    Utils.set_SPA_for_measure(instr, config_file)

    trace = instr.get_trace(1) # Get trace
    
    Utils.plot_lineplot(trace)
    Utils.save_data_as_csv(trace)
    