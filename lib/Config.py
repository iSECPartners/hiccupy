from java.net import URL

class Config:
  """ handles intializiation and modifcation of hiccupy global config """

  def __init__(self, callbacks):
    self.config = {}

    # Burp specific configs
    self.config['callbacks'] = callbacks
    self.config['callbacks'].setProxyInterceptionEnabled(True)
    conf_to_reload = self.config['callbacks'].saveConfig()
    conf_to_reload['proxy.interceptresponses'] = True
    self.config['callbacks'].loadConfig(conf_to_reload)

    # Scope
    url  = URL("HTTPS", "isecpartners.com.com", 443, "/")
    self.config['callbacks'].includeInScope(url)

    # Hiccupy specific configs
    self.config['path_2_enabled_plugins'] = './lib/plugins/plugins-enabled/'
    self.config['debug'] = True

    print "[%s] Completed configuration load" % self.__class__.__name__

#    if self.config['debug']:
#      tmp_cnf = self.config['callbacks'].saveConfig()
#      for option in tmp_cnf.entrySet():
#	      print "%s => %s" % (option.key, option.value)

  def __getitem__(self, key):
    return self.config[key]

  def __setitem__(self, key, value):
    self.config[key] = value
