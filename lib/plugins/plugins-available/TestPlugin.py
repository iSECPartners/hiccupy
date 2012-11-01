from Plugin import Plugin
from re import compile

class TestPlugin(Plugin):
  """ Test plugin to make sure this works and give you and idea of how to put
  together your own plugins """

  def __init__(self, config):
	self.http_sep = compile('\r\n\r\n')
	self.config = config

  def processProxyRequest(self, msgRef, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	message = message.tostring()
	headers, body = self.http_sep.split(message)

  def processProxyResponse(self, msgRef, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	message = message.tostring()
	headers, body = self.http_sep.split(message)
