class Dispatcher:
  """ dispatches calls to enabled plugins. """

  def __init__(self, config, plugins):
    self.config = config
    self.plugins = plugins

  def processProxyRequest(self, messageReference, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
    for plugin in self.plugins.keys():
      if self.config['debug']:
        print "[%s] %s.processProxyRequest" % (self.__class__.__name__, plugin)
      self.plugins[plugin].processProxyRequest(messageReference, messageIsRequest,
		      remoteHost, remotePort, serviceIsHttps, httpMethod,
		      path, resourceType, statusCode, responseContentType,
		      message, interceptAction)
 
  def processProxyResponse(self, messageReference, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
    for plugin in self.plugins.keys():
      if self.config['debug']:
        print "[%s] %s.processProxyResponse" % (self.__class__.__name__, plugin)
      self.plugins[plugin].processProxyResponse(messageReference, messageIsRequest,
		      remoteHost, remotePort, serviceIsHttps, httpMethod,
		      path, resourceType, statusCode, responseContentType,
		      message, interceptAction)

