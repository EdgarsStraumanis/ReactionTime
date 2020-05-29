#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import the PsychoPy libraries and rest
from psychopy import core, visual, event
import time
import csv
import os
import random

from psychopy.hardware import keyboard

# Create a window
win = visual.Window([800,600], monitor="testMonitor", color="white")


code_dir = os.path.dirname(__file__)
rel_path = "colorData.txt" # data set for allowed colors
abs_file_path = os.path.join(code_dir, rel_path)

file = open(abs_file_path, "r")
stimuli_color = file.read().split(" ")
file.close()

answers = [["Yes","Yeah","Sure","Roger"],["No","Nope","Negative","Not"]] # data sets for positive and negative test
mouse = event.Mouse()
keyboard = keyboard.Keyboard()
begin = visual.TextStim(win, text='''Rules:
1. You have to wait till different words appears
2. You have to click as fast as possible when it says positive and don't click when it says negative

When You're ready click to start''', color="black")

results = []
running = 1

def showResults():
    """
    Shows the average results for routine in accuracy and reaction time
    """
    ending = visual.TextStim(win, text=f"", color="black")
    ending.draw()
    win.flip()
    core.wait(1)

    print(results)

    total_tests = len(results)
    accuracy = total_tests
    time_avg = 0
    timed_clicks = 0
    for tests in results:
        if len(tests) == 2:
            if tests[0] in answers[0]:
                accuracy -= 1
        if len(tests) == 3:
            timed_clicks += 1
            time_avg += tests[2]
            if tests[0] in answers[1]:
                accuracy -= 1

    if (timed_clicks>0):
        ending = visual.TextStim(win, text=f"Accuracy of clicking: {'%.3f' % (accuracy/total_tests*100)}% with average clicking reaction time of: {'%.3f' % (time_avg/(timed_clicks))} seconds", color="black")
    else:
        ending = visual.TextStim(win, text=f"No clicks recorded", color="black")
    mouse.clickReset()
    while mouse.getPressed()[0]==0:
        ending.draw()
        win.flip()
        #exit result view

def askDifficulty():
    """
    Promts the users to select diffucluty based on 2 seconds/difficulty
    """
    approved = False
    difficulty_selection = visual.TextStim(win, text=f'''Select difficulty: [1-5] from which 1 is easy and 5 is hard''', color="black", alignHoriz="center")
    difficulty_selection.draw()
    win.flip()
        
    while approved == False: # difficulty
        keys = keyboard.getKeys()
        if '1' in keys:
            return 1
        if '2' in keys:
            return 2
        if '3' in keys:
            return 3
        if '4' in keys:
            return 4
        if '5' in keys:
            return 5

def doReactionTest():
    """
    Routine of the reaction time test
    """
    results.clear()
    begin.draw() # creates starting window
    win.flip()
    mouse.clickReset()
    while mouse.getPressed()[0]==0:
        keys = keyboard.getKeys()
        if 'escape' in keys:
            win.close()
            core.quit()
    mouse.clickReset()
    # awaits till the starting window has ended
    intensity = askDifficulty()
    
    ready_check = visual.TextStim(win, text='''Test will start after mouse click
    
Click ESC to exit
Click Backspace to return to beginning''', color="black", alignHoriz="center")
    ready_check.draw() 
    win.flip()
    
    while mouse.getPressed()[0]==0: #creates an escape and return in case the test has to be discontinued
        keys = keyboard.getKeys()
        if 'escape' in keys:
            win.close()
            core.quit()
        if 'backspace' in keys:
            return
    mouse.clickReset()
    # awaits the start of the test after difficulty and confirmation
    
    for x in range(1,20):
        clicking_word = answers[random.randint(0,1)][random.randint(0,len(answers[random.randint(0,1)])-1)] # word selection from list
        clicking_color = stimuli_color[random.randint(0,len(stimuli_color)-1)] # color selection from the list
        starting = visual.TextStim(win, text=" ")
        starting.draw()
        win.flip()
        
        core.wait(random.uniform(1, 2)/intensity) # gap between scales with intensity
        
        starting = visual.TextStim(win, text="")
        starting.draw()
        win.flip()
        
        startingClock = time.time()
        stop_stimul = 0
        waiting_clock = startingClock + (random.uniform(1, 2)/intensity)
        while (time.time() < waiting_clock) and (stop_stimul == 0):
            if mouse.getPressed()[0]==1:
                stop_stimul = 2

        startingClock = time.time()
        waiting_clock = startingClock + (2/intensity)
        recorded_click = 0
        while (time.time() < waiting_clock) and (stop_stimul == 0):
            message = visual.TextStim(win, text=clicking_word, color=clicking_color, height=0.3, alignHoriz="center")
            message.draw() # draw stimulus from randomized list
            win.flip()
            if mouse.getPressed()[0]==1:
                recorded_click = time.time()
                mouse.clickReset()
                stop_stimul = 1
                
        if stop_stimul == 1:
            results.append([clicking_word,stop_stimul,recorded_click-startingClock])
        else:
            results.append([clicking_word,stop_stimul])
        # begins next cycle of objects after ssaving the data
    showResults() # results after the test
    core.wait(1)

while True:
    doReactionTest() #always does the test unless it has been exited

# Backup close
# Close the window
win.close()

# Close PsychoPy
core.quit()