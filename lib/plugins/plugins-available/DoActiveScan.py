from Plugin import Plugin

class DoActiveScan(Plugin):
  """
  DoActiveScan just basically sends all in-scope requests to the active scanner.
  Calling doActiveScan returns an IScanQueueItem that can be used to inspect the
  scanner results.
  """

  def __init__(self, config):
	self.config = config
	self.scanQueueItems = []

  def processProxyRequest(self, msgRef, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	# keep a reference to the returned IScanQueueItem
	self.scanQueueItems.append(self.config['callbacks'].doActiveScan(remoteHost,
		remotePort, serviceIsHttps, message))
	for item in self.scanQueueItems:
	  print "Percentage complete: %s" % item.getPercentageComplete()
	  if item.getPercentageComplete() == '100':
	    for issue in item.getIssues():
	      print "\tUrl: %s" % issue.getUrl()
	      print "\tIssue: %s" % issue.getIssueName()

  def processProxyResponse(self, msgRef, messageIsRequest, remoteHost,
		  remotePort, serviceIsHttps, httpMethod, path, resourceType,
		  statusCode, responseContentType, message, interceptAction):
	  print "NO RESPONSE ACTIONS"
