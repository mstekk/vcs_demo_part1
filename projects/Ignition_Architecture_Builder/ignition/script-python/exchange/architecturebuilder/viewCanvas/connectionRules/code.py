CONNECTIONALLTYPES={
				"Gateway Network":
					{'color': "var(--ignition-orange)",
					"docs": 'https://docs.inductiveautomation.com/docs/8.1/platform/gateway-network',
					"multiple": False},
				"MQTT":
					{'color': 'var(--cirrusLink)',
					"docs": "https://docs.chariot.io/display/CLD80/Cirrus+Link+Ignition+Modules",
					"multiple": True},
				'Device Driver':
					{'color':  'var(--seq-3)',
					"docs": "https://docs.inductiveautomation.com/docs/8.1/ignition-modules/opc-ua/opc-ua-drivers",
					"multiple": True},
				'OPC-UA':
					{'color': '#FFE7BA',
					"docs": "https://docs.inductiveautomation.com/docs/8.1/ignition-modules/opc-ua",
					"multiple": True},
				'OPC-COM':
					{'color': '#FFE7BA',
					"docs": "https://docs.inductiveautomation.com/docs/8.1/ignition-modules/opc-ua/third-party-opc-servers/opc-com",
					"multiple": True},
#				'OPC-UA SSL':
#					{'color':  '#FFE7BA',
#					"docs": "https://docs.inductiveautomation.com/docs/8.1/ignition-modules/opc-ua",
#					"multiple": True},
				'DB':
					{'color': '#34A853',
					"docs": "https://docs.inductiveautomation.com/docs/8.1/platform/database-connections",
					"multiple": True},
				'Client':
					{'color': 'var(--neutral-60)',
					"docs": "https://docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/perspective-sessions",
					"multiple": False},
				'Standard':
					{'color': 'var(--neutral-100)',
					"docs": "https://docs.inductiveautomation.com/docs/8.1/platform/gateway/status/connections",
					"multiple": True},
				'MongoDB':
					{'color': 'green',
					"docs": "https://docs.inductiveautomation.com/docs/8.1/ignition-modules/cloud-connector-modules/mongodb",
					"multiple": True}
				}
				
COMPONENTPATH="Exchange/ArchitectureBuilder/Components/{path}/"	
COMPONENTTYPES={
	'standard':{
		'name': 'Standard Gateway',
		'path': COMPONENTPATH.format(path='Server'), 
		'icon': {'path':'material/assessment', 'color': 'var(--standard)', 'style':{}}}, 
	'edge':{
		'name': 'Edge IIOT  Gateway',
		'path': COMPONENTPATH.format(path='Server'), 
		'icon': {'path':'material/assessment', 'color': 'var(--edge)', 'style':{}}}, 
	'panel':{
		'name': 'Edge Panel Gateway',
		'path': COMPONENTPATH.format(path='Server'), 
		'icon': {'path':'material/assessment', 'color': 'var(--panel)', 'style':{}}}, 
	'cloud':{
		'name':'Cloud Gateway',
		'path': COMPONENTPATH.format(path='Server'), 
		'icon': {'path':'material/assessment', 'color': 'var(--cloud)', 'style':{}}}, 
	'Database':{
		'name': 'Database',
		'path': COMPONENTPATH.format(path='Database'), 
		'icon': {'path':'material/view_agenda', 'color': '#34A853', 'style':{}}} , 
	'Device':{
		'name': 'Device',
		'path': COMPONENTPATH.format(path='Device'), 
		'icon': {'path':'material/settings_input_composite', 'color': 'var(--seq-3)', 'style':{}}}, 
	'Client':{
		'name': 'Client',
		'path': COMPONENTPATH.format(path='Client'), 
		'icon': {'path':'material/computer', 'color': 'var(--neutral-60)', 'style':{}}},
	'Connector':{
		'name': 'Connector',
		'path': COMPONENTPATH.format(path='Cloud'), 
		'icon': {'path':'material/cloud_queue', 'color': '', 'style':{}}}, 
	'Comms':{
		'name': 'Communication',
		'path': COMPONENTPATH.format(path='Server'), 
		'icon': {'path':'material/signal_cellular_alt', 'color': '', 'style':{}}}, 
	'LoadBalancer':{
		'name': 'Load Balancer',
		'path': COMPONENTPATH.format(path='Loadbalancer'), 
		'icon': {'path':'material/call_split', 'color': '', 'style':{}}}, 
	'MongoDB':{
		'name': 'MongoDB',
		'path': COMPONENTPATH.format(path='MongoDB'), 
		'icon':  {'path':'material/emoji_symbols', 'color': 'green', 'style':{}}}, 
	'OPCUA':{
		'name': 'OPC-UA Server',
		'path': COMPONENTPATH.format(path='OPCUA'), 
		'icon': {'path':'material/table_chart', 'color': '#FFE7BA', 'style':{}}}, 
	'Note':{
		'name': 'Note',
		'path': COMPONENTPATH.format(path='Notes'), 
		'icon': {'path':'material/sticky_note_2', 'color': '', 'style':{}}},
	'Firewall':{
		'name': 'Firewall',
		'path': COMPONENTPATH.format(path='Firewall'), 
		'icon': {'path':'material/lock', 'color': 'RED', 'style':{}}},
	'Custom':{
		'name': 'Custom',
		'path': COMPONENTPATH.format(path='Custom'), 
		'icon': {'path':'material/input', 'color': '', 'style':{}}},
	'IIOT':{
		'name': 'IIOT',
		'path': COMPONENTPATH.format(path='IIOT'), 
		'icon': {'path':'material/cloud_queue', 'color': 'var(--cirrusLink)', 'style':{}}},
	'ReverseProxy':{
		'name': 'Reverse Proxy',
		'path': COMPONENTPATH.format(path='ReverseProxy'), 
		'icon': {'path':'material/security', 'color': '', 'style':{}}},
	'Usersource':{
		'name': 'User Source',
		'path': COMPONENTPATH.format(path='Usersource'), 
		'icon': {'path':'material/supervised_user_circle', 'color': '', 'style':{}}},
	'fourIR':{
		'name': '4IR',
		'path': COMPONENTPATH.format(path='4IR'), 
		'icon': {'path':'material/supervised_user_circle', 'color': '', 'style':{}}},
	'server':{
		'name': 'Server',
		'path': COMPONENTPATH.format(path='ServerGen'), 
		'icon': {'path':'material/supervised_user_circle', 'color': '', 'style':{}}},
	}



