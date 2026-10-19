ignition = [
	{
		'load': {
			'devices': 2,
			'tags': 500,
			'clients': 2
		},
		'resources': {
			'cpu': {
				'cores': 2,
				'arm': True
			},
			'ram': 1
		}
	},
	{
		'load': {
			'devices': 10,
			'tags': 2500,
			'clients': 5
		},
		'resources': {
			'cpu': {
				'cores': 2,
				'arm': False
			},
			'ram': 2
		}
	},
	{
		'load': {
			'devices': 10,
			'tags': 5000,
			'clients': 10
		},
		'resources': {
			'cpu': {
				'cores': 2,
				'arm': False
			},
			'ram': 4
		}
	},
	{
		'load': {
			'devices': 25,
			'tags': 10000,
			'clients': 20
		},
		'resources': {
			'cpu': {
				'cores': 4,
				'arm': False
			},
			'ram': 4
		}
	},
	{
		'load': {
			'devices': 50,
			'tags': 25000,
			'clients': 25
		},
		'resources': {
			'cpu': {
				'cores': 4,
				'arm': False
			},
			'ram': 8
		}
	},
	{
		'load': {
			'devices': 100,
			'tags': 50000,
			'clients': 50
		},
		'resources': {
			'cpu': {
				'cores': 4,
				'arm': False
			},
			'ram': 16
		}
	},
	{
		'load': {
			'devices': 100,
			'tags': 75000,
			'clients': 50
		},
		'resources': {
			'cpu': {
				'cores': 8,
				'arm': False
			},
			'ram': 8
		}
	},
	{
		'load': {
			'devices': 100,
			'tags': 100000,
			'clients': 75
		},
		'resources': {
			'cpu': {
				'cores': 8,
				'arm': False
			},
			'ram': 16
		}
	},
	{
		'load': {
			'devices': 100,
			'tags': 150000,
			'clients': 100
		},
		'resources': {
			'cpu': {
				'cores': 16,
				'arm': False
			},
			'ram': 32
		}
	},
]


def getIndex(instanceLoad):
	for i in range(len(ignition)):
		if instanceLoad['devices'] <= ignition[i]['load']['devices'] and \
			instanceLoad['tags'] <= ignition[i]['load']['tags'] and \
			instanceLoad['clients'] <= ignition[i]['load']['clients']:
			return i


def getRecommendedResources(instanceLoad):
	history = instanceLoad['histTags'] + instanceLoad['histSQL']
	hours = instanceLoad['histHrs']
	index = getIndex(instanceLoad)

	# Return units is GB (Gigabytes)
	# 10 is the default disk size displayed on the Downloads page
	# Assume 100 bytes for each record stored to disk (Store & Forward cache)
	disk = {'disk': 10.0 + (((100.0 * 3600) / (1024 * 1024 * 1024)) * history * hours)}
	if index is None:
		resources = {'cpu': "Server Load Exceeds Server Sizing Guide",
			'ram': "Server Load Exceeds Server Sizing Guide"}
	else:
		resources = ignition[index]['resources']
	disk.update(resources)
	return disk