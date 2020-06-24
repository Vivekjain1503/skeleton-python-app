def process_query(query):
	if ("name" in query.lower()):
		return "Vivek"
	if ("romeo and juliet" in query.lower()):
		return "William Shakespeare is not the answer"
	if ("plus" in query.lower()):
		num1 = int(query.split()[2])
		num2 = int(query.split()[4])
		return str(num1+num2)
	return ""