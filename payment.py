def payment(courses):
	total = 0 
	print("*"*30)
	print("Your courses with fee are these ")
	for course in courses:
	 print(f"Course Name : {course} ||  Price of course : {15000}")
	 total+=15000
	return total
selected_courses = ["Discrete","PF","Maths1","English","ICT"]
pay = payment(selected_courses)

print(f"Your total dues are {pay}")
while True:
	user = int(input(f"Pay {pay} Rs here: "))
	if user == pay:
		print("fee has paid")
		break
	else:
		print("Please pay whole fee")
print("*"*30)