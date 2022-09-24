from Position import Position
from Translator import Translator
import logging
import copy
import json

logging.basicConfig(filename="log.log", level=logging.INFO)

activePos = Position(5,0,0,0,0,0,0)
targetPos = Position(20,0,0,0,0,0,0)
presetPos = []
time = 0
smoothnes = 1
stepcount = 20
translator = Translator(stepcount)
translator.buildSteps(1)

for i in range(16):
    presetPos.append(Position(i,0,0,0,0,0,0))

def execute(): 
    translator.interpolate(activePos, targetPos)
    activePos.update(targetPos.cranePan, targetPos.craneTilt, targetPos.craneTele, targetPos.camPan, targetPos.camTilt, targetPos.camZoom, targetPos.camFocus)

def presetSave(i):
    global presetPos
    presetPos[i] = copy.deepcopy(activePos)

def presetLoad(i):
    global targetPos
    targetPos = copy.deepcopy(presetPos[i])
    execute()

def saveShow(filename):
    pass  

def loadShow(filename):
    pass

