# Imports
from exchange.perspective_screenshot.common.html import onclick, onload, error

## Function
def getDocument(
	mode='onclick'
	, elementId='app-container'
	, captureMode='only-visible'
	, imageName='screenshot'
	, imageType='png'
	, distribute=False
	, gateway=None
	, project=None
	):
	"""Get the HTML document to be returned by the webdev endpoint
	
	Args:
		mode: document display mode (onclick | onload)
		elementId: DOM id of the element to capture screenshot of 
		captureMode: boolean flag to indicate if the screenshot should include
			the entire page (scrollable area etc) or only the visible portion
		imageName: name of the file to be used
		imageType: type of the image (png)
		distribute: whether to distribute the screenshot image or save locally
		gateway: gateway address to use for the distribution endpoint
		project: project name where distribution endpoint exists
	Returns:
		html doc string
	"""
	logger = system.util.getLogger('PerspectiveScreenshot.HtmlDocument')
	
	if mode == 'onclick':
		document = onclick.HtmlDocument(elementId, captureMode, imageName, imageType, distribute, gateway, project).doc
	elif mode == 'onload':
		document = onload.HtmlDocument(elementId, captureMode, imageName, imageType, distribute, gateway, project).doc
	elif mode == 'dev':
		document = dev.HtmlDocument(elementId, captureMode, imageName, imageType, distribute, gateway, project).doc
	else:
		document = error.HtmlDocument().doc
		logger.info("Invalid mode '{0}'.".format(mode))
	return document