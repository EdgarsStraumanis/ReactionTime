# ReactionTimeAndAccuracy
A little application that tests reaction time and accruacy based on words and colors.
Author: Edgars Straumanis
Created: May 2020
Last update: 5/29/2020

This application is based on PsychoPy v3 https://www.psychopy.org/
The application was made on Python version 3.7.5

Base of the program consists from 1 file for the code and 1 file for the data.

Application runs through several screens:
1. Starting view, describes the routine. After mouseButton1 click it goes to 2nd view.
	Rules:
	1. You have to wait till different words appears
	2. You have to click as fast as possible when it says positive and don't click when it says negative

	When You're ready click to start
This view has an option to use ESC to escape application.

2. Difficulty view, lets the user select the difficulty of how fast stimuls appears. After mouseButton1 click it goes to 3nd view.
	Select difficulty: [1-5] from which 1 is easy and 5 is hard
	
3. Confirmation view, promts for the user to use mouseButton1 or allows the user to exit the application or return to the 1st step
	Test will start after mouse click
		
	Click ESC to exit
	Click Backspace to return to beginning
After the confirmation in starts the 4th step based on the difficulty selected

4. Routine views, with randomized delays shows the user view of an object(word with color)
The step uses the Rule set of 1st view.
After completing 20 repeats of 4th step the program goes to result view

5. Result view, shows the user results for the test - accuracy and reaction time.
After mouse click 1 the program returns to 1st step.

The aplication is open source for educational purposes that can be copied, modified, learned from. It's not meant for any other way of use.