componentRules={
		'edge': {
			'disallow': ['Database', 'Client', 'MongoDB'],
			'limited': ['edge', 'panel'],
			'limitedMessages':{},
			'approval': []
		},
		'panel': {
			'disallow': ['Database', 'MongoDB'],
			'limited': ['edge', 'panel', 'Client'],
			'limitedMessages':{'Client': ' (2 Clients Total)'},
			'approval': []
		},
		'cloud': {
			'disallow': ['Device'],
			'limited': [],
			'limitedMessages':{},
			'approval': []
		},
		'standard': {
			'disallow': [],
			'limited': [],
			'limitedMessages':{},
			'approval': []
		},
		'all':{
			'disallow': ['Note'],
			'limited': [],
			'limitedMessages':{},
			'approval': []
		}
	}
def preEstablishedConnectionRules(targetConnection, preDefinedConnections):
	if targetConnection==None or targetConnection=='':
		return {'allow': False, 'limited': False, 'approval': False, 'message': ''}
	allowMultiple=CONNECTIONALLTYPES[targetConnection]['multiple']
	if not allowMultiple and targetConnection in preDefinedConnections:
		message="Multiple {} connections between the same components is NOT Allowed".format(targetConnection)
		return {'allow': False, 'limited': False, 'approval': False, 'message': message}
	else:
		return {'allow': True, 'limited': False, 'approval': False, 'message': ''}
	
	
	
def getIconByType(typeid):
	"""	Retrieves the icon details based on the component type ID.
	Args:
	    typeid (str): The type ID of the component.
	Returns:
	    dict: A dictionary containing the icon details.
	"""
	if typeid in COMPONENTTYPES.keys():
		return COMPONENTTYPES[typeid]['icon']
	else:
		return {'path': "material/location_city", 'color': '', 'style':{}}

def getComponentPath(typeid, view='Main'):
	"""	Constructs the component path based on the type ID and view.
	Args:
	    typeid (str): The type ID of the component.
	    view (str, optional): The view type to append to the path. Default is 'Main'.
	Returns:
	    str: The constructed component path.
	"""
	return COMPONENTTYPES[typeid]['path']+view

def getConnectionAllTypes():
	return CONNECTIONALLTYPES

def getConnectionTypes():
	return CONNECTIONALLTYPES.keys()

def getConnectionColor(connectionType):
	"""	Retrieves the color associated with a connection type.
	Args:
	    connectionType (str): The type of the connection.
	Returns:
	    str: The color associated with the connection type. Defaults to "var(--neutral-70)" if not found.
	"""
	if connectionType in CONNECTIONALLTYPES.keys():
		return CONNECTIONALLTYPES[connectionType]['color']
	else:
		return "#FFCCCC"

