def process_query(query):
	if ("romeo and juliet" in query.lower()):
		return "William Shakespeare is not the answer"
	if ("what is your name" in query.lower()):
		return "Vivek"
	return ""