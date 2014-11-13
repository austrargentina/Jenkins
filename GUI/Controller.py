'''
Created on 07.10.2014

@author: Daniel Scheuch
@contact: daniel.scheuch@student.tgm.ac.at

@description: The controller class handels our user inputs and calls the methods
'''
import flask.views
from markupsafe import Markup
from Util.Model import Model
from flask.globals import request
app = flask.Flask(__name__)
app.secret_key ="geheim"

class View(flask.views.MethodView):    
    '''
    This is the constructor of the class View
    '''
    def __init__(self): 
         self.model1 = Model()
    
    '''
    When the index route is called we get our index.html
    '''    
    @app.route('/',methods=['GET','POST'])  
    def index(): 
        return flask.render_template('index.html')   
    
    '''
    When the /login route is called we get our login.html
    '''
    @app.route('/login',methods=['GET','POST'])    
    def login():
        return flask.render_template('login.html')  
    
    '''
    When the connect route is called we get our index.html back with a prompt if the connection was successfull if not the we got an error message
    '''
    @app.route('/login/connect',methods=['GET','POST']) 
    def connect():
        #CHECK IP
        flash=""
        model1 = Model()
        errorOpen = "<div class='error'>"   
        errorContent = ""
        successOpen = "<div class='success'>" 
        successContent = "" 
        divClose = "</div>"
        isError = False
        isSuccess = False
        validIP = model1.validIP(flask.request.form['ip'])
        
        if validIP == False:
            errorContent += "please enter correct ip!<br/>"
            isError = True
        else:
            model1.setIP(flask.request.form['ip']) 
            isSuccess = True
            successContent = "Successful logged in to device"
            
        if isError == True:
            flash += errorOpen+errorContent+divClose
            
        if isSuccess == True:
            flash += successOpen+successContent+divClose
        flask.flash(Markup(flash))      
        
        return flask.render_template('rules.html')  
    
    '''
        ssh route to get the ssh.html
    '''
    @app.route('/ssh',methods=['GET','POST'])    
    def ssh():               
        return flask.render_template('ssh.html') 
    
    '''
    send ssh rout to get the ssh html bac with the return
    '''
    @app.route('/ssh/send',methods=['GET','POST'])    
    def sshsend(): 
        flash=""
        data = []
        isError = False
        errorOpen = "<div class='error'>"   
        errorContent = ""
        divClose = "</div>"
        
        model1 = Model()
        ip = flask.request.form['ip']
        user = flask.request.form['user']
        pw = flask.request.form['pw']
        cmd = flask.request.form['cmd']
        flash += "return from "+str(ip)+"<br><br>"
        validIP = model1.validIP(ip)
        if validIP == False:
            errorContent += "please enter correct ip!<br/>"
            isError = True
        else:
            data = model1.connectSSH(ip, user, pw, cmd)
         
        for i in range(1,len(data)):
            flash += ip+"> " +data[i]+"<br/>"
            
        if isError == True:
            flash += errorOpen+errorContent+divClose  
              
        flask.flash(Markup(flash))
        return flask.render_template('ssh.html') 
    
    '''
    Render the rules.html flask template
    '''
    @app.route('/rules',methods=['GET','POST'])    
    def rules():               
        return flask.render_template('rules.html')  
    
    '''
    getrules route for gettng the rules.html
    '''
    @app.route('/rules/getrules', methods=['GET','POST'])
    def getrules():
        return flask.render_template('rules.html') 
    
    '''
    route for Getting zones of the firewall
    '''
    @app.route('/rules/getrules/zones', methods=['GET','POST'])
    def getzones():
        flash=""
        model1 = Model()
        flash += '<h1>zones</h1>'
        flash += model1.RulesToString('zones')
        flash += '<br/><br/>' 
        flask.flash(Markup(flash)) 
        return flask.render_template('rules.html') 
    
    '''
    route for Getting policies of the firewall
    '''
    @app.route('/rules/getrules/policies', methods=['GET','POST'])
    def getpolicies():
        flash=""
        model1 = Model()
        flash += '<h1>policies</h1>'
        flash += model1.RulesToString('policies')
        flash += '<br/><br/>' 
        flask.flash(Markup(flash)) 
        return flask.render_template('rules.html')
    
    '''
    route for Getting services of the firewall
    '''
    @app.route('/rules/getrules/services', methods=['GET','POST'])
    def getservices():
        flash=""
        model1 = Model()
        flash += '<h1>services</h1>'
        flash += model1.RulesToString('services')
        flash += '<br/><br/>' 
        flask.flash(Markup(flash)) 
        return flask.render_template('rules.html')  
    
    '''
    route for getting the txt file
    '''
    @app.route('/tofile', methods=['GET','POST'])
    def tofile():
        #SAVE TO FILE
        flash = ""
        successOpen = "<div class='success'>" 
        successContent = ""
        isSuccess = False
        divClose = "</div>"
        model1 = Model()
        listFile = model1.listToFile()
        if listFile == True:
            successContent += "successful writen to file in /static/file/Firewall_Rules.txt!"
            isSuccess = True
            
        if isSuccess == True:
            flash += successOpen+successContent+divClose
                 
        flask.flash(Markup(flash))   
        return flask.render_template('rules.html')
    
    '''
    route for getting the chart (html and .svg file)
    '''    
    @app.route('/chart', methods=['GET','POST'])    
    def chart():
        #model1 = Model()
        #model1.getChart
        flash = ""
        flash += "<h1> Throughput of Policies: </h1>"
        flash += "<object data='static/img/charts/line_chart.svg' type='image/svg+xml'></object>"
        flask.flash(Markup(flash))
        return flask.render_template('chart.html')
        
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])
app.debug = True
app.run()