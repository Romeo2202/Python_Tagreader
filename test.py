from turtle import update
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
from Phidget22.Devices.DigitalOutput import *
import time
import requests
# Tagdata function
def Tagdata (self, tag, Cardtag):
	Cardtag = str(tag)
	print(str(Cardtag))
# Post request to api
	requests.post(f'http://192.168.1.11:10000/Updatepoints?id={Cardtag}')

def main():
	tagreader1 = RFID()
	digitalOutput0 = DigitalOutput()
# Send output to Tagreader function
	tagreader1.setOnTagHandler(Tagdata)

	tagreader1.openWaitForAttachment(5000)
	digitalOutput0.openWaitForAttachment(5000)

	digitalOutput0.setDutyCycle(1)
# Stop program when pressing enter
	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass
# Close connection
	tagreader1.close()
	digitalOutput0.close()
main()