components={
  "I7037ee25": {
    "top": 920,
    "left": 960,
    "width": 100,
    "primaryViewPath": "Exchange/ArchitectureBuilder/Components/Server/Main",
    "height": 100
  },
  "If5b72e39": {
    "top": 920,
    "left": 1120,
    "width": 100,
    "primaryViewPath": "Exchange/ArchitectureBuilder/Components/Client/Main",
    "height": 100
  },
  "I2530462a": {
    "top": 760,
    "left": 960,
    "width": 100,
    "primaryViewPath": "Exchange/ArchitectureBuilder/Components/Database/Main",
    "height": 100
  },
  "Ie72e1311": {
    "top": 920,
    "left": 800,
    "width": 100,
    "primaryViewPath": "Exchange/ArchitectureBuilder/Components/Device/Main",
    "height": 100
  }
}
connections={
  "I91077783": {
    "I7037ee25": {
      "x": 0,
      "y": 0.5
    },
    "Ie72e1311": {
      "x": 1,
      "y": 0.5
    }
  },
  "Ib3003436": {
    "I7037ee25": {
      "x": 1,
      "y": 0.5
    },
    "If5b72e39": {
      "x": 0,
      "y": 0.5
    }
  },
  "I4be1bbff": {
    "I7037ee25": {
      "x": 0.5,
      "y": 1
    },
    "I2530462a": {
      "x": 0.5,
      "y": 0
    }
  }
}
containers=[]

canvasSize={
  "height": 2000,
  "width": 2000
}

configs={
  "I91077783": {
    "name": "Connection",
    "type": "Connection",
    "uuid": "I91077783",
    "config": {
      "lineType": "Segmented",
      "connectionType": "Device Driver"
    },
    "desc": ""
  },
  "I7037ee25": {
    "name": "Standard",
    "type": "standard",
    "uuid": "I7037ee25",
    "config": {
      "displayModules": True,
      "licenseKey": "",
      "development": False,
      "licenseKeyRedun": "",
      "version": "8.1.x",
      "modules": {
        "SS": [],
        "TPM": [],
        "IA": [
          {
            "name": "Platform"
          },
          {
            "name": "Alarm Notification"
          },
          {
            "name": "OPC UA"
          },
          {
            "selection": "Unlimited",
            "name": "Perspective"
          },
          {
            "name": "Reporting"
          },
          {
            "name": "SQL Bridge"
          },
          {
            "selection": "Full",
            "name": "Tag Historian"
          }
        ],
        "CL": []
      },
      "redundant": False,
      "supportPlan": "Total",
      "connections": [
        "Ib3003436",
        "I91077783",
        "I4be1bbff"
      ]
    },
    "desc": ""
  },
  "If5b72e39": {
    "name": "Client",
    "type": "Client",
    "uuid": "If5b72e39",
    "config": {
      "image": "ClientLaptopWhite-Left",
      "quantity": 1,
      "connections": [
        "Ib3003436"
      ]
    },
    "desc": ""
  },
  "I2530462a": {
    "name": "Database",
    "type": "Database",
    "uuid": "I2530462a",
    "config": {
      "DBType": "PostgreSQL",
      "connections": [
        "I4be1bbff"
      ]
    },
    "desc": ""
  },
  "Ib3003436": {
    "name": "Connection",
    "type": "Connection",
    "uuid": "Ib3003436",
    "config": {
      "lineType": "Direct",
      "connectionType": "Client"
    },
    "desc": ""
  },
  "Ie72e1311": {
    "name": "Device",
    "type": "Device",
    "uuid": "Ie72e1311",
    "config": {
      "image": "PLCBlue-Left",
      "quantity": 1,
      "tagCount": 0,
      "model": "",
      "PLCType": "",
      "ips": [],
      "connections": [
        "I91077783"
      ]
    },
    "desc": ""
  },
  "I4be1bbff": {
    "name": "Connection",
    "type": "Connection",
    "uuid": "I4be1bbff",
    "config": {
      "lineType": "Segmented",
      "connectionType": "DB"
    },
    "desc": ""
  }
}
def getDefaultTemplate():
	return {
		"canvasSize": canvasSize,
		"components": components,
		"connections": connections,
		"containers": containers,
		"configs": configs}