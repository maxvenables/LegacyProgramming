import world
import fighters

       
world = world.world()

player = fighters.fighters(world)
world.import_world("river",player)

world.start_world()
    