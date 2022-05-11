import telnetlib
import socket # for sockets
import sys # for exit
import time

##################################################
# DAT64F - 6GHz Programmable finestep attenuator #
##################################################

def set_dat64f(dat_host, dat_port, timeout, db):
    att_string = 'att ' + str(db) + ' \n'
    att_bytes = bytes(att_string, 'ASCII')
    
    with telnetlib.Telnet(dat_host, dat_port, timeout) as session:
        #session.interact()
        session.write(att_bytes)

    time.sleep(1)

    with telnetlib.Telnet(dat_host, dat_port, timeout) as session:
        session.write(b"att?\n")
        print("\n\tDAT64F attenuator: " + session.read_until(b'\r\n').decode('ascii'))

##################################################
#             Siglent SDP 3003X                  #
##################################################


#Port 5024 is valid for the following:
#SIGLENT SDS1202X-E, SDG2X Series, SDG6X Series
#SDM3055, SDM3045X, and SDM3065X
#
#Port 5025 is valid for the following:
#SIGLENT SVA1000X series, SSA3000X Series, and SPD3303X/XE

def SocketConnect():
    try:
        #create an AF_INET, STREAM socket (TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print ('\tFailed to create socket.')
        sys.exit()
    
    try:
        #Connect to remote server
        sock.connect((siglent_ip , siglent_port))
    except socket.error:
        print ('\tfailed to connect to ip ' + siglent_ip)
    return sock

def SocketSend(Sock, cmd):
    try :
        #Send cmd string
        Sock.sendall(cmd)
        Sock.sendall(b'\n')
        time.sleep(1)
    except socket.error:
        #Send failed
        print ('\tSend failed')
        sys.exit()
        
def SocketQuery(Sock, cmd):
    SocketSend(Sock, cmd)
    reply = Sock.recv(4096)
    print(reply)

def SocketClose(Sock):
    #close the socket
    Sock.close()
    time.sleep(1)

def set_siglent(switch):
    sock = SocketConnect()
    
    switch_string = 'OUTP CH1,'+ switch
    switch_bytes = bytes(switch_string, 'ASCII')
    
    SocketSend(sock, switch_bytes)
    """
    SocketQuery(sock, b'*IDN?')
    SocketQuery(sock, b'MEAS:CURR? CH2') 
    SocketQuery(sock, b'MEAS:VOLT? CH2') 
    SocketQuery(sock, b'MEAS:POWE? CH2') 

    SocketSend(sock, b'INST CH1')
    SocketQuery(sock, b'INST?')

    SocketSend(sock, b'CH1:CURR 1')
    SocketQuery(sock, b'CH1:CURR?')

    SocketSend(sock, b'CH1:VOLT 15')
    SocketQuery(sock, b'CH1:VOLT?')
    """
    
    SocketClose(sock)
    print('\tSiglent SDP 3003X: ' + switch_string + "\n")


if __name__ == '__main__':
    # network settings
    dat_local = "192.168.60.73"
    dat_remote = "localhost" 
    dat_port = 10001
    timeout = 1000
    
    siglent_local = "192.168.60.72"
    siglent_remote = "localhost" 
    siglent_port = 5025 
    
    dat_host = ""
    siglent_ip = ""
    
    # arguments for attenuator and power supply
    experimentlist = ["PC", "PC+m", "PH+m", "PH", "PC"]
    dat64list = [63, 63, 21.5, 21.5, 63]
    siglentlist = ["OFF", "ON", "ON", "OFF", "OFF"]


    interface = input("select interface: (1) for local inteface, (2) for remote interface: ")
    if interface == '1':
        dat_host = dat_local
        siglent_ip = siglent_local
    elif interface == '2':
        dat_host = dat_remote
        siglent_ip = siglent_remote
    else:
        print("No available interfaces, try again...")
        sys.exit()

    for i in range(5):
        input("Press Enter to continue with " + experimentlist[i])
        set_dat64f(dat_host, dat_port, timeout, dat64list[i])
        time.sleep(1)
        set_siglent(siglentlist[i])
        print("\t" + experimentlist[i] + " done\n")