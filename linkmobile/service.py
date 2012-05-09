from linkmobile.handlers import SMSHandler


class MessageService(object):
    """
    Base SMS service.
    
    Documentation:
    http://msgw.linkmobility.com/MessageService.htm
    """
    
    def __init__(self, username, password, debug=True):
        
        # Set account credentials
        self.user = username
        self.password = password
        self.debug = debug
        
        # Default base URL
        self.base_url = 'http://msgw.linkmobility.com/'
        
        # Add agreement handlers
        self.add_resource('sms', SMSHandler)
    
    def add_resource(self, name, handler):
        """
        Initializes the handler with this service instance.
        """
        
        setattr(self, name, handler(self))
