# encoding: utf-8
import logging
import sys
import unittest

from linkmobile.handlers import SMSHandler
from linkmobile.service import MessageService

# Basic logging of the tests
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')


class TestService(unittest.TestCase):
    """
    Test initialization of service.
    """
    
    def testServiceSetup(self):
        
    	service = MessageService(username='YOUR_USERNAME', password='YOUR_PASSWORD', debug=True)
	    
        # Check default values and setting of kwargs
        self.assertEquals(service.user, 'YOUR_USERNAME')
        self.assertEquals(service.password, 'YOUR_PASSWORD')
        self.assertTrue(service.debug)
        
        # Check that the order handlers are present
        self.assertTrue(isinstance(service.sms, SMSHandler))

class TestSMS(unittest.TestCase):
    """
    Test the SMSHandler methods.
    """
    
    def testSendMessage(self):
        """
        Test the SMS send method.
        """
        
    	service = MessageService(username='USER', password='PASS', debug=True)
	    
    	# Generate SMS object
        sms = service.sms(
            Data=u'Hello Wørld!',
            Originator='Santa',
            Msisdn='+4700000000'
        )
        
        # Check the object
        self.assertEquals(type(sms), SMSHandler)
        
        response = sms.send()
        
        # Check debug response
        self.assertTrue(response)
        self.assertTrue(response['success'])
        self.assertEquals(response['raw_response'], 'OK\r\nMessageID=1234')
        self.assertEquals(response['message'], 'MessageID=1234')
        self.assertEquals(response['MessageID'], '1234')
    
    def testParseFailedResponse(self):
        """
        Test the parseResponse method.
        """
        
    	service = MessageService(username='USER', password='PASS', debug=True)
        
    	# Generate SMS object
        sms = service.sms(
            Data=u'Hello Wørld!',
            Originator='Santa',
            Msisdn='+4700000000'
        )
        
        # Parse an error message
        data = 'NOK\r\nAccess is denied. Incorrect user or password.'
        response = sms.parse_response(data)
        
        # Check debug response
        self.assertTrue(response)
        self.assertFalse(response['success'])
        self.assertEquals(response['raw_response'], data)
        self.assertEquals(response['message'], 'Access is denied. Incorrect user or password.')
        

if __name__ == "__main__":
    unittest.main()
