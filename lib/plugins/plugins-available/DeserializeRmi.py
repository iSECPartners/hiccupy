from Plugin import Plugin
import re
import org.python.util as util
import java.io as io
from sys.path import append
from os import walk
from os.path import join

class DeserializeRmi(Plugin):
  """
  This plugin accepts an RMI input stream and decodes it. Extend it to do any
  additional inspection on the received objects.
  """

  def __init__(self, config):
	self.config = config
	self.http_sep = re.compile('\r\n\r\n')
	# append any specific jars to the path
	for dirname, dirnames, filenames in walk('~/current/code/jars'):
	  for filename in filenames:
	    if ".jar" in filename:
	      append(join(dirname, filename))
	      print "Appended to path: %s" % join(dirname, filename)

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
	stream = util.PythonObjectInputStream(body)
	instance = stream.readObject()
	print "=" * 5 + "Decoded RMI Object" + "=" * 5
	print instance.toString()
	print "=" * 28
