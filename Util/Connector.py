'''
@author: Maximilian Wech, Balkan Arif
@contact: mwech@student.tgm.ac.at, abalkan@student.tgm.ac.at
@version: 2014 10 05
@last update: 2014 10 30
@content: The class connects to the firewall, due to some log-in data.
          It reads the firewall data (policies, zones, services) out of the specific 
          MIB files.
          
'''
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pyasn1.type.univ import OctetString
from Objekte.FirewallRule import FirewallRule
#import paramiko

class Connector():
    
    '''
    Constructor
    @param communityData The user group 
    @param ip The IP address to be used
    @param port The port to be connected
    @param mib The mibfile to be connected
    @param table The specific table in the mibfile 
    '''
    def __init__(self, communityData, ip, port, mib, table): 

            if isinstance(communityData, str) and isinstance(ip, str) and isinstance(port, int) and isinstance(mib, str) and isinstance(table, str):
                self.CommunityData2 = communityData
                self.IP = ip
                self.Port = port
                self.MIB = mib
                self.Table = table
            else:
                raise ValueError('Only Strings and Integer allowed')

       
    '''
    The method connects to the Firewall appliance (via IP, Port, user group, mib file, mib table), and checks if there are any errors occurring.
    When the check was successful and no errors were appearing,  the OIDs and the specific values will be printed separately.
    SNMPv2 is used.
    '''
    def getRules(self):
        output = []
        # Connecting to the firewall 
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(                                                             
            cmdgen.CommunityData(self.CommunityData2),                                                          
            cmdgen.UdpTransportTarget((self.IP, self.Port)),
            0, 1,
               #MIB is the name of the MIB File, Table is the neccessary table, to get the Name of the ordered data
            cmdgen.MibVariable(self.MIB, self.Table).addMibSource('MIB_Files'),           
        )    
        # Checking the Error Indications 
        if errorIndication:
            print(errorIndication)
        else:
            ResultData = Connector.defineData(self, varBindTable)
            return ResultData
    
    '''
    The method handles the retrieved Data form the firewall appliance. Cause of mass results, a rectangular table of var-binds will be used
    The width of that table is determined by the number of var-binds in request and it never changes while some var-binds hitting end-of-MIB condition. 
    '''    
    def defineData(self, varBindTable):      
        output = []
        #Delete First entry in varBindTable
        del varBindTable[-1]
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                output.append(FirewallRule(name.prettyPrint(),val.prettyPrint()))  
        else:
            return output 
        
    '''
    This method tries to connect to firewall appliance with SNMPv3. If this protocol is not available a fallback to SNMPv2 happens.
    The result is the retrieved data in a list.
    '''            
    def getRulesWithSNMPv3AndFallback(self):
        output = []
        # Connecting to the firewall 
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd( 
            #SNMPv3 Try
            cmdgen.UsmUserData('usr-md5-none', 'authkey1', securityName='self.CommunityData2'),
            cmdgen.UdpTransportTarget((self.IP, self.Port)),
            0, 1,
               #MIB is the name of the MIB File, Table is the neccessary table, to get the Name of the ordered data
            cmdgen.MibVariable(self.MIB, self.Table).addMibSource('../MIB_Files'),           
        )    
        # Checking the Error Indications 
        if errorIndication:
            # FALLBACK; Try if SNMPv2 is available
            # Connecting to the firewall 
            cmdGen = cmdgen.CommandGenerator()
            errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(                                                             
                cmdgen.CommunityData(self.CommunityData2),                                                          
                cmdgen.UdpTransportTarget((self.IP, self.Port)),
                0, 1,
                #MIB is the name of the MIB File, Table is the neccessary table, to get the Name of the ordered data
                cmdgen.MibVariable(self.MIB, self.Table).addMibSource('../MIB_Files'),           
            )    
            # Checking the Error Indications 
            if errorIndication:
                print(errorIndication)
            else:
               ResultData = Connector.defineData(self, varBindTable)
               return ResultData
        else:
            ResultData = Connector.defineData(self, varBindTable)
            return ResultData
        

    
    
        '''
    #DEBIAN CONNECT
    #executing commands works
    import paramiko
 
    cmd = "sudo ifconfig"
 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.0.19', username='root', password='root')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print stdout.readlines()
    ssh.close()
    '''
