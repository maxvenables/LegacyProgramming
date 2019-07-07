import random
import time
import sys
raw_input = input
class fighters:

    def __init__(self,name, world):
    ####
        Q = "y"
        world.add_entitie(self)
        self.potions = 1
        if name == "player":
            Q = input("Would you like to start a new game? (y/n)")
        if Q == "n":
            self.coords = []
            save = open("save.txt", "r")
            nextLine = save.readline()
            nextLine = nextLine.split()
            self.orgAttackStat = int(nextLine[0])
            self.attackStat = self.orgAttackStat
            self.orgDefenseStat = int(nextLine[1])
            self.defenseStat = self.orgDefenseStat
            self.healthStat = int(nextLine[2])
            self.orgHealthStat = int(nextLine[3])
            self.orgSpeedStat = int(nextLine[4])
            self.speedStat = self.orgSpeedStat
            self.orgMagicStat = int(nextLine[5])
            self.magicStat = self.orgMagicStat
            self.magicCooldown = self.orgMagicStat
            self.hasMagic = bool(nextLine[6])
            self.doClass = str(nextLine[7])
            self.className = self.doClass
            self.coords.append(int(nextLine[8][0]))
            self.coords.append(int(nextLine[8][1]))
            self.prevcoords = self.coords
            self.exp = int(nextLine[9])
            self.level = int(nextLine[10])
            self.potions = int(nextLine[11])
            self.name = "player"
            self.currentlyDefending = False
        else:
            self.classes = ["barb", "wiz", "knight", "rogue", "paladin", "upupdowndownleftrightleftrightbastart"]
            self.name = name
            self.coords = [8, 0]
            self.prevcoords = [8, 0]
            self.attackStat = random.randint(20, 25)
            self.defenseStat = random.randint(20, 25)
            self.healthStat = random.randint(20, 25)
            self.speedStat = random.randint(20, 25)
            self.magicStat = random.randint(20, 25)
            self.hasMagic = False
            self.exp = 0
            self.level = 1
            self.doClass = ""
            if self.doClass != "":
                classSelected = True
            else:
                self.classSelected = False
            if self.name == "player":
                while self.classSelected == False:
                    self.doClass = input("choose your class (barb, wiz, knight, rogue, paladin)")
                    if self.doClass in self.classes:
                        self.decideClass() 
                        self.classSelected = True
                    else:
                        print("Thats not a class MEME LORD")
            else:
                self.daWorld = world
                self.doClass = self.randClass()
                self.decideClass() 
        
            self.className = self.doClass
            self.orgAttackStat = self.attackStat
            self.orgDefenseStat = self.defenseStat
            self.orgHealthStat = self.healthStat
            self.orgSpeedStat = self.speedStat
            self.orgMagicStat = self.magicStat
            self.daWorld = world
            self.currentlyDefending = False
            self.magicCooldown = 0
        return None

   
    def decide_move(self, move, target):
        """
            finds what move user or computer will use
        """
        if self.name != "player": # checks if user isnt player
            relMove = self.get_move(target) #runs get_move to find a random attack, assigns it to relMove 
        else:
            relMove = move #for player
        if relMove == "a" or relMove == "attack" or relMove == "att": #attack
            self.attack(target)
        elif relMove == "d" or relMove == "defend" or relMove == "def": #defend
            self.defend()
        elif relMove == "h" or relMove == "heal":
            self.heal()
        elif relMove == "m" or relMove == "magic":
            self.magicAttack(target)
        elif relMove == "q" or relMove == "quit":
            self.daWorld.quit_game()
        elif relMove == "p" or relMove == "potion":
            if self.potions > 0:
                print("You used a potion and healed all your health")
                ##time.sleep(0.45)
                self.healthStat = self.orgHealthStat
                self.potions -= 1
        return None
        
        
    def get_move(self, target):
    
        
        choice = random.randint(1,9)
        if self.hasMagic == True:
            if choice == 3:
                move = "h"
            elif choice <= 2:
                move = "d"
            else:
                if choice == 4 or choice == 5:
                    move = "m"
                else:
                    move = "a"
        else:
            if choice <= 3:
                move = "d"
            else:
                move = "a"
            
        return move

    
    def attack(self, target):


        damagePre = (float(self.attackStat) / float(target.defenseStat)) * float(self.attackStat) #arbitrary formula to calculate damage done
        damageDone = (damagePre // 6) + 1 # ""
        target.healthStat -= int(damageDone) # takes health off target 
        if target.healthStat < 0: # makes sure target doesnt have negative health
            target.healthStat = 0
        self.stop_defending()
        print("\n" + self.name + " attacks")
        ##time.sleep(0.45)
        self.magicCooldown -= 1
        if self.magicCooldown < 0:
            self.magicCooldown = 0
        target.print_health()
        return None

    
    def defend(self):


        if not self.currentlyDefending:
               self.currentlyDefending = True
               self.defenseStat *= 2
        print("\n" + self.name + " defends ")
        ##time.sleep(0.45)
        recovery = 2
        self.healthStat += recovery
        if self.healthStat > self.orgHealthStat:
            self.healthStat = self.orgHealthStat
        print(self.name + " recovered " + str(recovery) + " health")
        ##time.sleep(0.45)
        self.print_health()
        self.magicCooldown -= 1
        if self.magicCooldown < 0:
            self.magicCooldown = 0
        return None


    def heal(self):
        if self.hasMagic == True:
            if self.magicCooldown < 2:
                recovery = self.magicStat // 4
                self.healthStat += recovery
                if self.healthStat > self.orgHealthStat: 
                    self.healthStat = self.orgHealthStat
                print(self.name + " recoverd " + str(recovery)+ " health, " + self.name + " now has " + str(self.healthStat))
                #time.sleep(0.45)
                self.magicCooldown += 1
                if self.magicCooldown == 2:
                    print(self.name + " is now on magic cooldown, " + self.name +" cannot use a magical move for 2 turn(s)")
                    #time.sleep(0.45)
            else:
                if self.magicCooldown == 1:
                    print(self.name + " is on magical cooldown " + self.name +" will be able to use magical move next turn")
                    self.magicCooldown -= 1
                    if self.magicCooldown < 0:
                        self.magicCooldown = 0
                    #time.sleep(0.45)
                else:
                    print(self.name + " is on magical cooldown " + self.name +" will be able to use magical move in " + str(self.magicCooldown) + " turn(s)")
                    self.magicCooldown -= 1
                    if self.magicCooldown < 0:
                        self.magicCooldown = 0
                    #time.sleep(0.45)
        else:
            print(self.name + " cannot heal as " + self.name +" has no magical capabilities")
            #time.sleep(0.45)
    
    def magicAttack(self, target):
        if self.hasMagic:
            if self.magicCooldown == 0:
                if self.magicCooldown == 0: 
                    damageDone = self.magicStat // 3
                    target.healthStat -= int(damageDone) 
                    if target.healthStat < 0: 
                        target.healthStat = 0
                    self.stop_defending()
                    print("\n" + self.name + " uses a magical attack")
                    #time.sleep(0.45)
                    target.print_health()
                    self.magicCooldown = 2
                    print(self.name + " is now on magic cooldown, " + self.name +" cannot use a magical move for 2 turns")
                    #time.sleep(0.45)
            else:
                self.magicCooldown -= 1
                if self.magicCooldown < 0:
                    self.magicCooldown = 0
                if self.magicCooldown == 1:
                    print(self.name + " is on magical cooldown " + self.name +" will be able to use magical move next turn")
                    #time.sleep(0.45)
                else:
                    print(self.name + " is on magical cooldown " + self.name +" will be able to use magical move in " + str(self.magicCooldown) + " turns")
                    #time.sleep(0.45)
                self.magicCooldown -= 1
                if self.magicCooldown < 0:
                    self.magicCooldown = 0
        else:               
            print(self.name + " cannot use a magical attack as " + self.name +" has no magical capabilities")
            #time.sleep(0.45)
    
    def reset_magic(self):
        self.magicCooldown = 0
            
   
    def stop_defending(self):


        if self.currentlyDefending:
            self.currentlyDefending = False
            self.defenseStat /= 2
        return None


    def print_health(self):
        
        
        print(self.name + " health is " + str(self.healthStat) + "\n")
        #time.sleep(0.45)
        
    def print_things(self):
        print(self.name + " health is " + str(self.healthStat))
        print(self.name + "class is " + str(self.className) + "\n")
    
    def print_stats(self):
        
        
        print(self.name + "health is " + str(self.healthStat))
        print(self.name + "attack is " + str(self.attackStat))
        print(self.name + "defense is " + str(self.defenseStat))
        print(self.name + "magic is " + str(self.magicStat))
        print(self.name + "speed is " + str(self.speedStat))
        print(self.name + "class is " + str(self.className) + "\n")
    
    def refreshStats(self):
        
        
        self.healthStat = self.orgHealthStat
        self.defenseStat = self.orgDefenseStat
        self.currentlyDefending = False
        
    
    def randomiseStats(self):
        
        
        self.attackStat = random.randint(20, 25)
        self.defenseStat = random.randint(20, 25)
        self.healthStat = random.randint(20, 25)
        self.speedStat = random.randint(20, 25)
        self.magicStat = random.randint(20, 25)
        self.doClass = self.randClass()
        self.decideClass() 
        self.className = self.doClass
        self.orgAttackStat = self.attackStat
        self.orgDefenseStat = self.defenseStat
        self.orgHealthStat = self.healthStat
        self.orgSpeedStat = self.speedStat
        self.orgMagicStat = self.magicStat
        
    def decideClass(self):
        
        
        if self.doClass == "barb":
            self.attackStat += 10
            self.speedStat += 7
            self.defenseStat -= 5
            self.healthStat -= 5
            self.hasMagic = False
            
        elif self.doClass == "wiz":
            self.attackStat -= 10
            self.speedStat -= 5
            self.magicStat += 10
            self.defenseStat += 2            
            self.hasMagic = True
        
        elif self.doClass == "knight":
            self.attackStat += 7
            self.defenseStat += 5
            self.speedStat -= 3
            self.hasMagic = False

        
        elif self.doClass == "rogue": 
            self.attackStat += 5
            self.defenseStat -= 3
            self.healthStat -= 5
            self.speedStat += 15
            self.hasMagic = False
            
        elif self.doClass == "paladin":
            self.defenseStat += 10
            self.attackStat -= 10
            self.healthStat += 7
            self.speedStat -= 15
            self.magicStat -= 10
            self.hasMagic = True
            
        elif self.doClass == "upupdowndownleftrightleftrightbastart":
            self.attackStat = 1000
            self.orgHealthStat = 1000
            self.defenseStat = 1000
            self.healthStat = 1000
            self.speedStat = 1000
            self.magicStat = 1000
            self.hasMagic = True
            self.doClass = "GOD"
            
            
        elif self.doClass == "BOSS":
            self.hasMagic = True
            
        if self.name == "enemy" and self.doClass == "GOD":
            self.attackStat -= 5
            self.defenseStat -= 5
            self.healthStat -= 5
            self.speedStat -= 5
            self.magicStat -= 5
        
        if self.hasMagic == False:
            self.magicStat = 0
            
    def randClass(self):
        classes = ["barb", "wiz", "knight", "rogue", "paladin"]
        num = random.randint(0,4)
        final = classes[num]
        return final
        
    def levelUp(self):
        expNeeded = 40 * (2**self.level - 1)
        expNeeded -= self.exp
        if self.exp >= expNeeded:
            self.level += 1
            self.exp -= expNeeded
            expNeeded = 40 * (2**self.level - 1)
            print("You leveled up to level " + str(self.level) )
            print("You have " + str(expNeeded) + " till level " + str(self.level + 1))
            self.attackStat += random.randint(1, 5)
            self.defenseStat += random.randint(1, 5)
            self.orgHealthStat += random.randint(1, 5)
            self.speedStat += random.randint(1, 5)
            if self.hasMagic == True:
                self.magicStat += random.randint(1, 5)
            
            self.orgAttackStat = self.attackStat
            self.orgDefenseStat = self.defenseStat
            self.healthStat = self.orgHealthStat
            self.orgSpeedStat = self.speedStat
            self.orgMagicStat = self.magicStat
            print("your attack stat is now " + str(self.orgAttackStat))
            print("your defense stat is now " + str(self.orgDefenseStat))
            print("your speed stat is now " + str(self.orgSpeedStat))
            print("your health stat is now " + str(self.orgHealthStat))
            print("your magic stat is now " + str(self.orgMagicStat))
        else:
            print("You have " + str(expNeeded) + " till level " + str(self.level + 1))
            
    def makeBoss(self):
        self.attackStat = 35
        self.defenseStat = 35
        self.healthStat = 35
        self.speedStat = 35
        self.magicStat = 35
        self.doClass = "BOSS"
        self.decideClass() 
        self.className = self.doClass
        self.orgAttackStat = self.attackStat
        self.orgDefenseStat = self.defenseStat
        self.orgHealthStat = self.healthStat
        self.orgSpeedStat = self.speedStat
        self.orgMagicStat = self.magicStat
        
        
        



class Player(fighters):
    
    def __init__(self, name, world):
        fighters.__init__(self, name, world) ###

    def run(self): # player exclusive

        if self.healthStat <= 0:
            print("\nThe enemy has won, you have hurried back to the nearest friendly home\n")
            self.daWorld.leave_battle("enemy")
        else:
            print("\n" + self.name + " ran\n")
            self.daWorld.leave_battle("noone")
            
    def decide_move(self, move, target):
        relMove = move #for player
        if relMove == "a" or relMove == "attack" or relMove == "att": #attack
            self.attack(target)
        elif relMove == "d" or relMove == "defend" or relMove == "def": #defend
            self.defend()
        elif relMove == "r" or relMove == "run":
            self.run()
        elif relMove == "h" or relMove == "heal":
            self.heal()
        elif relMove == "m" or relMove == "magic":
            self.magicAttack(target)
        elif relMove == "q" or relMove == "quit":
            self.daWorld.quit_game()
        elif relMove == "p" or relMove == "potion":
            if self.potions > 0:
                print("You used a potion and healed all your health")
                #time.sleep(0.45)
                self.healthStat = self.orgHealthStat
                self.potions -= 1
        return None








class Enemy(fighters):
    pass
    







class world:
    
    
    def __init__(self):
        
        
        self.entitiesList = []
    
    
    def sortSpeeds(self, *entities):
        
        
        speeds = []
        for i in entities: 
           for j in i:
              speeds.append(j.speedStat)
        sortSpeeds = sorted(speeds)
        objectsInOrder = []
        for i in sortSpeeds:
            for j in entities:
                for k in j:
                    if i == k.speedStat:
                        if k not in objectsInOrder:
                            objectsInOrder.append(k)
        final =[]
        length = len(objectsInOrder)
        while length != 0:
            final.append(objectsInOrder[length-1])
            length -= 1
        return final
        
        
    def add_entitie(self, newEnt):
        
        
        (self.entitiesList).append(newEnt)

   
    
    def update_fight(self):
        
        
        if self.entitiesList[0].healthStat == 0:
            if len(self.entitiesList) > 2:
                winner = "enemies"
            else:
                winner = "enemy"
        elif self.entitiesList[0].healthStat != 0 and self.entitiesList[1].healthStat != 0:
            winner = "noone"
        else:
            winner = "player"
        
        return winner
    def return_world(self, prevcoords):
        
        
        if prevcoords == [8, 0]:
            self.add_place(self.overworld, "\033[1;34mH \033[1;32m" , prevcoords[0], prevcoords[1])
        elif prevcoords == [0, 8]:
            self.add_place(self.overworld, "\033[1;30mC \033[1;32m" , prevcoords[0], prevcoords[1])
        else:
            self.add_place(self.overworld, "\033[1;32mx \033[1;32m" , prevcoords[0], prevcoords[1])
        
    def adventuring(self):
        
        for i in self.entitiesList:
            i.reset_magic()
            notInBattle = True
            moves = ["w", "a", "s", "d", "q"]
            #coords = "Player coords are ({0}, {1})"
        while notInBattle == True:
            
            userInput = input("\nMove with w/a/s/d: ")
            if userInput in moves:
                self.prevcoords = self.entitiesList[0].coords
                #print(coords.format(prevcoords[0],prevcoords[1]))
                self.return_world(self.prevcoords)
                if userInput == "w":
                    self.entitiesList[0].coords[0] -= 1
                elif userInput == "a":
                    self.entitiesList[0].coords[1] -= 1
                elif userInput == "s":
                    self.entitiesList[0].coords[0] += 1
                elif userInput == "d":
                    self.entitiesList[0].coords[1] += 1
                elif userInput == "q":
                    save = open("save.txt", "w")
                    save.write(str(self.entitiesList[0].orgAttackStat) + " " + str(self.entitiesList[0].orgDefenseStat) + " " + str(self.entitiesList[0].orgHealthStat) + " " + str(self.entitiesList[0].healthStat) + " " + str(self.entitiesList[0].orgSpeedStat) + " " + str(self.entitiesList[0].orgMagicStat) + " " + str(self.entitiesList[0].hasMagic) + " " + str(self.entitiesList[0].doClass)+ " " + str(self.entitiesList[0].coords[0]) + str(self.entitiesList[0].coords[1]) + " " + str(self.entitiesList[0].exp) + " " + str(self.entitiesList[0].level) + " " + str(self.entitiesList[0].potions))
                    save.close()
                    self.quit_game()
                
                if self.entitiesList[0].coords[1] >= self.maxX:
                    self.entitiesList[0].coords[1] = 8
                
                if self.entitiesList[0].coords[1] < 0:
                    self.entitiesList[0].coords[1] = 0
                    
                if self.entitiesList[0].coords[0] >= self.maxY:
                    self.entitiesList[0].coords[0] = 8
                
                if self.entitiesList[0].coords[0] < 0:
                    self.entitiesList[0].coords[0] = 0
            
                
                
                
                
                
                #print(coords.format(self.entitiesList[0].coords[0],self.entitiesList[0].coords[1]))
                self.add_place(self.overworld, "\033[1;33m@ \033[1;32m",self.entitiesList[0].coords[0], self.entitiesList[0].coords[1])
                self.clear()
                self.print_world(self.overworld)
                
                
                rand = random.randint(1,10)
                if rand < 4:
                    notInBattle = False
                if self.entitiesList[0].coords == [0, 8]:
                    notInBattle = False
            else:
                print("that is not a move")
            
        
        self.enter_battle()
        
    def clear(self):
        for i in range(100):
            print()
        
    def gen_world(self, width, height):
        worldo =[]
        self.maxX = width
        self.maxY = height
        for i in range(height+1):
            worldo.append([])
            for j in range(width+1):
                worldo[i].append("\u001b[32mx \033[1;32m")
        return(worldo)
    
    def add_place(self, worldo, symbol, width, height):
        worldo[width][height] = symbol
    
    def print_world(self, worldo):
        self.clear()
        for i in worldo:
            for j in i:
                print(j, end="")
            print("")
        
    
    def fighting(self):
        
        self.clear()
        print("\nyou encounter an enemy\n")
        winner = "" 
        speeds = self.sortSpeeds(self.entitiesList)
        gamePlaying = True
        self.entitiesList[1].print_things()
        self.entitiesList[0].print_things()
        while gamePlaying:
            userMove = raw_input("\nenter move(a/d/h/m/r): ") ###
            print("")
            for i in speeds:
                if i == self.entitiesList[0]:
                    self.entitiesList[0].decide_move(str(userMove), self.entitiesList[1])
                    if self.entitiesList[1].healthStat == 0:
                        break
                else:
                    self.entitiesList[1].decide_move("",self.entitiesList[0])
                    if self.entitiesList[0].healthStat == 0:
                        break
                    
            winner = self.update_fight()
            if winner != "noone":
                self.leave_battle(winner)
                
    def start(self):
        
        self.overworld = self.gen_world(8, 8)
        self.add_place(self.overworld, "\033[1;34mH \033[1;32m" ,8,0)
        self.add_place(self.overworld, "\033[1;30mC \033[1;32m" ,0, 8)
        self.clear()
        self.print_world(self.overworld)
        self.adventuring()
    
    
    def enter_battle(self):
        self.entitiesList[0].print_stats()
        if self.entitiesList[0].coords == [0, 8]:
            self.entitiesList[1].makeBoss()
        
        self.fighting()
    
    def leave_battle(self, winner):
        
        if winner == "player":
            print("\nyou have vanquished your enemy\n")
            self.entitiesList[0].exp += 20 * self.entitiesList[1].level
            pot = random.randint(1, 10)
            if pot < 3:
                self.entitiesList[0].potions += 1 
                print("Your enemy dropped a potion")
            if self.entitiesList[1].doClass == "BOSS":
                self.finish_game()
                
        
        elif winner == "enemies":
            print("\nThe " + winner + " have won, you have hurried back to the nearest friendly home\n")
        
        elif winner == "noone":
            print("\nYou ran away ... coward\n")
        else:
            print("\nThe " + winner + " has won, you have hurried back to the nearest friendly home\n")
                    
        if winner != "player" and winner != "noone":
            self.entitiesList[0].refreshStats()
            self.entitiesList[0].coords = [8, 0]
            self.return_world(self.prevcoords)
        self.entitiesList[1].randomiseStats()
        self.entitiesList[0].levelUp()
        self.adventuring()
        
    def finish_game(self):
        print("you have beatean the game, stop playing")
        sys.exit(0)
    def quit_game(self):
        save = open("save.txt", "w")
        save.write(str(self.entitiesList[0].orgAttackStat) + " " + str(self.entitiesList[0].orgDefenseStat) + " " + str(self.entitiesList[0].orgHealthStat) + " " + str(self.entitiesList[0].healthStat) + " " + str(self.entitiesList[0].orgSpeedStat) + " " + str(self.entitiesList[0].orgMagicStat) + " " + str(self.entitiesList[0].hasMagic) + " " + str(self.entitiesList[0].doClass)+ " " + str(self.entitiesList[0].coords[0]) + str(self.entitiesList[0].coords[1]) + " " + str(self.entitiesList[0].exp) + " " + str(self.entitiesList[0].level) + " " + str(self.entitiesList[0].potions))
        save.close()
        
        sys.exit(0)
#sweet