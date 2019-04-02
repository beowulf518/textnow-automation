import time
import pyautogui
import speech_recognition as sr
import os
import subprocess
from queryAPI import bing, google, ibm

''' You'll need to update based on the coordinates of your setup '''
FIREFOX_ICON_COORDS = (25, 	 125) # Location of the Firefox icon on the side toolbar (to left click)
PRIVATE_COORDS		= (205,  143) # Location of "Open a new Private Window"
PRIVATE_BROWSER 	= (460, 500) # A place where the background of the Private Window will be
#PRIVATE_COLOR		= '#25003E'  # The color of the background of the Private Window
PRIVATE_COLOR		= '#323639'  # The color of the background of the Private Window
SEARCH_COORDS 		= (755, 78) # Location of the Firefox Search box
REFRESH_COORDS      = (150, 76) # Refresh button
GOOGLE_LOCATION     = (472, 159) # Location of the TEXTNOW Icon after navigating to www.textnow.com/signup?ref=NonSale-GatewaySlot3
#GOOGLE_COLOR 		= '#642BDD'  # Color of the TEXTNOW Icon
GOOGLE_COLOR 		= '#652CDE'  # Color of the TEXTNOW Icon
CAPTCHA_COORDS		= (867, 420) # Coordinates of the empty CAPTCHA checkbox
TEMP_CHECK_COORDS	= (337, 45) # Temp location
CHECK_COORDS 		= (857, 420) # Location where the green checkmark will be
CHECK_COLOR 		= '#009E55'  # Color of the green checkmark
AUDIO_COORDS		= (966, 691) # Location of the Audio button
DOWNLOAD_COORDS		= (1030, 474) # Location of the Download button
AUDIO_PLAY_BAR		= (925, 572) # Location of Audio Player
PLAY_BAR_COLOR		= '#F1F3F4'
DOWNLOAD_AUDIO_ITME = (963, 678) # Location of Download MENU Item
SAVE_BUTTON 		= (1406, 805) # Save the auido file.
CLOSE_TAB			= (536, 43) # Close the Audio play tab
FINAL_COORDS  		= (974, 416) # Text entry box
VERIFY_COORDS 		= (1118, 541) # Verify button
EMAIL_INPUT			= (862, 271) # Location of email input
PASSWORD_INPUT		= (862, 331) # Location of password input
SIGNUP_BUTTON		= (910, 516)
NOCAPTCHA_SIGNUP_BUTTON = (915,413)
CLOSE_LOCATION		= (14, 14)


DOWNLOAD_LOCATION = "../../../../Downloads/"
''' END SETUP '''

noCaptcha = False
r = sr.Recognizer()

def runCommand(command):
	''' Run a command and get back its output '''
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	return proc.communicate()[0].split()[0]

def waitFor(coords, color):
	''' Wait for a coordinate to become a certain color '''
	pyautogui.moveTo(coords)
	numWaitedFor = 0
	print (runCommand("eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop \"1x1+$X+$Y\" txt:- | grep -om1 '#\w\+'").decode("utf-8"))
	
	while color != runCommand("eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop \"1x1+$X+$Y\" txt:- | grep -om1 '#\w\+'").decode("utf-8"):
		time.sleep(.1)
		numWaitedFor += 1
		if numWaitedFor > 25:
			return -1
	return 0

def downloadCaptcha():
	''' Navigate to demo site, input user info, and download a captcha. '''
	print("Opening Firefox")
	pyautogui.moveTo(FIREFOX_ICON_COORDS)
	pyautogui.rightClick()
	time.sleep(.3)
	pyautogui.moveTo(PRIVATE_COORDS)
	pyautogui.click()
	time.sleep(2)
	if waitFor(PRIVATE_BROWSER, PRIVATE_COLOR) == -1: # Wait for browser to load
		return -1
	
	print("Visiting Demo Site")
	pyautogui.moveTo(SEARCH_COORDS)
	pyautogui.click()
	pyautogui.typewrite('textnow.com')
	pyautogui.press('enter')
	time.sleep(7)
	pyautogui.moveTo(SEARCH_COORDS)
	pyautogui.click()
	time.sleep(2)
	pyautogui.click()
	pyautogui.typewrite('/signup?ref=NonSale-GatewaySlot3')
	pyautogui.press('enter')
	time.sleep(10)

	# pyautogui.moveTo(REFRESH_COORDS)
	# pyautogui.click()
	# time.sleep(5)
	# Check if the page is loaded...
	pyautogui.moveTo(GOOGLE_LOCATION)
	if waitFor(GOOGLE_LOCATION, GOOGLE_COLOR) == -1: # Waiting for site to load
		return -1

	print("Downloading Captcha")
	pyautogui.moveTo(CAPTCHA_COORDS)
	pyautogui.click()
	time.sleep(3)
	pyautogui.moveTo(CHECK_COORDS)
	if waitFor(CHECK_COORDS, CHECK_COLOR) == -1: # Waiting for site to load
		print("An error occured.")
	else:
		print ("Already completed captcha.")
		return 2

	global noCaptcha

	if waitFor(CHECK_COORDS, '#FFFFFF') == -1: # Waiting for site to load
		print("An error occured.")
	else:
		print ("Already completed captcha.")
		noCaptcha = True
		return 2
		
	# if CHECK_COLOR in runCommand("eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop '1x1+$X+$Y' txt:- | grep -om1 '#\w\+'").decode("utf-8"):
	# 	print ("Already completed captcha.")
	# 	return 2

	pyautogui.moveTo(AUDIO_COORDS)
	pyautogui.click()
	time.sleep(2.5)
	
	pyautogui.moveTo(DOWNLOAD_COORDS)
	pyautogui.click()
	time.sleep(11)
	pyautogui.moveTo(AUDIO_PLAY_BAR)
	if waitFor(AUDIO_PLAY_BAR, PLAY_BAR_COLOR) == -1: # Waiting for site to load
		return -1
	pyautogui.rightClick()
	time.sleep(.3)
	pyautogui.moveTo(DOWNLOAD_AUDIO_ITME)
	pyautogui.click()
	time.sleep(1)
	pyautogui.moveTo(SAVE_BUTTON)
	pyautogui.click()
	time.sleep(2)
	pyautogui.moveTo(CLOSE_TAB)
	pyautogui.click()

	return 0

