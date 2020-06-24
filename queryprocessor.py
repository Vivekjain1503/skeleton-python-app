def process_query(query):
	if ("name" in query.lower()):
		return "Vivek"
	if ("romeo and juliet" in query.lower()):
		return "William Shakespeare is not the answer"
	if ("plus" in query.lower()):
		num1 = int(query.split()[3])
		num2 = int(query.split()[5])
		# print(num1,num2)
		return str(num1+num2)
	if ("largest" in query.lower()):
		nums = query.split(":")[1].trim()
		nums = nums.split(",")
		a = 0
		for num in nums:
			if int(num) > a :
				a = int(num)
		return str(a)
	return ""

# print(process_query("what is 20 plus 5"))