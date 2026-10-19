def insertAuditEvent(enabled, action, actionTarget, originatingSystem=[], actionValue=None, auditProfile='AB_AuditProfile'):
	#system.util.audit([action], [actionTarget], [actionValue], [auditProfile], [actor], [actorHost], [originatingSystem], [eventTimestamp], [originatingContext], [statusCode])
	if enabled:
		if actionValue is not None:
			system.util.audit(action=action, actionTarget=actionTarget, actionValue=actionValue, originatingSystem=originatingSystem, auditProfile=auditProfile)
		else:
			system.util.audit(action=action, actionTarget=actionTarget, originatingSystem=originatingSystem, auditProfile=auditProfile)
		return True