import Engine

world = Engine.world()
player = Engine.Player("player",world)
enemy = Engine.Enemy("enemy",world)
world.start()