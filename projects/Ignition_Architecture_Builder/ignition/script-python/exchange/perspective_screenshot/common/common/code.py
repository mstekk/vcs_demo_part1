### Common values used for the screenshot resource ###

### Endpoint string
ENDPOINT = '{gatewayAddress}/system/webdev/{project}/exchange/perspective-screenshot/screenshot?{params}'

### Distribution endpoint
DISTRIBUTION_ENDPOINT = '{gatewayAddress}/system/webdev/{project}/exchange/perspective-screenshot/distribute'
		
# Button Styling colors for the html doc
BUTTON_COLOR = '#D3D3D3'
ICON_COLOR = '#4691F6'

# Screenshot capture mode options
CAPTURE_MODE = [
	'only-visible' # Only capture the visible portion of the page
	, 'entire-page' # Capture a screenshot of the entire webpage
]

# Support screenshot image types
IMAGE_TYPE = [
	'png'
]

# SMTP Profile to use for distribution
SMTP_PROFILE = 'EmailSender'
