def process_query(query):
	if ("romeo and juliet" in query.lower()):
		return "William Shakespeare is not the answer"
	if ("name" in query.lower()):
		return "Vivek"
	if ("email" in query.lower()):
		return "vivek-c.jain@db.com"
	return ""