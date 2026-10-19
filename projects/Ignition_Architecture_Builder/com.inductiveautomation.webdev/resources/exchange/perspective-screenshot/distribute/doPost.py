def doPost(request, session):
	# Perspective Screenshot Distribution Endpoint
	# Endpoint Logger
	logger = system.util.getLogger('PerspectiveScreenshot.Distribute')
	
	# Response Container
	response = {
		'message': None
	}
	# Perform Distribution
	if request.get('postData'):
		if not request['postData'].get('filename'):
			message = "No 'filename' param found in POST request."
			logger.info(message)
			response['message'] = message
			
		if not request['postData'].get('data'):
			message = "No 'data' param found in POST request."
			logger.info(message)
			response['message'] = message
			
		# Perform distribution function
		response['message'] = exchange.perspective_screenshot.distribute.distribute(request['postData']['filename'], request['postData']['data'])
	else:
		message = "No 'postData' found in POST request."
		logger.info(message)
		response['message'] = message
	
	return {'json': response}