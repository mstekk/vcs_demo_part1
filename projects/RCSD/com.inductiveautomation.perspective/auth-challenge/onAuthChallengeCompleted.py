def onAuthChallengeCompleted(session, payload, result):
	tagPath = '[RCSD]Users_Theme/' + session.custom.currentUser
	assignedTheme = system.tag.readBlocking(tagPaths)
	
	session.props.theme = assignedTheme