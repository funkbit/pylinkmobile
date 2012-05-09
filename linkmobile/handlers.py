import logging
import urllib
import urllib2

logger = logging.getLogger(__name__)


class SMSHandler(object):
    """
    Handler for sending SMS messages.
    
    Documentation:
    http://msgw.linkmobility.com/MessageServiceHttp.htm
    """
    
    def __init__(self, service):
        self._service = service
        
        # Set URL endpoint with auth
        self._url = '%(base_url)sMessageService.aspx?User=%(user)s&Password=%(password)s&' % {
            'base_url': self._service.base_url,
            'user': self._service.user,
            'password': self._service.password,
        }
        
        # Set default values
        self.LookupOption = 'Forced'
        self.MessageType = 'Sms'
    
    def __call__(self, *args, **kwargs):
        
        # Set the parameters on object
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        
        return self
    
    def _generate_query_string(self):
        """
        Generates the GET query string.
        """
        
        query_items = {}
        
        for key, val in self.__dict__.iteritems():
            if not key.startswith('_'):
                query_items[key] = val.encode('utf-8')
        
        return urllib.urlencode(query_items)
    
    def send(self):
        """
        Sends a SMS message.
        """
        
        # Generate the URL to call
        url = self._url + self._generate_query_string()
        logger.debug('Sending request: %s' % url)
        
        # Generate GET request
        req = urllib2.Request(url=url)
        
        if not self._service.debug:
            try:
                f = urllib2.urlopen(req)
                data = f.read()
                f.close()
            except urllib2.HTTPError, err:
                data = err.read()
                logger.error('Request failed: %s' % data, exc_info=err)
        else:
            # Debug data
            data = 'OK\r\nMessageID=1234'
        
        # Log raw response
        logger.info('Raw response: %s' % data)
        
        # Try to make sense of return value
        try:
            status, msg = data.split('\r\n')
        except ValueError:
            return data
        
        return {
            'success': status == 'OK',
            'status': status,
            'message': msg,
        }
