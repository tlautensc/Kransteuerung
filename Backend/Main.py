from Position import Position
import logging
import copy

logging.basicConfig(filename="log.log", level=logging.INFO)


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
    logger = logging.getLogger("execute")
    logger.setLevel(logging.DEBUG)
    
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
        stepsCranePan.append(round(dCranePan*steps[i],3))
        stepsCraneTilt.append(round(dCraneTilt*steps[i],3))
        stepsCraneTele.append(round(dCraneTele*steps[i],3))
        stepsCamPan.append(round(dCamPan*steps[i],3))
        stepsCamTilt.append(round(dCamTilt*steps[i],3))
        stepsCamZoom.append(round(dCamZoom*steps[i],3))
        stepsCamFocus.append(round(dCamFocus*steps[i],3))

    logger.debug(activePos.cranePan)
    logger.debug(activePos)
    activePos.update(targetPos.cranePan, targetPos.craneTilt, targetPos.craneTele, targetPos.camPan, targetPos.camTilt, targetPos.camZoom, targetPos.camFocus)
    logger.debug(activePos.cranePan)
    logger.debug(activePos)


def smooth(x,m):
    n = 2*m+1
    if x<0.5:
        y=(pow(2,n-1))*pow(x,n)
    else:
        y=1-(pow((-2*x+2),n))/2
    return y


execute()