#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on April 19, 2021, at 17:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'scale_training'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\xf82\\Desktop\\OEA & HFD\\1 Screening\\1 training to use scales\\gLMS_LHS_training_SHORT.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='AliceBlue', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intense_instr"
intense_instrClock = core.Clock()
intense_slider_instr = visual.Slider(win=win, name='intense_slider_instr',
    size=(20,800), pos=(500,0), units=None,
    labels=['No sensation','Barely detectable', 'Weak', 'Moderate', 'Strong', 'Very strong', 'Strongest imaginable sensation of any kind'], ticks=[0, 1.4,6,17,35,51,100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
rating_instr1 = visual.TextStim(win=win, name='rating_instr1',
    text='Intensity scale instructions',
    font='Arial',
    pos=(-300, 0), height=40, wrapWidth=1000, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "intense_imagined"
intense_imaginedClock = core.Clock()
intense_slider_imagined = visual.Slider(win=win, name='intense_slider_imagined',
    size=(20,800), pos=(500,0), units=None,
    labels=['No sensation','Barely detectable', 'Weak', 'Moderate', 'Strong', 'Very strong', 'Strongest imaginable sensation of any kind'], ticks=[0, 1.4,6,17,35,51,100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
rating_item = visual.TextStim(win=win, name='rating_item',
    text='default text',
    font='Arial',
    pos=(-300, 0), height=40, wrapWidth=1000, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rate_instructions = visual.TextStim(win=win, name='rate_instructions',
    text='Rate the intensity of:',
    font='Arial',
    pos=(-600, 300), height=40, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
pause_exp = visual.TextStim(win=win, name='pause_exp',
    text='Pause for instructions',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "intense_real"
intense_realClock = core.Clock()
intense_slider_real = visual.Slider(win=win, name='intense_slider_real',
    size=(20,800), pos=(500,0), units=None,
    labels=['No sensation','Barely detectable', 'Weak', 'Moderate', 'Strong', 'Very strong', 'Strongest imaginable sensation of any kind'], ticks=[0, 1.4,6,17,35,51,100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
rating_item_2 = visual.TextStim(win=win, name='rating_item_2',
    text='default text',
    font='Arial',
    pos=(-300, 0), height=40, wrapWidth=1000, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rate_instrutions_2 = visual.TextStim(win=win, name='rate_instrutions_2',
    text='Rate the intensity of:',
    font='Arial',
    pos=(-600, 300), height=35, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
pause_exp = visual.TextStim(win=win, name='pause_exp',
    text='Pause for instructions',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "intense_taste"
intense_tasteClock = core.Clock()
intense_slider_taste = visual.Slider(win=win, name='intense_slider_taste',
    size=(20,800), pos=(500,0), units=None,
    labels=['No sensation','Barely detectable', 'Weak', 'Moderate', 'Strong', 'Very strong', 'Strongest imaginable sensation of any kind'], ticks=[0, 1.4,6,17,35,51,100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
rating_item_3 = visual.TextStim(win=win, name='rating_item_3',
    text='default text',
    font='Arial',
    pos=(-300, 0), height=40, wrapWidth=1000, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rate_instrutions_3 = visual.TextStim(win=win, name='rate_instrutions_3',
    text='Rate the intensity of:',
    font='Arial',
    pos=(-600, 300), height=35, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
whichcup = visual.TextStim(win=win, name='whichcup',
    text='default text',
    font='Arial',
    pos=(-400, 100), height=50, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "like_instr"
like_instrClock = core.Clock()
like_slider_instr = visual.Slider(win=win, name='like_slider_instr',
    size=(20,800), pos=(500,0), units=None,
    labels=['Most disliked sensation imaginable','Dislike extremely','Dislike very much','Dislike moderately','Dislike slightly','Neutral','Like slightly','Like moderately','Like very much','Like extremely','Most liked sensation imaginable'], ticks=[-100, -62.89, -41.58, -17.59, -5.92, 0, 6.25, 17.82, 44.43, 65.72, 100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
lhs_instr = visual.TextStim(win=win, name='lhs_instr',
    text='Liking scale instructions',
    font='Arial',
    pos=(-300, 0), height=40, wrapWidth=1000, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "like"
likeClock = core.Clock()
like_slider = visual.Slider(win=win, name='like_slider',
    size=(20,800), pos=(500,0), units=None,
    labels=['Most disliked sensation imaginable','Dislike extremely','Dislike very much','Dislike moderately','Dislike slightly','Neutral','Like slightly','Like moderately','Like very much','Like extremely','Most liked sensation imaginable'], ticks=[-100, -62.89, -41.58, -17.59, -5.92, 0, 6.25, 17.82, 44.43, 65.72, 100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
like_trials = visual.TextStim(win=win, name='like_trials',
    text='default text',
    font='Arial',
    pos=(-300, 0), height=40, wrapWidth=1000, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
lhs_instructions = visual.TextStim(win=win, name='lhs_instructions',
    text='Rate how much you like:',
    font='Arial',
    pos=(-600, 300), height=35, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You have completed the training :)',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intense_instr"-------
# update component parameters for each repeat
intense_slider_instr.reset()
mouse = event.Mouse(visible=False)

intense_slider_instr.marker.size=(2,.1);
intense_slider_instr.marker.color='Red';

mouse.setPos((0,0))
intense_slider_instr.markerPos=0
# keep track of which components have finished
intense_instrComponents = [intense_slider_instr, rating_instr1]
for thisComponent in intense_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intense_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "intense_instr"-------
while continueRoutine:
    # get current time
    t = intense_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intense_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intense_slider_instr* updates
    if intense_slider_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intense_slider_instr.frameNStart = frameN  # exact frame index
        intense_slider_instr.tStart = t  # local t and not account for scr refresh
        intense_slider_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intense_slider_instr, 'tStartRefresh')  # time at next scr refresh
        intense_slider_instr.setAutoDraw(True)
    
    # *rating_instr1* updates
    if rating_instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rating_instr1.frameNStart = frameN  # exact frame index
        rating_instr1.tStart = t  # local t and not account for scr refresh
        rating_instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rating_instr1, 'tStartRefresh')  # time at next scr refresh
        rating_instr1.setAutoDraw(True)
    x = mouse.getPos()[1]
    intense_slider_instr.markerPos=((x) /3)
    
    if mouse.getPressed()[0]:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intense_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intense_instr"-------
for thisComponent in intense_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
core.wait(0.5)
# the Routine "intense_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
gLMS_imagined_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('gLMS_imagined_2.xlsx'),
    seed=None, name='gLMS_imagined_trials')
thisExp.addLoop(gLMS_imagined_trials)  # add the loop to the experiment
thisGLMS_imagined_trial = gLMS_imagined_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGLMS_imagined_trial.rgb)
if thisGLMS_imagined_trial != None:
    for paramName in thisGLMS_imagined_trial:
        exec('{} = thisGLMS_imagined_trial[paramName]'.format(paramName))

for thisGLMS_imagined_trial in gLMS_imagined_trials:
    currentLoop = gLMS_imagined_trials
    # abbreviate parameter names if possible (e.g. rgb = thisGLMS_imagined_trial.rgb)
    if thisGLMS_imagined_trial != None:
        for paramName in thisGLMS_imagined_trial:
            exec('{} = thisGLMS_imagined_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intense_imagined"-------
    # update component parameters for each repeat
    intense_slider_imagined.reset()
    rating_item.setText(gLMS_imagined)
    mouse = event.Mouse(visible=False)
    
    intense_slider_imagined.marker.size=(2,.1);
    intense_slider_imagined.marker.color='Red';
    
    mouse.setPos((0,-0))
    intense_slider_imagined.markerPos=0
    # keep track of which components have finished
    intense_imaginedComponents = [intense_slider_imagined, rating_item, rate_instructions]
    for thisComponent in intense_imaginedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intense_imaginedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intense_imagined"-------
    while continueRoutine:
        # get current time
        t = intense_imaginedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intense_imaginedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intense_slider_imagined* updates
        if intense_slider_imagined.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intense_slider_imagined.frameNStart = frameN  # exact frame index
            intense_slider_imagined.tStart = t  # local t and not account for scr refresh
            intense_slider_imagined.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intense_slider_imagined, 'tStartRefresh')  # time at next scr refresh
            intense_slider_imagined.setAutoDraw(True)
        
        # *rating_item* updates
        if rating_item.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_item.frameNStart = frameN  # exact frame index
            rating_item.tStart = t  # local t and not account for scr refresh
            rating_item.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_item, 'tStartRefresh')  # time at next scr refresh
            rating_item.setAutoDraw(True)
        
        # *rate_instructions* updates
        if rate_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rate_instructions.frameNStart = frameN  # exact frame index
            rate_instructions.tStart = t  # local t and not account for scr refresh
            rate_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rate_instructions, 'tStartRefresh')  # time at next scr refresh
            rate_instructions.setAutoDraw(True)
        x = mouse.getPos()[1]
        intense_slider_imagined.markerPos=((x) / 3)
        
        if mouse.getPressed()[0]:
            gLMS_imagined_trials.addData('Intense_Imagined', intense_slider_imagined.markerPos)
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intense_imaginedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intense_imagined"-------
    for thisComponent in intense_imaginedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "intense_imagined" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'gLMS_imagined_trials'


# ------Prepare to start Routine "pause"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
pauseComponents = [pause_exp, key_resp]
for thisComponent in pauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "pause"-------
while continueRoutine:
    # get current time
    t = pauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pause_exp* updates
    if pause_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pause_exp.frameNStart = frameN  # exact frame index
        pause_exp.tStart = t  # local t and not account for scr refresh
        pause_exp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pause_exp, 'tStartRefresh')  # time at next scr refresh
        pause_exp.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pause"-------
for thisComponent in pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
gLMS_real_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('gLMS_real_2.xlsx'),
    seed=None, name='gLMS_real_trials')
thisExp.addLoop(gLMS_real_trials)  # add the loop to the experiment
thisGLMS_real_trial = gLMS_real_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGLMS_real_trial.rgb)
if thisGLMS_real_trial != None:
    for paramName in thisGLMS_real_trial:
        exec('{} = thisGLMS_real_trial[paramName]'.format(paramName))

for thisGLMS_real_trial in gLMS_real_trials:
    currentLoop = gLMS_real_trials
    # abbreviate parameter names if possible (e.g. rgb = thisGLMS_real_trial.rgb)
    if thisGLMS_real_trial != None:
        for paramName in thisGLMS_real_trial:
            exec('{} = thisGLMS_real_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intense_real"-------
    # update component parameters for each repeat
    intense_slider_real.reset()
    rating_item_2.setText(gLMS_real)
    mouse = event.Mouse(visible=False)
    
    intense_slider_real.marker.size=(2,.1);
    intense_slider_real.marker.color='Red';
    
    mouse.setPos((0,0))
    intense_slider_real.markerPos=0
    # keep track of which components have finished
    intense_realComponents = [intense_slider_real, rating_item_2, rate_instrutions_2]
    for thisComponent in intense_realComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intense_realClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intense_real"-------
    while continueRoutine:
        # get current time
        t = intense_realClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intense_realClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intense_slider_real* updates
        if intense_slider_real.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intense_slider_real.frameNStart = frameN  # exact frame index
            intense_slider_real.tStart = t  # local t and not account for scr refresh
            intense_slider_real.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intense_slider_real, 'tStartRefresh')  # time at next scr refresh
            intense_slider_real.setAutoDraw(True)
        
        # *rating_item_2* updates
        if rating_item_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_item_2.frameNStart = frameN  # exact frame index
            rating_item_2.tStart = t  # local t and not account for scr refresh
            rating_item_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_item_2, 'tStartRefresh')  # time at next scr refresh
            rating_item_2.setAutoDraw(True)
        
        # *rate_instrutions_2* updates
        if rate_instrutions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rate_instrutions_2.frameNStart = frameN  # exact frame index
            rate_instrutions_2.tStart = t  # local t and not account for scr refresh
            rate_instrutions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rate_instrutions_2, 'tStartRefresh')  # time at next scr refresh
            rate_instrutions_2.setAutoDraw(True)
        x = mouse.getPos()[1]
        intense_slider_real.markerPos=((x) / 3)
        
        if mouse.getPressed()[0]:
            gLMS_real_trials.addData('Intense_real', intense_slider_real.markerPos)
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intense_realComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intense_real"-------
    for thisComponent in intense_realComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "intense_real" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'gLMS_real_trials'


# ------Prepare to start Routine "pause"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
pauseComponents = [pause_exp, key_resp]
for thisComponent in pauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "pause"-------
while continueRoutine:
    # get current time
    t = pauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pause_exp* updates
    if pause_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pause_exp.frameNStart = frameN  # exact frame index
        pause_exp.tStart = t  # local t and not account for scr refresh
        pause_exp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pause_exp, 'tStartRefresh')  # time at next scr refresh
        pause_exp.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pause"-------
for thisComponent in pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
gLMS_taste_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('gLMS_tastes_2.xlsx'),
    seed=None, name='gLMS_taste_trials')
thisExp.addLoop(gLMS_taste_trials)  # add the loop to the experiment
thisGLMS_taste_trial = gLMS_taste_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGLMS_taste_trial.rgb)
if thisGLMS_taste_trial != None:
    for paramName in thisGLMS_taste_trial:
        exec('{} = thisGLMS_taste_trial[paramName]'.format(paramName))

for thisGLMS_taste_trial in gLMS_taste_trials:
    currentLoop = gLMS_taste_trials
    # abbreviate parameter names if possible (e.g. rgb = thisGLMS_taste_trial.rgb)
    if thisGLMS_taste_trial != None:
        for paramName in thisGLMS_taste_trial:
            exec('{} = thisGLMS_taste_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intense_taste"-------
    # update component parameters for each repeat
    intense_slider_taste.reset()
    rating_item_3.setText(gLMS_tastes)
    mouse = event.Mouse(visible=False)
    
    intense_slider_taste.marker.size=(2,.1);
    intense_slider_taste.marker.color='Red';
    
    mouse.setPos((0,0))
    intense_slider_taste.markerPos=0
    whichcup.setText(trialno)
    # keep track of which components have finished
    intense_tasteComponents = [intense_slider_taste, rating_item_3, rate_instrutions_3, whichcup]
    for thisComponent in intense_tasteComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intense_tasteClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intense_taste"-------
    while continueRoutine:
        # get current time
        t = intense_tasteClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intense_tasteClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intense_slider_taste* updates
        if intense_slider_taste.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intense_slider_taste.frameNStart = frameN  # exact frame index
            intense_slider_taste.tStart = t  # local t and not account for scr refresh
            intense_slider_taste.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intense_slider_taste, 'tStartRefresh')  # time at next scr refresh
            intense_slider_taste.setAutoDraw(True)
        
        # *rating_item_3* updates
        if rating_item_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_item_3.frameNStart = frameN  # exact frame index
            rating_item_3.tStart = t  # local t and not account for scr refresh
            rating_item_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_item_3, 'tStartRefresh')  # time at next scr refresh
            rating_item_3.setAutoDraw(True)
        x = mouse.getPos()[1]
        intense_slider_taste.markerPos=((x) / 3)
        
        if mouse.getPressed()[0]:
            gLMS_taste_trials.addData('Intense_taste', intense_slider_taste.markerPos)
            continueRoutine = False
        
        # *rate_instrutions_3* updates
        if rate_instrutions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rate_instrutions_3.frameNStart = frameN  # exact frame index
            rate_instrutions_3.tStart = t  # local t and not account for scr refresh
            rate_instrutions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rate_instrutions_3, 'tStartRefresh')  # time at next scr refresh
            rate_instrutions_3.setAutoDraw(True)
        
        # *whichcup* updates
        if whichcup.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            whichcup.frameNStart = frameN  # exact frame index
            whichcup.tStart = t  # local t and not account for scr refresh
            whichcup.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whichcup, 'tStartRefresh')  # time at next scr refresh
            whichcup.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intense_tasteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intense_taste"-------
    for thisComponent in intense_tasteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "intense_taste" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'gLMS_taste_trials'


# ------Prepare to start Routine "like_instr"-------
# update component parameters for each repeat
like_slider_instr.reset()
mouse = event.Mouse(visible=False)

like_slider_instr.marker.size=(2,.1);
like_slider_instr.marker.color='Red';

mouse.setPos((0,0))
like_slider_instr.markerPos=0
# keep track of which components have finished
like_instrComponents = [like_slider_instr, lhs_instr]
for thisComponent in like_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
like_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "like_instr"-------
while continueRoutine:
    # get current time
    t = like_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=like_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *like_slider_instr* updates
    if like_slider_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        like_slider_instr.frameNStart = frameN  # exact frame index
        like_slider_instr.tStart = t  # local t and not account for scr refresh
        like_slider_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(like_slider_instr, 'tStartRefresh')  # time at next scr refresh
        like_slider_instr.setAutoDraw(True)
    
    # *lhs_instr* updates
    if lhs_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lhs_instr.frameNStart = frameN  # exact frame index
        lhs_instr.tStart = t  # local t and not account for scr refresh
        lhs_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lhs_instr, 'tStartRefresh')  # time at next scr refresh
        lhs_instr.setAutoDraw(True)
    x = mouse.getPos()[1]
    like_slider_instr.markerPos=((x) /5 )
    
    if mouse.getPressed()[0]:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in like_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "like_instr"-------
for thisComponent in like_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
core.wait(0.5)
# the Routine "like_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LHS_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('LHS.xlsx'),
    seed=None, name='LHS_trials')
thisExp.addLoop(LHS_trials)  # add the loop to the experiment
thisLHS_trial = LHS_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLHS_trial.rgb)
if thisLHS_trial != None:
    for paramName in thisLHS_trial:
        exec('{} = thisLHS_trial[paramName]'.format(paramName))

for thisLHS_trial in LHS_trials:
    currentLoop = LHS_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLHS_trial.rgb)
    if thisLHS_trial != None:
        for paramName in thisLHS_trial:
            exec('{} = thisLHS_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "like"-------
    # update component parameters for each repeat
    like_slider.reset()
    like_trials.setText(LHS)
    mouse = event.Mouse(visible=False)
    
    like_slider.marker.size=(2,.1);
    like_slider.marker.color='Red';
    
    mouse.setPos((0,0))
    like_slider.markerPos=0
    # keep track of which components have finished
    likeComponents = [like_slider, like_trials, lhs_instructions]
    for thisComponent in likeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    likeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "like"-------
    while continueRoutine:
        # get current time
        t = likeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=likeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *like_slider* updates
        if like_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_slider.frameNStart = frameN  # exact frame index
            like_slider.tStart = t  # local t and not account for scr refresh
            like_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_slider, 'tStartRefresh')  # time at next scr refresh
            like_slider.setAutoDraw(True)
        
        # *like_trials* updates
        if like_trials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            like_trials.frameNStart = frameN  # exact frame index
            like_trials.tStart = t  # local t and not account for scr refresh
            like_trials.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_trials, 'tStartRefresh')  # time at next scr refresh
            like_trials.setAutoDraw(True)
        
        # *lhs_instructions* updates
        if lhs_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lhs_instructions.frameNStart = frameN  # exact frame index
            lhs_instructions.tStart = t  # local t and not account for scr refresh
            lhs_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lhs_instructions, 'tStartRefresh')  # time at next scr refresh
            lhs_instructions.setAutoDraw(True)
        x = mouse.getPos()[1]
        like_slider.markerPos=((x) / 5)
        
        if mouse.getPressed()[0]:
            LHS_trials.addData('Like', like_slider.markerPos)
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in likeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "like"-------
    for thisComponent in likeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "like" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'LHS_trials'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_2]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
