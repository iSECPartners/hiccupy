README
======

Hiccupy - Jython binding for Port Swigger's BurpExtender. Hooks
`processProxyMessage` and executes plugin modules on both requests and
responses. Plugins can be dynamically modified during runtime and will be
reloaded during the next call to `processProxyMessage`, allowing you to alter
your code on the fly without having to recompile hiccupy!

Build & Install
---------------

* Update the `JYTHON_PATH` variable in src/Makefile

* Update the jython.jar location in run.sh

* Update the scope information in lib/ConfigManager.py

* `make && ./run.sh`

Plugin Development
---------------

Plugin development is meant to be quick and easy. Plugins can be developed in
a few simple steps. First create a class for your plugin:

`vim lib/plugins/plugins-available/MyPlugin.py`

     from Plugin import Plugin

     class MyPlugin(Plugin):
	""" this plugin does something super sweet """

Then code whatever processing you want to do on requests and responses into
the following respective methods: `processProxyRequest` and `processProxyResponse`.

     def processProxyRequest(self, message, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	# Here's where the fuzz goes
    
     def processProxyResponse(self, message, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	# And whatever it is you do with responses

Finally, move plugins you want to activate into the plugin/plugins-enabled/
directory and `make clean && make && ./run.sh`.

