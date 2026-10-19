import uuid

def newUuid():
	return 'I{}'.format(str(uuid.uuid4())[:8])
