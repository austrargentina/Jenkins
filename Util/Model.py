'''
Created on 29.09.2014

@author: Daniel Scheuch, Maximilian Wech, Balkan Arif
@contact: daniel.scheuch@student.tgm.ac.at, maximilian.wech@student.tgm.ac.at, abalkan@student.tgm.ac.at
@description: This is the Modelclass it handles all our functions of the website
'''
from Objekte.FirewallRule import FirewallRule
from Util.Connector import Connector
from Util.RenderChart import RenderChart
import socket
class Model():   
    policesList = []
    zonesList = []
    servicesList = []
    throughPutList = []
    ip =''
    user =''
    renderer = RenderChart()
    sshdata = []
    '''
    Constructor set the defaulte values
    '''
    def __init__(self): 
         self.user = '5xHIT'
         self.ip = '10.0.100.10'
         self.policesList = Connector(self.user , self.ip , 161 , 'NETSCREEN-POLICY-MIB' , 'nsPlyName').getRules()
         self.zonesList = Connector(self.user , self.ip , 161 , 'NETSCREEN-ZONE-MIB' , 'nsZoneCfgName').getRules()
         self.servicesList = Connector(self.user , self.ip , 161 , 'NETSCREEN-SERVICE-MIB' , 'nsServiceName').getRules()
         #self.throughPutList = Connector(self.user,self.ip, 161, '1.3.6.1.4.1.3224.10.2.1.6.1.0', '1.3.6.1.4.1.3224.10.2.1.6.42.0', 0, 5).getRules()
         self.getChart()
         
    '''
    getting the chart
    '''
    def getChart(self):
        #self.renderer.setValues(self.getThroughputValues())
        self.renderer.render()
    '''
    ip setter
    '''   
    def setIP(self,ip):
        if isinstance(ip, str):
            self.ip = ip
        else:
            raise ValueError('Only Strings allowed')   
    '''
    user setter
    '''
    def setUser(self,user):
        if isinstance(user, str):
            self.user = user
        else:
            raise ValueError('Only Strings allowed')   
    '''
    get firewall list
    '''    
    def getFirewalllist(self):
        return self.firewallList()
    '''
    firewall setter
    '''
    def setFirewalllist(self,FirewallRule):
        self.firewallList.append(FirewallRule)

    '''
    sets our lists to file
    '''
    def listToFile(self):
        self.refresh()
        try:
            file = open("GUI/static/file/Firewall_Rules.txt", "w")
            file.write("Polices:\n")
            for x in range(0,len(self.policesList)):         
                file.write(self.policesList[x].toString()+"\n")
    
            file.write("\nZones:\n")    
            for x in range(0,len(self.zonesList)):
                file.write(self.zonesList[x].toString()+"\n")
            
            file.write("\nServices:\n")    
            for x in range(0,len(self.servicesList)):
                file.write(self.servicesList[x].toString()+"\n")    
    
            file.close()
            return True  
        except IOError:
            return False
             
    '''
    refreshes all our lists
    '''
    def refresh(self):        
        self.policesList = Connector('5xHIT' , self.ip , 161 , 'NETSCREEN-POLICY-MIB' , 'nsPlyName').getRules()
        self.zonesList = Connector('5xHIT' , '10.0.100.10' , 161 , 'NETSCREEN-ZONE-MIB' , 'nsZoneCfgName').getRules()
        self.servicesList = Connector('5xHIT' , '10.0.100.10' , 161 ,'NETSCREEN-SERVICE-MIB' , 'nsServiceName').getRules()
        #self.throughPutList = Connector(self.user,self.ip, 161, '1.3.6.1.4.1.3224.10.2.1.6.1.0', '1.3.6.1.4.1.3224.10.2.1.6.42.0', 0, 5).getRules()

    '''
    toStringmethod
    param name : name of the list you want to have
    returns the list in string
    '''
    def RulesToString(self, name):
        out = ''
        if name == "policies" and isinstance(name, str):
            for x in range(0,len(self.policesList)):
                 out += self.policesList[x].toString()+'<br/>'
            
        elif name == "services" and isinstance(name, str):
            for x in range(0,len(self.servicesList)):
                 out += self.servicesList[x].toString()+'<br/>'
            
        elif name == "zones" and isinstance(name, str):
            for x in range(0,len(self.zonesList)):
                 out += self.zonesList[x].toString()+'<br/>' 
        
        elif name == "throughput" and isinstance(name, str):         
             for x in range(0,len(self.throughPutList)):
                 out += self.throughPutList[x].toString()+'<br/>' 
        elif not isinstance(name, str): 
            raise ValueError("Only Strings allowed")
        return out

    '''
    get througput values
    '''
    def getThroughputValues(self):
        out = []
        for x in range(0,len(self.throughPutList)):
                 out.append(int(self.throughPutList[x].getValue()))    
                            
        return out
    
    '''
    validation of the ip
    '''
    def validIP(self,ip):
        try:
            socket.inet_aton(ip)
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            for item in parts:
                if not 0 <= int(item) <= 255:
                    return False
                return True
            val = int(ip)
        except (ValueError, socket.error) as e:
            return False
    '''
    connect with ssh to destination with user pw and command
    '''
    def connectSSH(self, ip, user, pw, cmd):
        '''
        Firewall: ipadress: 10.0.100.10, user: 5bhit, pw: Eephaefagh1p, command: sudo ifconfig  -->Connecting Works, executing command not
        Debian: ipadress: 192.168.0.19, user: root, pw: root, command: sudo ifconfig   --> WORKS
        
        A firewall connection is possible, but we can't run any commands on the appliance.
        Therefore we used a mock object, to show how the result would be.
        '''        
        #data = []
        #ssh = paramiko.SSHClient()
        #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh.connect(ipadress, username=user, password=pw)
        #stdin, stdout, stderr = ssh.exec_command(cmd)
        #data.append(stdout.readlines())
        #ssh.close()
        data=[ip,user,pw,cmd]
        return data