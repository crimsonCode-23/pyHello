classes = []
while True:
	course_ID = input("Enter the Course Code or enter \"done\" to finish:")
	if course_ID.lower() == 'done':
		break
	classes.append(course_ID)
print("You are taking the following classes:")
for course_ID in classes:
	print(course_ID)