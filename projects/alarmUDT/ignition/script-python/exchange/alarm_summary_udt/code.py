def getAllAlarms():

		'''
		Description:
			Query all alarms using system function 'system.alarm.queryStatus' and store in
			a global vaiable dictionary, 'alarmSummaryGlobal'. This function calls 'system.alarm.queryStatus'
			only one time vs calling it several times per instance, which can cause higher than normal CPU usage 
			when several instances are used. 
			
			This function is typically called from a gateway event, like a timer event. 
			The frequency of this event can vary depending on the specific project needs, but has been
			tested using a one second delay with very good results.
			
		Arguments:
			None 
		
		History:
			No.		Date		  Author				Comment
			1.0		2022-10-20	  James Landwerlen	    Initial
			1.1	    2022-10-29    James Landwerlen	    Added shelving
		'''
		
		global alarmSummaryGlobal
		alarmSummary = {}
		
		state = ["ActiveUnacked", "ActiveAcked", "ClearUnacked"]
		#Get an Alarm Query Result for all alarms, including alarms that are shelved
		alarms = system.alarm.queryStatus(state=state, includeShelved=True)
		
		for alarm in alarms:
			
			#iterate through all alarms and place into the global dictionary 'alarmSummaryGlobal' to be called later
			#  on by each UDT instance
			source = alarm.source
			#Build a typical tag path [MyTagProvider]MyTag
			tagPath = '[' + alarm.source.getPathComponent('prov') +']' + alarm.source.getPathComponent('tag')
			name = alarm.name
			state = alarm.state.name()
			priority = alarm.priority.name()
			
			#if the alarm is shelved, flag as shelved and set state/priority to Shelved so the counts
			#  will be ignored later on
			if alarm.isShelved():
				state = priority = 'Shelved'
			alarmSummary[source] = {'tagPath':tagPath, 'name':name, 'state':state, 'priority':priority, 'shelved':alarm.isShelved()}
		
		alarmSummaryGlobal = alarmSummary
		
		
		
		
def getUDTInstances(tp, alarmPath):

	'''
	Description:
		This function is called from each UDT instance using `runScript` in the element `summary` and
		returns a json with alarm information specific to the path.
		
		The argument `tp` is populated automatically in each UDT instance using a value change script
		in the element `TagProvider`.
		
	Arguments:
		tp = Tag Provider
		alarmPath = Path to the UDT instance parent folder. Root will be blank.
	
	History:
		No.		Date		  Author				Comment
		1.0		2022-10-20	  James Landwerlen	    Initial
		1.1	    2022-10-29    James Landwerlen	    Added shelving
	'''
	global alarmSummaryGlobal
	
	alarmPath = '[' + tp + ']' + alarmPath
	alarmPriorities = {'Shelved':-1, 'Diagnostic':0, 'Low':1, 'Medium':2, 'High':3, 'Critical':4}
	statePriorities = {'Shelved':-1, 'ClearAcked':0, 'ClearUnacked':1, 'ActiveAcked':2, 'ActiveUnacked':3}
	#These styles were not part of the resource, but any style can be added and will be selected based on the state and priority
	styleStates = {'DiagnosticActiveUnacked':'exchange/navigation/diagnostic-unacked', 'DiagnosticActiveAcked':'exchange/navigation/diagnostic-acked', 
				   'LowActiveUnacked':'exchange/navigation/low-unacked', 'LowActiveAcked':'exchange/navigation/low-acked',
				   'MediumActiveUnacked':'exchange/navigation/medium-unacked', 'MediumActiveAcked':'exchange/navigation/medium-acked',
				   'HighActiveUnacked':'exchange/navigation/high-unacked', 'HighActiveAcked':'exchange/navigation/high-acked',
				   'CriticalActiveUnacked':'exchange/navigation/critical-unacked', 'CriticalActiveAcked':'exchange/navigation/critical-acked',}
	priorityCounts = {'Diagnostic': 0, 'Low': 0, 'Medium': 0, 'High': 0, 'Critical': 0, 'Shelved':0}
	priority = None
	state = None
	styleClass = None
	hasUnackAlarm = False
	resultDict = {'counts': priorityCounts, 'priority':	'', 'state': '', 'class': '', 'hasUnackAlarm': ''}	
	alarmPrioritiesList = []
	
	for alarm in alarmSummaryGlobal:
		#If alarm found within the summary then get counts and priorities
		#  The tagPath must match exactly starting from the left, this prevents partial matches
		tagPath = alarmSummaryGlobal[alarm]['tagPath']
		if tagPath.startswith(alarmPath, 0, len(alarmPath)):
					
			#Create a list of alarm priorities, so we can later find the highest priority as well as state for that priority
			alarmPriority = alarmSummaryGlobal[alarm]['priority']
			alarmState = alarmSummaryGlobal[alarm]['state']
			alarmPrioritiesList.append([alarmPriorities[alarmPriority], statePriorities[alarmState]])
			
			shelved = alarmSummaryGlobal[alarm]['shelved']
			if not shelved and (alarmState == 'ClearedUnacked' or alarmState == 'ActiveUnacked'):
				hasUnackAlarm = True
			
			priorityCounts[alarmPriority] += 1
	
	if alarmPrioritiesList:		
		alarmListMax = max(alarmPrioritiesList, key=lambda item: (item[0], item[1]))
		priority = alarmPriorities.keys()[alarmPriorities.values().index(alarmListMax[0])]
		state = statePriorities.keys()[statePriorities.values().index(alarmListMax[1])]
		styleClass = styleStates.get(str(priority) + str(state))
	
	#Take the results and place in a dictionary		
	resultDict = {
					'counts': priorityCounts, #A dicionary holding counts for each priority
					'priority':	priority, #The highest priority
					'state': state, #The most important state
					'class': styleClass, #The style class for indication purposes
					'hasUnackAlarm': hasUnackAlarm #At least one unacknowledged alarm exists
					}	
	
	json = system.util.jsonEncode(resultDict)	
	return json