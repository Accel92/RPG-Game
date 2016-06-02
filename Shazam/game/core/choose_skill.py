def choose_skill(number_of_skills):
	heyhey = "Joe hey"
	on = True
	while on == True:
		try:
			skill_number = int(raw_input())
			on = False
		except ValueError:
			print "\nNeed a number, not a phrase\n"
			continue
	if skill_number <= number_of_skills:
		return skill_number
	else:
		print "This skill is not unclocked yet"
		print "(or it doesn't exist).\nTry again"
