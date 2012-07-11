from Plugin import Plugin
import org.python.util as util
import java.io as io

class TestPlugin(Plugin):
  """ Test plugin to make sure this works and give you and idea of how to put
  together your own plugins """

  def processProxyRequest(self, msgRef, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	  print "REQUEST"

  def processProxyResponse(self, msgRef, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	  print "RESPONSE"
