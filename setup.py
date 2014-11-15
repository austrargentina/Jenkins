'''
Created on 10.10.2014
@author: Daniel Scheuch
@contact: daniel.scheuch@student.tgm.ac.at
@description: Starts our services
'''
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'GUI'))

from GUI.Controller import View
if __name__ == '__main__':    
    v = View()
    
