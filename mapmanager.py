class Mapmanager:
    def __init__(self):
        self.color = (0.2, 0.8, 0.2, 1)

        self.startNew()
        self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position):
        self.block = loader.loadModel("models/box")
        self.block.setPos(position)
        self.block.setScale(1)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    def createMap(self):
        for x in range(5):
            for y in range(5):
                if (x + y) % 2 == 0:
                    color = (0.2, 0.8, 0.2, 1)
                    z = 0
                else:
                    color = (0.2, 0.4, 0.9, 1)
                    z = 1

                self.addBlock((x, y + 10, z), color)