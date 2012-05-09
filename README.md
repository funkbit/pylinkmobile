# pylinkmobile

pylinkmobile is a Python module for interacting with the Link Mobile Solutions API.

The API documentation is available here:
http://msgw.linkmobility.com/MessageService.htm

## Installation

Install `pylinkmobile` (available on PyPi):

	pip install pylinkmobile


## Usage

	from linkmobile.service import MessageService
	
	service = MessageService(user='YOUR_USERNAME', password='YOUR_PASSWORD', debug=False)
	
	# Send SMS
    sms = service.sms(
        Data='Hello World!',
        Originator='Santa',
        Msisdn='+4700000000'
    )
    response = sms.send()
