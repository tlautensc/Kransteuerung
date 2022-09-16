class Position:
    cranePan = 0
    craneTilt = 0
    craneTele = 0
    camPan = 0
    camTilt = 0
    camZoom = 0
    camFocus = 0

    def __init__(self, cranePan, craneTilt, craneTele, camPan, camTilt, camZoom, camFocus):
        self.cranePan = cranePan
        self.craneTilt = craneTilt
        self.craneTele = craneTele
        self.camPan = camPan
        self.camTilt = camTilt
        self.camZoom = camZoom
        self.camFocus = camFocus

    def changeCranePan(self, i):
        self.cranePan + i
        if self.cranePan > 270:
            self.cranePan = 270
        if self.cranePan < -270:
            self.cranePan = 270

    def changeCraneTilt(self, i):
        self.craneTilt + i
        if self.craneTilt > 270:
            self.craneTilt = 270
        if self.craneTilt < -270:
            self.craneTilt = 270


    def changeCraneTele(self, i):
        self.craneTele + i
        if self.craneTele > 100:
            self.craneTele = 100
        if self.craneTele < 0:
            self.craneTele = 0

    def changeCamPan(self, i):
        self.camPan + i
        if self.camPan > 270:
            self.camPan = 270
        if self.camPan < -270:
            self.camPan = 270

    def changeCamTilt(self, i):
        self.camTilt + i
        if self.camTilt > 270:
            self.camTilt = 270
        if self.camTilt < -270:
            self.camTilt = 270

    def changeCamZoom(self, i):
        self.camZoom + i
        if self.camZoom > 100:
            self.camZoom = 100
        if self.camZoom < 0:
            self.camZoom = 0
    
    def changeCamFocus(self, i):
        self.camFocus + i
        if self.camFocus > 100:
            self.camFocus = 100
        if self.camFocus < 0:
            self.camFocus = 0