def checkCaptcha():
	''' Check if we've completed the captcha successfully. '''
	print (CHECK_COORDS)
	print ("check verify result")
	pyautogui.moveTo(CHECK_COORDS)
	if waitFor(CHECK_COORDS, CHECK_COLOR) == -1: # Waiting for site to load
		print("An error occured.")
		output = 0
	else:
		print ("Successfully completed captcha.")
		output = 1
	# print (runCommand("eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop '1x1+$X+$Y' txt:- | grep -om1 '#\w\+'"))
	# if CHECK_COLOR in runCommand("eval $(xdotool getmouselocation --shell); xwd -root -silent | convert xwd:- -depth 8 -crop '1x1+$X+$Y' txt:- | grep -om1 '#\w\+'").decode("utf-8"):
	# 	print ("Successfully completed captcha.")
	# 	output = 1
	# else:
	# 	print("An error occured.")
	# 	output = 0

	# pyautogui.moveTo(CLOSE_LOCATION)
	# pyautogui.click()
	return output

def runCap():
	try:
		print("Removing old files...")
		os.system('rm ./audio.wav 2>/dev/null') # These files may be left over from previous runs, and should be removed just in case.
		os.system('rm ' + DOWNLOAD_LOCATION + 'audio.mp3 2>/dev/null')
		# First, download the file
		downloadResult = downloadCaptcha()
		if downloadResult == 2:
			# pyautogui.moveTo(CLOSE_LOCATION)
			# pyautogui.click()
			return 2
		elif downloadResult == -1:
			pyautogui.moveTo(CLOSE_LOCATION)
			pyautogui.click()
			return 3
		
		# Convert the file to a format our APIs will understand
		print("Converting Captcha...")
		os.system("echo 'y' | ffmpeg -i " + DOWNLOAD_LOCATION + "audio.mp3 ./audio.wav 2>/dev/null")
		with sr.AudioFile('./audio.wav') as source:
			audio = r.record(source)
		
		print("Submitting To Speech to Text:")
		determined = google(audio) # Instead of google, you can use ibm or bing here
		print(determined)

		print("Inputting Answer")
		# Input the captcha 
		pyautogui.moveTo(FINAL_COORDS)
		pyautogui.click()
		time.sleep(.5)
		pyautogui.typewrite(determined, interval=.05)
		time.sleep(.5)
		pyautogui.moveTo(VERIFY_COORDS)
		pyautogui.click()

		print("Verifying Answer")
		time.sleep(5)
		
		# Check that the captcha is completed
		
		result = checkCaptcha()
		return result
	except Exception as e:
		pyautogui.moveTo(CLOSE_LOCATION)
		pyautogui.click()
		return 3


def runCaptcha(tempEmail):
	success = 0
	fail = 0
	allowed = 0

	# Run this forever and print statistics
	while True:
		res = runCap()
		if res == 1:
			success += 1
		elif res == 2: # Sometimes google just lets us in
			allowed += 1
		else:
			fail += 1

		print("SUCCESSES: " + str(success) + " FAILURES: " + str(fail) + " Allowed: " + str(allowed))

		if (res==2) or (res==1):
			break

		pyautogui.moveTo(CLOSE_LOCATION)
		pyautogui.click()

	#input email
	pyautogui.moveTo(EMAIL_INPUT)
	pyautogui.click()
	time.sleep(.5)
	pyautogui.typewrite(tempEmail, interval=.05)
	time.sleep(.5)
	#input password
	pyautogui.moveTo(PASSWORD_INPUT)
	pyautogui.click()
	time.sleep(.5)
	pyautogui.typewrite("testpassword12345", interval=.05)
	time.sleep(.5)

	#creatin new textnow account
	print (noCaptcha)
	if noCaptcha :
		pyautogui.moveTo(NOCAPTCHA_SIGNUP_BUTTON)
		pyautogui.click()
	else:
		pyautogui.moveTo(SIGNUP_BUTTON)
		pyautogui.click()

	return 3
	



		
	