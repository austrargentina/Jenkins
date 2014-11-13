'''
Created on 30.10.2014

@author: Maximilian Wech
@contact: maximilian.wech@student.tgm.ac.at
@description: Unit Tests for RenderChart
'''
import unittest
from Util.RenderChart import RenderChart

class Test(unittest.TestCase):
    #This method will run prior to each test; Creating an Instance of a Class
    def setUp(self):
        global rend
        rend = RenderChart()

    def testRenderChart(self):
        array = [324,234,234,122,543,3,452]
        result = rend.setValues(array)

    def testRenderChartWrongTypeInt(self):
        array = 1
        self.assertRaises(ValueError, rend.setValues, array)
        
    def testRenderChartWrongTypeBoolean(self):
        array = True
        self.assertRaises(ValueError, rend.setValues, array)
        
    def testRender(self):
        result = rend.render()
    
    #After each test, the test runner will invoke it      
    def tearDown(self):
        rend = None


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()