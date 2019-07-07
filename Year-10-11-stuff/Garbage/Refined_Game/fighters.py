class fighters:
    
    def __init__(self, world):
        self.coords = [0, 0]
        self.pcoords = [0, 0]
        self.symbol = "\u001b[33m@"
        self.inventory = ["raft"]
        self.world = world
        self.world.add_player(self)
        