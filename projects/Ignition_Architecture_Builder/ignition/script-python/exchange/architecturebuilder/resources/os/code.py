# Dropdown menus for operating system selection

selections = {
	"Windows": [
		"Windows 7 x64",
		"Windows 8 x64",
		"Windows 8.1 x64",
		"Windows 10 Pro x64",
		"Windows 10 LTSC x64",
		"Windows 10 IoT Enterprise x64",
		"Windows 10 IoT Enterprise LTSC x64",
		"Windows 11 x64",
		"Windows Server 2008 x64",
		"Windows Server 2008 R2 x64",
		"Windows Server 2012 x64",
		"Windows Server 2012 R2 x64",
		"Windows Server 2016 x64",
		"Windows Server 2019 x64",
		"Windows Server 2022 x64",
		"Windows Server 2025 x64"
	],
	"Linux": [
		"Ubuntu 14.04 LTS x64",		# EOL April 2026
		"Ubuntu 16.04 LTS x64",		# EOL April 2028
		"Ubuntu 18.04 LTS x64",		# EOL April 2030
		"Ubuntu 20.04 LTS x64",		# EOL April 2032
		"Ubuntu 22.04 LTS x64",		# EOL April 2034
		"Ubuntu 24.04 LTS x64",		# EOL April 2036
		"Ubuntu 24.10 x64",			# EOL July 2025
		"RHEL 7 ELS x64",			# EOL June 30, 2028
		"RHEL 8 x64",				# EOL May 31, 2032
		"RHEL 9 x64",				# EOL May 31, 2035
		"Other: [ARMHF]",
		"Other: [ARM64]", 
		"Other: [x86-64]
	],
	"macOS": [
		"macOS 13 Ventura x64",
		"macOS 14 Sonoma x64",
		"macOS 15 Sequoia x64"
	]
}


# Function to return dropdown-compatible list of operating system families
def getFamilies():
	returnList = []
	for key in selections.keys():
		returnList.append({"value": key, "label": key})
	return returnList


# Function to return dropdown-compatible list of versions of specified operating system family
#    'family' should be "Windows", "Linux", or "macOS"
def getVersions(family):
	returnList = []
	for i in range(len(selections[family])):
		returnList.append({"value": selections[family][i], "label": selections[family][i]})
	return returnList