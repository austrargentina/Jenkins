'''
Created on 29.09.2014

@author: Daniel Scheuch
@contact: daniel.scheuch@student.tgm.ac.at
@description: The renderchart class renders our chart and set our options for the chart
'''
import pygal
from pygal.style import Style
class RenderChart():
    path = ""
    label = ""
    values = []
    def __init__(self): 
         self.path = 'GUI/static/img/charts/line_chart.svg'
         self.label = 'B/s'
         self.values = [324,234,234,122,543,3,452]
         self.times = ['15:55:01','15:55:02','15:55:03','15:55:04','15:55:05','15:55:06']
   
    def setValues(self,array):
        if isinstance(array, list):
            self.values = array  
        else: 
            raise ValueError('Only Lists allowed')   
         
    def render(self):
       custom_style = Style(
              background='transparent',
              plot_background='transparent',
              foreground='#53E89B',
              foreground_light='#53A0E8',
              foreground_dark='#630C0D',
              opacity='.6',
              opacity_hover='.9',
              transition='400ms ease-in',
              colors=('#E89B53')
              )
        
       chart = pygal.StackedLine(fill=True, style=custom_style, x_label_rotation=20)
       chart.x_labels = self.times
       chart.add(self.label, self.values)
       chart.render_to_file(self.path)
    