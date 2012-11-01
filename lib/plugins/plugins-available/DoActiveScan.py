from Plugin import Plugin
from re import compile

class DoActiveScan(Plugin):
  """
  DoActiveScan just basically sends all in-scope requests to the active scanner.
  Calling doActiveScan, a IScanQueueItem
  """

  def __init__(self, config):
	self.http_sep = compile('\r\n\r\n')
	self.config = config

  def processProxyRequest(self, msgRef, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	self.config['callbacks'].doActiveScan(remoteHost, remotePort,
			serviceIsHttps, message)
	print "Added request to active scanner"

  def processProxyResponse(self, msgRef, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	  print "NO RESPONSE ACTIONS"
