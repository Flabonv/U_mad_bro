from appJar import gui

def submit(button):
	if button == "Cancel":
		Umad.stop()
	else:
		if Umad.getOptionBox("Gender") == "Male":
			return Umad.yesNoBox("Status","U mad bro?"), Umad.getOptionBox("Gender")
		if Umad.getOptionBox("Gender") == "Female":
			return Umad.yesNoBox("Status","U mad brah?"), Umad.getOptionBox("Gender")
		if Umad.getOptionBox("Gender") == "Other":
			return Umad.yesNoBox("Status","U mad?"),Umad.getOptionBox("Gender")
		else:
			Umad.infoBox("Input needed","Please make a choice from the list provided")
			Umad.go()

def get(button):
	print(Umad.getOptionBox("Gender"))
			
def yesNoMad(button):
	status,S = submit(button)
	if status == True:
		Umad.infoBox("mad","Deal with it!!")
	elif S == "Male":
		Umad.infoBox("notMad","Cool story bro...")
	elif S == "Female":
		Umad.infoBox("notMad","Cool story brah...")
	elif S == "Other":
		Umad.infoBox("notMad","Cool story...")

def checkstop():
	return Umad.yesNoBox("Confirm Exit","Are you sure you want to exit the Umad?")
	
Umad = gui("Welcome box","400x200")
Umad.setBg("grey")
Umad.addLabel("welcome","Please choose from the folowing list")

# Gender choice box
Umad.addLabelOptionBox("Gender",["- Choose -","Male","Female","Other"])

# Buttons
Umad.addButtons(["Submit","Cancel"],yesNoMad)

# checkstop
Umad.setStopFunction(checkstop)


Umad.go()
