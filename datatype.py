def data_type(arg):
	if isinstance(arg, str):
		return len(arg)

	if arg is None:
		return "no value"

	if arg is True or arg is False:
		return arg

	if isinstance(arg, int):
		if arg < 100:
			return "less than 100"
		elif arg > 100:
			return "more than 100"
		else:
			return "equal to 100"
	if isinstance(arg, list):
		if len(arg) > 2:
			return arg[2]
		else:
			None
