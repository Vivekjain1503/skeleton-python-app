def process_query(query):
	if ("name" in query.lower()):
		return "Vivek"
	if ("romeo and juliet" in query.lower()):
		return "William Shakespeare is not the answer"
	if ("email" in query.lower()):
		return "vivek-c.jain@db.com"
	return ""