from Position import Position


class Translator:

    stepcount = 0
    steps = []
    stepsCranePan = []
    stepsCraneTilt = []
    stepsCraneTele = []
    stepsCamPan = []
    stepsCamTilt = []
    stepsCamZoom = []
    stepsCamFocus = []


    def __init__(self, stepcount):
        self.stepcount = stepcount
        for i in range(stepcount):
            self.steps.append(0)
            self.stepsCranePan.append(0)
            self.stepsCraneTilt.append(0)
            self.stepsCraneTele.append(0)
            self.stepsCamPan.append(0)
            self.stepsCamTilt.append(0)
            self.stepsCamZoom.append(0)
            self.stepsCamFocus.append(0)

    def smooth(self, x, m):
        n = 2*m+1
        if x<0.5:
            y=(pow(2,n-1))*pow(x,n)
        else:
            y=1-(pow((-2*x+2),n))/2
        return y


    def buildSteps(self, smoothnes):
        for i in range(self.stepcount):
            self.steps[i] = self.smooth((1/self.stepcount)*i, smoothnes)


    def interpolate(self, activePos: Position, targetPos: Position):

        dCranePan = targetPos.cranePan - activePos.cranePan
        dCraneTilt = targetPos.craneTilt - activePos.craneTilt
        dCraneTele = targetPos.craneTele - activePos.craneTele
        dCamPan = targetPos.camPan - activePos.camPan
        dCamTilt = targetPos.camTilt - activePos.camTilt
        dCamZoom = targetPos.camZoom - activePos.camZoom
        dCamFocus = targetPos.camFocus - activePos.camFocus

        for i in range(self.stepcount):
            self.stepsCranePan[i] = round(dCranePan*self.steps[i], 3) + activePos.cranePan
            self.stepsCraneTilt[i] = round(dCraneTilt*self.steps[i], 3) + activePos.craneTilt
            self.stepsCraneTele[i] = round(dCraneTele*self.steps[i], 3) + activePos.craneTele
            self.stepsCamPan[i] = round(dCamPan*self.steps[i], 3) + activePos.camPan
            self.stepsCamTilt[i] = round(dCamTilt*self.steps[i], 3) + activePos.camTilt
            self.stepsCamZoom[i] = round(dCamZoom*self.steps[i], 3) + activePos.camZoom
            self.stepsCamFocus[i] = round(dCamFocus*self.steps[i], 3) + activePos.camFocus
            print(self.stepsCranePan[i])
