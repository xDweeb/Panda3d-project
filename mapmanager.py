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