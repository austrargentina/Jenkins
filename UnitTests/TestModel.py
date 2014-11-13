'''
Created on 28.10.2014

@last update 30.10.2014
@author: Maximilian Wech, Balkan Arif
@contact: maximilian.wech@student.tgm.ac.at, abalkan@student.tgm.ac.at
@description: Testing the Model class
'''
import unittest
from Objekte.FirewallRule import FirewallRule
from Util.Model import Model

class Test(unittest.TestCase):

    #This method will run prior to each test; Creating an Instance of a Class
    def setUp(self):
        global mod, ipadress
        mod = Model()
        ipadress = '10.0.100.10'

    def testValidIp(self):
        expected = ipadress
        result = mod.validIP(expected)

    def testValidIp2(self):
        expected = True
        actual = mod.validIP(ipadress)
        self.assertEquals(expected,actual)

    def testValidIpWrongParameterType(self):
        self.assertRaises(ValueError, mod.setUser, True)

    def testValidIpWrongParameterType2(self):
       self.assertRaises(ValueError, mod.setUser, 2)

    def testValidIpWrongIp(self):
       actual = mod.setIP('10.0..100.10')
       expected = None
       self.assertEquals(actual, expected)

    def testValidIpTooManyParts(self):
        expected = False
        actual = mod.validIP('10.0.0.100.10')
        self.assertEquals(actual, expected)

    def testValidIpNumberTooHigh(self):
        expected = False
        actual = mod.validIP('10.0.100.257')
        self.assertEquals(actual, expected)

    def testValidIpNumberTooHighTwo(self):
        expected = False
        actual = mod.validIP('10.0.257.10')
        self.assertEquals(actual, expected)

    def testsetIp(self):
        result = mod.setIP('10.0.100.10')
      
    def testSetIpWrongParameterTypeInt(self):
        self.assertRaises(ValueError, mod.setIP, 2)
        
    def testSetIpWrongParameterTypeArray(self):
        self.assertRaises(ValueError, mod.setIP, [1,2])

    def testsetUser(self):
        result = mod.setUser('5xHIT')
    
    def testSetUserWrongParameterTypeInt(self):
        self.assertRaises(ValueError, mod.setUser, 2)
        
    def testSetUserWrongParameterTypeArray(self):
        self.assertRaises(ValueError, mod.setUser, [1,2])

    def testGetChart(self):
        result = mod.getChart()

    def testGetThroughputValues(self):
        result = mod.getThroughputValues()

    def testRulesToString(self):
        result = mod.RulesToString('policies')

    def testRulesToStringNotIsString(self):
        self.assertRaises(ValueError, mod.RulesToString, 0)

    def testRefresh(self):
        result = mod.refresh()

    def testListToFile(self):
        expected = True
        actual = mod.listToFile()
        self.assertEquals(actual, expected)

    #After each test, the test runner will invoke it  
    def tearDown(self):
        mod = None


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()