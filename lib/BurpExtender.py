from burp import IBurpExtender
from java.net import URL
from code import InteractiveConsole
from Config import Config
from Loader import Loader
from Dispatcher import Dispatcher

class BurpExtender(IBurpExtender):
  """ hiccupy """

  def registerExtenderCallbacks(self, callbacks):
	  self.mCallBacks = callbacks
	  self.config = Config(callbacks)
	  self.loader = Loader(self.config)
	  self.dispatcher = Dispatcher(self.config, self.loader.getPlugins())

  def processProxyMessage(self, messageReference, messageIsRequest,
		  remoteHost, remotePort, serviceIsHttps, httpMethod, path,
		  resourceType, statusCode, responseContentType, message,
		  interceptAction):
    self.loader.reloadIfChanged()
    url = URL("HTTPS" if serviceIsHttps else "HTTP", remoteHost, remotePort, path)
    if self.mCallBacks.isInScope(url):
      if messageIsRequest:
	self.dispatcher.processProxyRequest(messageReference, messageIsRequest,
		      remoteHost, remotePort, serviceIsHttps, httpMethod,
		      path, resourceType, statusCode, responseContentType,
		      message, interceptAction)
      else:
	self.dispatcher.processProxyResponse(messageReference, messageIsRequest,
		      remoteHost, remotePort, serviceIsHttps, httpMethod,
		      path, resourceType, statusCode, responseContentType,
		      message, interceptAction)
    return message

  def processHttpMessage(self, toolName, messageIsRequest, message):
    if toolName == "intruder" and messageIsRequest:
      print "[%s] %s" % (toolName, message.getRequest())

# DEBUG to drop into interactive shell
#    message = message.tostring()
#    loc = dict(locals())
#    c = InteractiveConsole(locals=loc)
#    msg = "[%s] hiccupy interactive python session" % ("REQUST" if messageIsRequest else "RESPONSE")
#    c.interact(msg)

