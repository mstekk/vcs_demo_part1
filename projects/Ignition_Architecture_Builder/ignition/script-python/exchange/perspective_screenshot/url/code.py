# Imports
from exchange.perspective_screenshot.common.common import ENDPOINT

# Url formatting function
def get(gatewayAddress, project=None, **params):
	"""Format the url string to point to the gateway screenshot endpoint
	
	Args:
		gatewayAddress: address of the gateway where the screenshot endpoint is 
			located (recomended to pass in the 'session.props.gateway.address' property)
		project: name of the project on the gateway where the project exists (default: None, uses the current project name)
		params: key word args to pass into the endpoint
	"""
	args = {
		'gatewayAddress': gatewayAddress
		, 'project': project if project else system.project.getProjectName()
		, 'params': '&'.join(["{key}={value}".format(key=key, value=value) for key, value in params.items() if bool(value)])
	}
	args['params'] += '&gateway={0}&project={1}'.format(gatewayAddress, project)
	return ENDPOINT.format(**args)