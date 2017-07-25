from appJar import gui

#def sexChoice():


def submit(button):
	if button == "Cancel":
		app.stop()
	else:
		if app.getOptionBox("Sex") == "Male":
			return app.yesNoBox("Status","You mad bro?"), app.getOptionBox("Sex")
		if app.getOptionBox("Sex") == "Female":
			return app.yesNoBox("Status","You mad brah?"), app.getOptionBox("Sex")
		if app.getOptionBox("Sex") == "Other":
			return app.yesNoBox("Status","You mad?"),app.getOptionBox("Sex")
		else:
			app.infoBox("Input needed","Please make a choice from the list provided")
			app.go()

def get(button):
	print(app.getOptionBox("Sex"))
			
def yesNoMad(button):
	status,S = submit(button)
	if status == True:
		app.infoBox("mad","Deal with it!!")
	elif S == "Male":
		app.infoBox("notMad","Cool story bro...")
	elif S == "Female":
		app.infoBox("notMad","Cool story brah...")
	elif S == "Other":
		app.infoBox("notMad","Cool story...")

def checkstop():
	return app.yesNoBox("Confirm Exit","Are you sure you want to exit the app?")
	
app = gui("Welcome box","400x200")
app.setBg("grey")
app.addLabel("welcome","Please choose from the folowing list")

# sex choice box
app.addLabelOptionBox("Sex",["- Choose -","Male","Female","Other"])

# sex gettting info
#app.getOptionbox("Sex")

# Buttons
app.addButtons(["Submit","Cancel"],yesNoMad)

# checkstop
app.setStopFunction(checkstop)


app.go()