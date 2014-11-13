'''
Created on 29.09.2014

@author: Daniel Scheuch
@contact: daniel.scheuch@student.tgm.ac.at
'''

class FirewallRule(object): 
    
    '''
    This is the constructor for the class FirewallRule
    @param oid: OID number
    @param value: value  
    '''
    def __init__(self, oid, value): 
        self.oid = oid 
        self.value = value 
    
    '''
    Get values from the firewall
    '''
    def getOid(self):
        return self.oid    
    
    '''
    Get values from the firewall
    '''
    def getValue(self):
        return self.value
    
    '''
    Convert to a string
    '''
    def toString(self):
        return str("\t"+self.value[2:-1])
        

