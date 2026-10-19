def doGet(request, session):
	# Get the endpoint params to pass into the html.getDocument function
	mode = request['params'].get('mode', 'onclick') # onclick | onload
	elementId = request['params'].get('elementId', 'app-container')
	captureMode = request['params'].get('captureMode', 'only-visible')
	imageName = request['params'].get('imageName', 'screenshot')
	imageType = request['params'].get('imageType', 'png')
	distribute = request['params'].get('distribute', False)
	gateway = request['params'].get('gateway')
	project = request['params'].get('project')
	
	# Return the HTML document
	return {'html': exchange.perspective_screenshot.html.getDocument(mode, elementId, captureMode, imageName, imageType, distribute, gateway, project)}