def componentType(uuid):
	"""	Checks if the component type associated with the given UUID is valid.
	Args:
	    uuid (str): The UUID of the component.
	Returns:
	    bool: True if the component type is 'cloud', 'standard', 'edge', or 'panel'; otherwise, False.
	"""
	comonentType=session.custom.structure.configs[uuid]['type']
	if comonentType in ['cloud', 'standard', 'edge', 'panel']:
		return True
	return False

	
def getConnectionName(typeid):
	"""	Retrieves the name associated with a connection type ID. If no type ID is provided, 
	returns a dictionary of all connection type names.
	Args:
	    typeid (str or None): The type ID of the connection, or None to get all connection names.
	Returns:
	    str or dict: The name of the connection type, a dictionary of all connection type names if typeid is None, 
	    or 'Does Not Exist' if the type ID is not found.
	"""
	if typeid==None:
		cname={}
		for key in COMPONENTTYPES:
			cname[key]=COMPONENTTYPES[key]['name']
		return cname
	try:
		return COMPONENTTYPES[typeid]['name']
	except:
		return 'Does Not Exist'

def panelClientRule(configs, quantity=0):
	"""	Checks if the given configurations contain both a 'panel' and a 'Client', 
	and if the quantity of 'Client' exceeds a threshold.
	Args:
	    configs (dict): A dictionary of configurations, where keys are UUIDs.
	    quantity (int, optional): The initial quantity of 'Client' to be considered. Default is 0.
	Returns:
	    list: A list containing a boolean indicating if the rule is satisfied and the updated quantity of 'Client'.
	"""
	# Get the list of UUIDs from the configs
	uuids=configs.keys()
	# Extract types from the first two UUIDs
	types=[configs[uuids[0]]['type'],configs[uuids[1]]['type']]
	
	# Check if both 'panel' and 'Client' are present in types
	if 'panel' in types and 'Client' in types:
		# Update quantity based on the type of the configurations
		if configs[uuids[0]]['type']=='Client':
			quantity+=configs[uuids[0]]['config']['quantity']
		elif configs[uuids[1]]['type']=='Client':
			quantity+=configs[uuids[1]]['config']['quantity']
		
		# Check if the quantity of 'Client' exceeds 2
		if quantity>2:
			return [True, quantity]
	return [False, quantity]


def checkDisallow(primaryComponent, checkComponent):
	""" Checks the rules associated with a primary component to determine if a secondary component is allowed, limited, or requires approval.
	Args:
	    primaryComponent (str): The primary component to check rules for.
	    checkComponent (str): The component being checked against the rules of the primary component.
	Returns:
	    tuple: A tuple containing:
	        - allow (bool): Indicates if the checkComponent is allowed.
	        - limited (bool): Indicates if the checkComponent is limited.
	        - approval (bool): Indicates if the checkComponent requires approval.
	        - limitedMessage (str): Message explaining the limitation if applicable.
	"""
	
	allow=True
	limited=False
	approval=False
	limitedMessage=''
	 # Check if the checkComponent is disallowed for the primaryComponent or for all components
	if checkComponent in componentRules[primaryComponent]['disallow'] or checkComponent in componentRules['all']['disallow']:
		allow=False
	
	# Check if the checkComponent is limited for the primaryComponent
	if checkComponent in componentRules[primaryComponent]['limited']:
		limited=True
		# Check if there is a specific limited message for the checkComponent
		if checkComponent in componentRules[primaryComponent]['limitedMessages']:
			limitedMessage=componentRules[primaryComponent]['limitedMessages'][checkComponent]
	
	# Check if the checkComponent requires approval for the primaryComponent
	if checkComponent in componentRules[primaryComponent]['approval']:
		approval=True
	return (allow, limited, approval, limitedMessage)


