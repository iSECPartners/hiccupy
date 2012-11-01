import os
import re
from Dispatcher import Dispatcher

class Loader:
  """ initializes dispatcher and enabled plugins. """

  def __init__(self, config):
    self.config = config
    self.plugin_mtimes = {}
    self.path = self.config['path_2_enabled_plugins']
    self.plugins, self.mods = self.loadPlugins(self.findEnabledPlugins(self.path))

  def findEnabledPlugins(self, path):
    print "[%s] Searching for plugins in: %s" % (self.__class__.__name__, path)
    plugins = []
    listing = os.listdir(path)
    for plugin in listing:
      self.plugin_mtimes[plugin] = os.stat(self.path + plugin).st_mtime
      if re.match('(\S+)\.py$', plugin):
	plugins.append(plugin)
        if self.config['debug']:
          print "[%s] Found plugin: %s" % (self.__class__.__name__, plugin)
    return plugins

  def loadPlugins(self, plugins):
    enabledMods = {}
    enabledPlugins = {}
    for plugin in plugins:
      mod = plugin[:-3]
      if self.config['debug']:
	 print "[%s] Trying to enable: %s" % (self.__class__.__name__, plugin)
      enabledMods[plugin] = __import__(mod)
      try:
        enabledPlugins[plugin] = getattr(enabledMods[plugin], mod)(self.config)
      except AttributeError, e:
	print "[%s] Failed to load plugin: %s => %s" % (self.__class__.__name__, plugin, e) 
    return enabledPlugins, enabledMods

  def getPlugins(self):
    return self.plugins

  def reloadIfChanged(self):
    for plugin in self.plugins:
      mtime = os.stat(self.path + plugin).st_mtime 
      if mtime > self.plugin_mtimes[plugin]:
        if self.config['debug']:
	  print "[%s] Plugin modified: %s" % (self.__class__.__name__, plugin)
	mod = reload(self.mods[plugin])
	self.plugins[plugin] = getattr(mod, plugin[:-3])(self.config)
	self.plugin_mtimes[plugin] = mtime

