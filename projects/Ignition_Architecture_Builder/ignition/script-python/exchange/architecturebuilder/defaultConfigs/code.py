componentConfigs={
	"standard":{ #Standard Gateway
		"connections": [],
		"development": False,
		"displayModules": False,
		"licenseKey": "",
		"licenseKeyRedun": "",
		"modules": {
		"CL": [],
		"IA": [
		  {
		    "name": "Platform"
		  },
		  {
		    "name": "OPC UA"
		  },
		  {
		    "name": "Perspective",
		    "selection": "Unlimited"
		  },
		  {
		    "name": "Tag Historian",
		    "selection": "Full"
		  },
		  {
		    "name": "Alarm Notification"
		  },
		  {
		    "name": "SQL Bridge"
		  }
		],
		"SS": [],
		"TPM": []
		},
		"redundant": False,
		"supportPlan": "Total",
		"trial": False,
		"version": "8.1.x"
		},
	"edge":{ #Edge IIOT Gateway
	  "connections": [],
	  "development": False,
	  "displayModules": False,
	  "licenseKey": "",
	  "licenseKeyRedun": "",
	  "modules": {
	    "CL": [
	      {
	        "name": "MQTT Transmission"
	      }
	    ],
	    "IA": [
	      {
	        "name": "Platform"
	      },
	      {
	        "name": "EAM"
	      },
	      {
	        "name": "Web Development"
	      },
	      {
	        "name": "Alarm Notification",
	        "selection": "1-Way Email"
	      },
	      {
	        "name": "Tag Historian",
	        "selection": "Edge"
	      },
	      {
	        "name": "OPC UA"
	      }
	    ],
	    "SS": [],
	    "TPM": []
	  },
	  "redundant": False,
	  "supportPlan": "Total",
	  "trial": False,
	  "version": "8.1.x"
	},
	"panel": { #Edge Panel Gateway
	  "connections": [],
	  "development": False,
	  "displayModules": False,
	  "licenseKey": "",
	  "licenseKeyRedun": "",
	  "modules": {
	    "CL": [
	      {
	        "name": "MQTT Transmission"
	      }
	    ],
	    "IA": [
	      {
	        "name": "Platform"
	      },
	      {
	        "name": "EAM"
	      },
	      {
	        "name": "Web Development"
	      },
	      {
	        "name": "Alarm Notification",
	        "selection": "1-Way Email"
	      },
	      {
	        "name": "Tag Historian",
	        "selection": "Edge"
	      },
	      {
	        "name": "OPC UA"
	      },
	      {
	        "name": "Perspective",
	        "selection": "2 Sessions"
	      }
	    ],
	    "SS": [],
	    "TPM": []
	  },
	  "redundant": False,
	  "supportPlan": "Total",
	  "trial": False,
	  "version": "8.1.x"
	},
	"cloud":{
	  "connections": [],
	  "development": False,
	  "displayModules": False,
	  "licenseKey": "",
	  "licenseKeyRedun": "",
	  "modules": {
	    "CL": [
	      {
	        "name": "MQTT Engine"
	      },
	      {
	        "name": "MQTT Distributor",
	        "selection": "Distributor (50 clients)"
	      },
	      {
	        "name": "MQTT Transmission"
	      }
	    ],
	    "IA": [
	      {
	        "name": "Platform"
	      },
	      {
	        "name": "Alarm Notification"
	      },
	      {
	        "name": "Twilio Notification"
	      },
	      {
	        "name": "EAM"
	      },
	      {
	        "name": "MongoDB"
	      },
	      {
	        "name": "Perspective",
	        "selection": "Unlimited"
	      },
	      {
	        "name": "Reporting"
	      },
	      {
	        "name": "SQL Bridge"
	      },
	      {
	        "name": "Tag Historian",
	        "selection": "Full"
	      },
	      {
	        "name": "Web Development"
	      },
	      {
	        "name": "OPC UA"
	      }
	    ],
	    "SS": [],
	    "TPM": []
	  },
	  "redundant": False,
	  "supportPlan": "Total",
	  "trial": False,
	  "version": "8.1.x"
	},
	"Database":{
	  "DBType": "AzureSQL"
	},
	"Device":{
	  "PLCType": "",
	  "image": "PLCBlue-Left",
	  "ips": [],
	  "model": "",
	  "quantity": 1,
	  "tagCount": 0
	},
	"Client":{
	  "image": "ClientKeyboardBlue-Left",
	  "quantity": 1
	},
	"IIOT":{
	  "image": "MQTT-Server"
	},
	"Connector":{
	  "image": "AWS"
	},
	"Comms":{
	  "image": "Cell-Tower"
	},
	"LoadBalancer":{
	},
	"MongoDB":{
	},
	"OPCUA":{
	},
	"Usersource":{
	},
	"ReverseProxy":{
	},
	"Firewall":{
	},
	"server":{
	},
	"Custom":{
	  "base64": None
	},
	"fourIR":{
	  "image": "FactoryStack"
	},
	"Opto22":{
	  "image": "Opto22-Epic",
	  "quantity": 1
	},
	"Note":{
	  "fontSize": 12
	},
	"Connection":{
	  "adjust": 0,
	  "lineType": "Segmented",
	  "connectionType": "Device Driver"
	},
	"Container":{
	  "quantity": 1,
	  "backColor": "#D5D5D5",
	  "vendor": False,
	  "transparency": 255,
	  "location": {
	    "lng": None,
	    "lat": None
	  },
	  "labelColor": "#000000"
	}
}

def getComponentKeys(component):
	return componentConfigs[component].keys()

def getComponentDefaults(component):
	return componentConfigs[component]
	
def getComponentDefaultKeyValue(component,key):
	return componentConfigs[component][key]
	
def checkConfigs(configs):
	logger = system.util.getLogger("loadCheck")
	for uuid in configs:
		try:
			componentType=configs[uuid]['type']
			componentName=configs[uuid]['name']
			myComponentKeys=configs[uuid]['config'].keys()
			defaultComponentKeys=getComponentKeys(componentType)
			missing_keys = set(defaultComponentKeys) - set(myComponentKeys)
			for missingKey in missing_keys:
				configs[uuid]['config'][missingKey]=getComponentDefaultKeyValue(componentType,missingKey)
		except:
			logger.warn("{} Component key error".format(componentType))
	return configs
		