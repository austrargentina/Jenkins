Auto Generated Documentation
============================

Util.Connector. **__init__** (self,communityData,ip,port,mib,table)
	This method is the constructor of the class Connector
	communityData The user group ip The IP address to be used port The port to be connected mib The mibfile to be connected table The specific table in the mibfile 

Util.Connector. **getRules** (self)
	The method connects to the Firewall appliance (via IP, Port, user group, mib file, mib table), and checks if there are any errors occurring.
	When the check was successful and no errors were appearing,  the OIDs and the specific values will be printed separately. SNMPv2 is used.

Util.Connector. **defineData** (self,varBindTable)
	   The method handles the retrieved Data form the firewall appliance. Cause of mass results, a rectangular 	      table of var-binds will be used. The width of that table is determined by the number of var-binds in req		 uest and it never changes while some var-binds hitting end-of-MIB condition.

Util.Model. **__init__** (self)
	This is the constructor of the class Model

Util.Model. **getChart** (self)
	Get the chart and will render it

Util.Model. **setIP** (self,ip)
	Set the IP-adress for the connection
	ip IP-adress

Util.Model. **setUser** (self, user)
	Set the user for the connection
	user Username
	
Util.Model. **getFirewalllist** (self)
	Get all Firewall from the device

Util.Model. **setFirewalllist** (self, FirewallRule)
	Set the Firewalllist for the output
	FirewallRule Firewall rule which you want

Util.Model. **listToFile** (self)
	Save the firewall output in an extra .txt-file

Util.Model. **refresh** (self)
	Refresh the website

Util.Model. **RulesToString** (self,name)
	Convert the output to a string
	name Rulename

Util.Model. **getThroughputValues** (self)
	Get the values for drawing the policies chart

Util.Model. **validIP** (self,ip)
	Validation of the IP-adress
	ip IP-adress

Util.RenderChart. **__init__** (self)
	This is the constructor of the class Renderchart

Util.RenderChart. **setValues** (self,array)
	Set the values for the policies chart
	array Throughput values

Util.RenderChart. **render** (self)
	Draw the chart

Objekte.FirewallRule. **__init__** (self,oid,value)
	This is the constructor for the class FirewallRule
	oid OID number
	value

Objekte.FirewallRule. **getValue** (self)
	Get values from the firewall	

Objekte.FirewallRule. **toString** (self)
	Convert to a string

Objekte.Throughput. **__init__** (self,value,date)
	This is the constructor of the class Throughput
	
GUI.Controller. **__init__** (self)
	This is the constructor of the class View
	
GUI.Controller. **index** (self)
	Render the index.html flask template

GUI.Controller. **login** (self)
	Render the login.html flask template

GUI.Controller. **connect** (self)
	By pushing the connect button the method test our input for validation and if there is a successful input i'll get a message

GUI.Controller. **rules** (self)
	Render the rules.html flask template

GUI.Controller. **getRules** (self)
	Get the Firewall rules

GUI.Controller. **getzones** (self)
	Get zones of the firewall

GUI.Controller. **getpolicies** (self)
	Get policies of the firewall

GUI.Controller. **getservices** (self)
	Get services of the firewall

GUI.Controller. **tofile** (self)
	Save the output-rules to an extra .txt-file	

GUI.Controller. **chart** (self)
	Render the chart.html flask template

GUI_Testing.test. **setUp** (self)
	Initialize the test environment

GUI_Testing.test. **text_search_in_python_org** (self)
	Check the IP-adress input with not allowed inputs like text 

UnitTests.TestModel. **setUp** (self)
	Initialize the test environment

UnitTests.TestsModel. **testValidIp** (self)
	Test the IP-adress input

UnitTests.TestModel. **testValidIp2** (self)
	Other Test for the IP-adress input

UnitTests.TestModel. **testValidWrongParameterType** (self)
	Test the user input

UnitTests.TestModel. **testValidWrongParameterType** (self)
	Other test for the user input

UnitTests.TestModel. **testValidIpWrongIP** (self)
	Check false ip

UnitTests.TestModel. **testValidIpTooManyParts** (self)
	Check the length of the ip adress

UnitTests.TestModel. **testValidIpNumberTooHigh** (self)
	One part of an ip-adress shouldn't have more than 255

UnitTests.TestModel. **testsetIp** (self)
	Test if we can set the ip-adress

UnitTests.TestModel. **testsetIpWrongParameterType** (self)
	Test if we can set a false ip-adress

UnitTests.TestModel. **testsetUser** (self)
	Test if we can set the user for the device

UnitTests.TestModel. **testsetUserFails** (self)
	Test if we can set a false user

UnitTests.TestModel. **testGetChart** (self)
	Test if we get a chart

UnitTests.TestModel. **testGetThroughputValues** (self)
	Test if we get the values for drawing the throughput

UnitTests.TestModel. **testRuleToString** (self)
	Test if we can convert the rules the a string

UnitTests.TestModel. **testRulesToStringNotIsString** (self)
	Test if we have really converted the rules to a string	

UnitTests.TestModel. **testRefresh** (self)
	Test if we can refresh the website

UnitTests.TestModel. **testListToFile** (self)
	Test if can save the output as a .txt-file

UnitTests.TestModel. **tearDown** (self)
	Tear down of the testclass	
