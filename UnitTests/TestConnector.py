__author__ = 'arif'
'''
Created on 30.10.2014

@author: Balkan Arif, Wech Maximilian
@contact: abalkan@student.tgm.ac.at, mwech@student.tgm.ac.at
@description: Testing the Model class
'''

import unittest
from Util.Connector import Connector

class Test(unittest.TestCase):

    #'5xHIT' , self.ip , 161 , 'NETSCREEN-POLICY-MIB' , 'nsPlyName'

    def setUp(self):
        global con, communityData, ip, port, mib, table
        communityData = '5xHIT'
        ip = '10.0.100.10'
        port = 161
        mib = 'NETSCREEN-POLICY-MIB'
        table = 'nsPlyName'
        con = Connector(communityData, ip, port, mib, table)

    #Constructer Testcases
    def test_Constructor_false_input(self):
        communityData = 2
        ip = 3
        port = 'text'
        mib = 4
        table = 5
        self.assertRaises(ValueError, Connector, communityData, ip, port, mib, table)

    def test_Constructor2_invalid_type_ip_port_mib_table(self):
        ip = 3
        port = 'text'
        mib = 4
        table = 5
        self.assertRaises(ValueError, Connector, communityData, ip, port, mib, table)

    def test_Constructor3_invalid_type_port_mib_table(self):
        port = 'text'
        mib = 4
        table = 5
        self.assertRaises(ValueError, Connector, communityData, ip, port, mib, table)

    def test_Constructor4_invalid_type_mib_table(self):
        mib = 4
        table = 5
        self.assertRaises(ValueError, Connector, communityData, ip, port, mib, table)

    def test_Constructor5_invalid_type_table(self):
        table = 5
        self.assertRaises(ValueError, Connector, communityData, ip, port, mib, table)

    def test_Constructor6_valid_input(self):
        result = Connector(communityData, ip, port, mib, table)

    #getRulesWithSNMPv3AndFallback Testcase
    """def test_getRulesWithSNMPv3AndFallback(self):
        result = con.getRulesWithSNMPv3AndFallback()"""

    #getRules Testcase
    def test_getRules(self):
        result = con.getRules()

    #After each test, the test runner will invoke it
    def tearDown(self):
        con = None

if __name__ == '__main__':
    unittest.main()