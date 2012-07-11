class Plugin:
    """ base class for all plugins """
    def __init__(self, config):
        self.config = config                                       
        print "[%s] plugin initialized" % (self.__module__)                    
                                                                               
    def __del__(self):                                                         
        pass
