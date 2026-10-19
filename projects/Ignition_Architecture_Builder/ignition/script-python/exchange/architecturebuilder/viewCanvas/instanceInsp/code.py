def instanceCoords(instance):
	"""	Extracts coordinates (top, bottom, left, right) and UUID from the instance object.
	Args:
	    instance (dict): Dictionary containing properties of an instance, including positional data.
	Returns:
	    list: A list containing top, bottom, left, right coordinates, and UUID.
	"""
	top=int(instance['top'].replace('px',''))
	height=int(instance['height'].replace('px',''))
	left=int(instance['left'].replace('px',''))
	width=int(instance['width'].replace('px',''))	
	
	# Calculate bottom coordinate
	if str(instance['bottom']).lower()=='auto':
		bottom=top+height
	else:
		bottom=int(instance['top'].replace('px',''))
	
	# Calculate right coordinate
	if instance['right']=='auto':
		right=left+width
	else:
		right=int(instance['right'].replace('px',''))
	
	uuid=instance['viewParams']['params']['uuid']
	
	return [top, bottom, left, right, uuid]

def instanceInContainer(instanceCoords,containerCoords):
	"""	Checks if an instance (represented by its coordinates) is fully contained within a container.
	Args:
	    instanceCoords (list): List containing [top, bottom, left, right, uuid] of the instance.
	    containerCoords (list): List containing [top, bottom, left, right, uuid] of the container.
	Returns:
	    bool: True if the instance is fully contained within the container, False otherwise.
	"""	
	top1, bottom1, left1, right1, uuid = instanceCoords
	top2, bottom2, left2, right2, uuid = containerCoords
	
	if top1 >= top2 and bottom1 <= bottom2 and left1 >= left2 and right1 <= right2:
	    return True
	else:
	    return False
        
def getInstanceIndexPerUuid(instances,uuid):
	"""	Retrieves the index of an instance in a list based on its UUID.
	Args:
	    instances (list): List of dictionaries, where each dictionary represents an instance.
	    uuid (str): UUID of the instance to find.
	Returns:
	    int or None: Index of the instance in the list if found, None if not found.
	"""
	for x in range(len(instances)):
		if instances[x]['viewParams']['params']['uuid']==uuid:
			return x
	return None
	