import subprocess
import pyautogui
import time
import json
import pandas as pd
from datetime import datetime
pyautogui.FAILSAFE = False
def sign_in(meeting_id, pswd):
	def keypress(pyautogui, code):
		pyautogui.keyDown(code)
		pyautogui.keyUp(code)


		#Open Zoom:
	print("Opening Zoom")
	pyautogui.keyDown("winleft")
	pyautogui.keyUp("winleft")
	time.sleep(3)
	pyautogui.write("zoom")
	pyautogui.keyDown("\n")
	pyautogui.keyUp("\n")
	time.sleep(15)
	print("Done")

	print("clicking join")
	time.sleep(2)
	while pyautogui.locateOnScreen('joinbutton.png'):
		time.sleep(2)
		x = pyautogui.locateCenterOnScreen('joinbutton.png')
		time.sleep(3)
		print(x)
		pyautogui.click(x)
		break
	else: print(".")
	print("done")

	time.sleep(5)

	print("entering meeting id")
	time.sleep(3)
	while pyautogui.locateOnScreen('meetingid.png'):
		time.sleep(3)
		y = pyautogui.locateOnScreen('meetingid.png')
		print(y)
		pyautogui.click(y)
		break
	else: print(".")



	pyautogui.write(meeting_id)


	time.sleep(3)

	print("joining")
	while pyautogui.locateOnScreen('joinbtn.png'):
		time.sleep(3)
		q = pyautogui.locateOnScreen('joinbtn.png')
		print(q)
		pyautogui.click(q)
		break
	else: print(".")
	time.sleep(3)

	#close invalid

	if pyautogui.locateOnScreen('sign.png'):
		pyautogui.hotkey('altleft', 'f4')
		print("CLOSING INVALID ID WINDOW")
	else: print("....")
	print("....")

	print("entering password")
	time.sleep(4)
	pyautogui.write(pswd)


	print("clicking joinmeeting")
	r = pyautogui.locateOnScreen('joinmeeting1.png')
	print(r)
	pyautogui.click(r)
	print(".")
	time.sleep(5)
	print("meeting_joined")
print("I'm Looking for the timetable")

df = pd.read_csv('enter.csv')

while True:
	#checking timetable
	now = datetime.now().strftime("%d/%m/%Y %H:%M")
	if now in str(df['timings']):
		row = df.loc[df['timings'] == now]
		m_id = str(row.iloc[0,1])
		m_pswd = str(row.iloc[0,2])

		sign_in(m_id, m_pswd)
		time.sleep(5)
		print("signed in")
	elif pyautogui.locateOnScreen('sign.png'):
		pyautogui.hotkey('altleft', 'f4')