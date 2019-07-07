import fighters
class world:
    
    def __init__(self):
        self.world =[]
        self.playerList = []
        self.coordsList = []
        self.teleLocals = []
        self.playerSCoords =[0, 0]
        
    
    def clear(self):
        for i in range(35):
            print()
            
    
    def getValue(self, value):
        x = value
        return x
            

    def add_player(self, player):
        player.coords = self.playerSCoords
        player.pcoords = self.playerSCoords
        self.playerList.append(player)
        self.coordsList.append(player.coords)
    
        
    def import_world(self, filename, player):
        file = open("maps/" + filename, "r")
        
        line = file.readline().rstrip("\n")
        coords = []
        if line[0] == "[":
            xs = line.split(",")
            coords.append(int(xs[1]))
            coords.append(int(xs[2]))
            line = file.readline().rstrip("\n")
        count = 0
        teles = []
        for i in xs:
            if count % 3 == 0:
                teles.append([])
            if count > 3:
                if count % 3 == 0:
                    teles[-2].append(i)
                else:
                    teles[-1].append(i)
            count += 1
        teles.pop(0)
        teles.pop(-1)
        
        self.teleLocals = teles
                
        print(xs)
        
        self.playerSCoords = coords
        self.add_player(player)
        print(self.playerSCoords)
        grid = []
        while line != "":
            xs = []
            for i in line:
                xs.append(i)
            grid.append(xs)
            line = file.readline().rstrip("\n")
        for i in grid:
            if "\n" in i:
                i.remove("\n")
        
            
        self.world = grid
        print(self.world)
        file.close()
        self.maxCoords = [len(self.world[0]), len(self.world)-1]
        
    def teleport(self, coords,player):
        possibleCoords = []
        for i in self.teleLocals:
            x = []
            x.append(int(i[0]))
            x.append(int(i[1]))
            possibleCoords.append(x)
            
        
        
        y = possibleCoords.index(coords)
        
        
        mapu = self.teleLocals[y][2]
        self.import_world(mapu,player)
        
        
        
    def print_world(self):
        self.clear()
        x = 0
        y = 0
        for i in self.world:
            for j in i:
                symbol =" "
                coords = []
                coords.append(x)
                coords.append(self.maxCoords[1] - y - 1)
                player = self.playerList[0]
                tile = self.decide_colour(j, player, False)
                if coords in self.coordsList:
                    index = self.coordsList.index(coords)
                    player = self.playerList[index]
                    symbol = player.symbol
                    tile = self.decide_colour(j, player, True)
                print(tile + symbol, end=" \u001b[0m")
                x += 1
            print()
            x = 0
            y += 1
            
    
    def move_player_through_world(self, player, move):
        pcoords = []
        for i in range(self.maxCoords[1] + 1):
            for j in range(self.maxCoords[0] + 1):
                xs = []
                xs.append(j)
                xs.append(i)
                if xs == player.coords:
                    pcoords = xs
                
        
        if move == "w":
            player.coords[1] = player.coords[1] + 1
        elif move == "a":
            player.coords[0] = player.coords[0] - 1
        elif move == "s":
            player.coords[1] = player.coords[1] - 1
        elif move == "d":
            player.coords[0] = player.coords[0] + 1
        
        
        if (player.coords[0] < 0) or (player.coords[0] > self.maxCoords[0] - 1) or (player.coords[1] < 0) or (player.coords[1] > self.maxCoords[1] - 1):
            self.pcoords_setter(player, pcoords)
        
        elif self.world[self.maxCoords[1] - 1 - player.coords[1]][player.coords[0]] == "~" and "raft" not in player.inventory:
            self.pcoords_setter(player, pcoords)
            
        elif self.world[self.maxCoords[1] - 1 - player.coords[1]][player.coords[0]] == "*":
            self.pcoords_setter(player, pcoords)
        
        elif self.world[self.maxCoords[1] - 1 - player.coords[1]][player.coords[0]] == "-":
            self.pcoords_setter(player, pcoords)
            
        elif self.world[self.maxCoords[1] - 1 - player.coords[1]][player.coords[0]] == "^":
            self.pcoords_setter(player, pcoords)
            
        possibleCoords = []
        for i in self.teleLocals:
            x = []
            x.append(int(i[0]))
            x.append(int(i[1]))
            possibleCoords.append(x)
            
        print(player.coords)
        print(possibleCoords)
            
        if player.coords in possibleCoords:
            self.teleport(player.coords,player)
            
    def pcoords_setter(self, player, pcoords):
        player.coords = pcoords
        index = self.playerList.index(player)
        self.coordsList[index] = player.coords

    def decide_colour(self, char, player, bol):
        """You're probably gonna need this: 
            http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html"""
        
        tile = ""
        if char == "x":
            tile = "\u001b[42m"
        elif char == "~" and "raft" in player.inventory and bol == True:
            tile = u"\u001b[48;5;94m"
        elif char == "~":
            tile = "\u001b[44m"
        elif char == "w":
            tile = "\u001b[47m"
        elif char == "*":
            tile = "\u001b[41m"
        elif char == "#":
            tile = u"\u001b[48;5;94m"
        elif char == "s":
            tile = u"\u001b[48;5;228m"
        elif char == "t":
            tile = u"\u001b[48;5;28m"
        elif char == "T":
            tile = u"\u001b[48;5;22m"
        elif char == "O":#entrace
            tile = u"\u001b[48;5;16m"
        elif char == "-":
            tile = u"\u001b[48;240m"
        elif char == "^":
             tile = u"\u001b[48;5;52m"
        elif char == "o":#exit
            tile = u"\u001b[48;136m"
        elif char == "w":
             tile = u"\u001b[37m"
        
        return tile

    def start_world(self):
        self.adventure_state(self.playerList[0])
        
    
    def adventure_state(self, player):
        move = ""
        while True:
            for i in self.playerList:
                self.move_player_through_world(i, move)
            self.print_world()
            move = input()

   