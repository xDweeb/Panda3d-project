from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.land = Mapmanager()

        base.camera.setPos(2, -12, 8)
        base.camera.setHpr(0, -25, 0)
        base.camLens.setFov(90)

game = Game()
game.run()