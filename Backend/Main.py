from Position import Position
import copy

activePos = Position(0,0,0,0,0,0,0)
targetPos = Position(10,0,0,0,0,0,0)
presetPos = []
time = 0
smoothnes = 1

for i in range(16):
    presetPos.append(Position(0,0,0,0,0,0,0))

def presetSave(i):
    global presetPos
    presetPos[i] = copy.deepcopy(activePos)

def presetLoad(i):
    global targetPos
    targetPos = copy.deepcopy(presetPos[i])
    execute()

def execute():
    stepcount = 20
    steps = []

    for i in range(stepcount):
        steps.append(smooth((1/stepcount)*i,smoothnes))

    dCranePan = targetPos.cranePan - activePos.cranePan
    dCraneTilt = targetPos.craneTilt - activePos.craneTilt
    dCraneTele = targetPos.craneTele - activePos.craneTele
    dCamPan = targetPos.camPan - activePos.camPan
    dCamTilt = targetPos.camTilt - activePos.camTilt
    dCamZoom = targetPos.camZoom - activePos.camZoom
    dCamFocus = targetPos.camFocus - activePos.camFocus
    stepsCranePan = []
    stepsCraneTilt = []
    stepsCraneTele = []
    stepsCamPan = []
    stepsCamTilt = []
    stepsCamZoom = []
    stepsCamFocus = []

    for i in range(stepcount):
        stepsCranePan.append(dCranePan*steps[i])
        stepsCraneTilt.append(dCraneTilt*steps[i])
        stepsCraneTele.append(dCraneTele*steps[i])
        stepsCamPan.append(dCamPan*steps[i])
        stepsCamTilt.append(dCamTilt*steps[i])
        stepsCamZoom.append(dCamZoom*steps[i])
        stepsCamFocus.append(dCamFocus*steps[i])
        


def smooth(x,m):
    n = 2*m+1
    if x<0.5:
        y=(pow(2,n-1))*pow(x,n)
    else:
        y=1-(pow((-2*x+2),n))/2
    return y


execute()