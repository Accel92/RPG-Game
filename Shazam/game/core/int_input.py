def int_input(prompt, error_prompt = ""):
	on = True
	while on == True:
		try:
			number = int(raw_input(prompt))
			on = False
			return number
		except ValueError:
			if len(error_prompt) > 0:
				print error_prompt
