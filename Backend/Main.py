from Position import Position
import copy

activePos = Position(0,0,0,0,0,0,0)
presetPos = []
time = 0
smoothnes = 0

for i in range(16):
    presetPos.append(Position(0,0,0,0,0,0,0))

def presetSave(i):
    global presetPos
    presetPos[i] = copy.deepcopy(activePos)

def presetLoad(i):
    global activePos
    activePos = copy.deepcopy(presetPos[i])
    execute()

def execute():
    pass