def connectionCheck(connections=[]):
	"""	Checks the rules for a connection between two components to determine if the connection is allowed, limited, or requires approval.
	Args:
	    connections (list): A list containing two component identifiers to be checked for connection rules.
	Returns:
	    dict: A dictionary containing:
	        - allow (bool): Indicates if the connection is allowed.
	        - limited (bool): Indicates if the connection is limited.
	        - approval (bool): Indicates if the connection requires approval.
	        - message (str): Message explaining the result of the connection check.
	"""
	allow=True
	limited=False
	approval= False
	message=''
	ruleOptions=componentRules.keys()
	# Check the connection rules for the first component in the list
	if connections[0] in ruleOptions:
		result= checkDisallow(connections[0], connections[1])
		allow, limited, approval, limitedMessage =result
	# Check the connection rules for the second component in the list
	elif connections[1] in ruleOptions:
		result= checkDisallow(connections[1], connections[0])
		allow, limited, approval, limitedMessage =result
		
		
    # Generate appropriate message based on the connection rules		
	if not allow:
		message='{} to {} connections NOT allowed'.format(COMPONENTTYPES[connections[0]]['name'], COMPONENTTYPES[connections[1]]['name'])
	elif limited:
		message='{} to {} connections have limited connectivity{}'.format(COMPONENTTYPES[connections[0]]['name'], COMPONENTTYPES[connections[1]]['name'], limitedMessage)
	elif approval:
		message='{} to {} connections require use case approval'.format(COMPONENTTYPES[connections[0]]['name'], COMPONENTTYPES[connections[1]]['name'])

	return {'allow': allow, 'limited': limited, 'approval': approval, 'message': message}
	
ALLCONNECTIONSTYPES=['Gateway Network', 'Device Driver', 'OPC-COM', 'OPC-UA', 'OPC-UA SSL', 'Client', 'MQTT', 'DB', 'Standard', 'MongoDB']

def availibleConnections(connectionTypes=[]):
	"""	Determines available connection options based on provided connection types.
	Args:
	    connectionTypes (list): A list of two connection types to be checked.
	Returns:
	    list: A list of dictionaries, each containing a 'value' and 'label' for available connection options.
	"""

	availiblevalue=[]
	options=[]
	if len(connectionTypes)==2:
		# Define groups of connection types
		availible_GWCs=['standard', 'cloud','edge','panel','fourIR']
		availible_DeviceCs=['standard','edge', 'panel', 'OPCUA']
		availible_OPCUA=['standard','edge', 'panel','cloud', 'Device', 'OPCUA', 'Connector']
		availible_Clients=['standard','cloud', 'panel', 'LoadBalancer']
		availible_MQTTCs=['standard','edge', 'panel','cloud', 'Connector', 'IIOT', 'Device', 'Comms','fourIR']
		availible_DBCs=['standard','edge', 'panel','cloud']
		availible_MongoDBs=['standard', 'cloud']
		
		
		# Check for Gateway Network connections
		if connectionTypes[0] in availible_GWCs and connectionTypes[1] in availible_GWCs:
			availiblevalue.append('Gateway Network')
		
		# Check for MongoDB connections
		if ('MongoDB' in connectionTypes) and (connectionTypes[0] in availible_MongoDBs or connectionTypes[1] in availible_MongoDBs):
			availiblevalue.append('MongoDB')	
		
		# Check for Device Driver connections
		if ('Device' in connectionTypes) and (connectionTypes[0] in availible_DeviceCs or connectionTypes[1] in availible_DeviceCs):
			availiblevalue.append('Device Driver')	
			availiblevalue.append('OPC-COM')	
			
		# Check for OPC-UA connections
		if connectionTypes[0] in availible_OPCUA and connectionTypes[1] in availible_OPCUA:
			availiblevalue.append('OPC-UA')		
#			availiblevalue.append('OPC-UA SSL')
				
		# Check for Client connections
		if ('Client' in connectionTypes or 'LoadBalancer' in connectionTypes) and (connectionTypes[0] in availible_Clients or connectionTypes[1] in availible_Clients):
			availiblevalue.append('Client')			
		
		# Check for MQTT connections
		if connectionTypes[0] in availible_MQTTCs and connectionTypes[1] in availible_MQTTCs:
			availiblevalue.append('MQTT')		
			
		# Check for Database connections
		if 'Database' in connectionTypes and (connectionTypes[0] in availible_DBCs or connectionTypes[1] in availible_DBCs):
			availiblevalue.append('DB')
		
		# Standard connection is always available
		availiblevalue.append('Standard')	

		# Create the options list from available values
		for option in availiblevalue:			
			options.append({
				  "value": option,
				  "label": option
				})	
		
	return options

def round_to_nearest(value, nearest):
	"""	Rounds the given value to the nearest multiple of the specified number.
	Args:
	    value (float or int): The value to be rounded.
	    nearest (int): The nearest multiple to which the value should be rounded.
	Returns:
	    int: The rounded value.
	"""
	# Round down to the nearest multiple
	rounded_value = int(value / nearest) * nearest
	# Calculate the remainder when divided by nearest
	remainder = value % nearest
	# If the remainder is greater than or equal to half of nearest, round up
	if remainder >= nearest / 2:
		rounded_value += nearest
	return rounded_value