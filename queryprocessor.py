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
		nums = query.split(":")[2].strip()
		nums = nums.split(",")
		print(nums)
		a = 0
		for num in nums:
			if int(num) > a :
				a = int(num)
		return str(a)

	if ("multiplied" in query.lower()):
		num1 = int(query.split()[-1])
		num2 = int(query.split()[-4])
		# print(num1,num2)
		return str(num1*num2)
	if ("both a square and a cube"):
		nums = query.split(":")[2].strip()
		nums = nums.split(",")
		print(nums)
		a = 0
		for num in nums:
			a = int(num)
			x = a ** (1 / 3)
			x = int(round(x))
			y = a ** (1 / 2)
			y = int(round(y))
			ans = True
			if x**3 == a and y**2 == a:
				return str(a)
	return ""

# print(process_query("what is 20 plus 5"))