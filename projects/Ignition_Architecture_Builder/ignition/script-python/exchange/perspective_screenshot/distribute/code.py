### PerspectiveScreenshot distribution function -- used in the webdev endpoint > perspective-screenshot/distribute ###
from exchange.perspective_screenshot.common.common import SMTP_PROFILE

def distribute(sendTo, filename, data):
	"""Screenshot distribution function, sends email using system.net.sendEmail
	
	Args:
		sendTo: list of emails to send screenshot to
		filename: name of the file for the attached image
		data: image data from the client
	Returns:
		string message
	"""
	# Script Logger
	logger = system.util.getLogger('PerspectiveScreenshot.Distribute')
	
	# Try/Except Block
	try:
		# Convert image data into binary format
		imgData = data.split(',')[-1].decode('base64')
		
		# Send email
		system.net.sendEmail(
			fromAddr='perspective-screenshot@ia.com' ## Enter your own from email here
			, subject='Perspective Screenshot - {0}'.format(system.date.now())
			, body='Perspective Screenshot'
			, to=[sendTo]
			, attachmentNames=[filename]
			, attachmentData=[imgData]
			, smtpProfile=SMTP_PROFILE
		)
		message = 'Screenshot Distributed'

	except Exception, e:
		# On exception log, and set error message
		logger.error(str(e))
		message = 'Error; {0}'.format(str(e))
	return message