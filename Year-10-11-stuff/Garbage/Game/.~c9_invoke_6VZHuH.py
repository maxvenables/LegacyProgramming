import random
input = raw_input
class fighters:

    def __init__(self,name, world):
    ####
        
        world.add_entitie(self)
        self.name = name
        self.attackStat = random.randint(20, 25)
        self.defenseStat = random.randint(20, 25)
        self.healthStat = random.randint(20, 25)
        self.speedStat = random.randint(20, 25)
        self.magicStat = random.randint(20, 25)
        self.hasMagic = False
        self.doClass = ""
        if self.name == "player":
            self.doClass = input("what do you want to be(barb, wiz, knight, rouge, paladin)")
            self.decideClass() 
        else:
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
        self.exp = 0
        self.level = 1
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
        self.magicCooldown -= 1
        target.print_health()
        return None

    
    def defend(self):


        if not self.currentlyDefending:
               self.currentlyDefending = True
               self.defenseStat *= 2
        print("\n" + self.name + " defends ")
        recovery = 2
        self.healthStat += recovery
        if self.healthStat > self.orgHealthStat:
            self.healthStat = self.orgHealthStat
        print(self.name + " recovered " + str(recovery) + " health")
        self.print_health()
        self.magicCooldown -= 1
        return None


    def heal(self):
        if self.hasMagic == True:
            if self.magicCooldown < 2:
                recovery = self.magicStat // 4
                self.healthStat += recovery
                if self.healthStat > self.orgHealthStat: 
                    self.healthStat = self.orgHealthStat
                print(self.name + " recoverd " + str(recovery)+ " health, " + self.name + " now has " + str(self.healthStat))
                self.magicCooldown += 1
                if self.magicCooldown == 2:
                    print(self.name + " is now on magic cooldown, " + self.name +" cannot use a magical move for 2 turn(s)")
            else:
                if self.magicCooldown == 1:
                    print(self.name + " is on magical cooldown " + self.name +" will be able to use magical move next turn")
                else:
                    print(self.name + " is on magical cooldown " + self.name +" will be able to use magical move in " + str(self.magicCooldown) + " turn(s)")
        else:
            print(self.name + " cannot heal as " + self.name +" has no magical capabilities")
            
    
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
                    target.print_health()
                    self.magicCooldown = 2
                    print(self.name + " is now on magic cooldown, " + self.name +" cannot use a magical move for 2 turns")
            else:
                self.magicCooldown -= 1
                if self.magicCooldown < 0:
                    self.magicCooldown = 0
                if self.magicCooldown == 1:
                    print(self.name + " is on magical cooldown " + self.name +" will be able to use magical move next turn")
                else:
                    print(self.name + " is on magical cooldown " + self.name +" will be able to use magical move in " + str(self.magicCooldown) + " turns")
                self.magicCooldown -= 1
                if self.magicCooldown < 0:
                    self.magicCooldown = 0
        else:               
            print(self.name + " cannot heal as " + self.name +" has no magical capabilities")
    
    def reset_magic(self):
        self.magicCooldown = 0
            
   
    def stop_defending(self):


        if self.currentlyDefending:
            self.currentlyDefending = False
            self.defenseStat /= 2
        return None


    def print_health(self):
        
        
        print(self.name + " health is " + str(self.healthStat) + "\n")
        
    
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
            self.defenseStat -= 10
            self.healthStat -= 7
            self.hasMagic = False
            
        elif self.doClass == "wiz":
            self.attackStat -= 10
            self.speedStat -= 5
            self.magicStat += 10
            self.hasMagic = True
        
        elif self.doClass == "knight":
            self.attackStat += 5
            self.defenseStat += 3
            self.speedStat -= 2
            self.hasMagic = False

        
        elif self.doClass == "rouge": 
            self.attackStat += 5
            self.defenseStat -= 7
            self.healthStat -= 5
            self.speedStat += 10
            self.hasMagic = False
            
        elif self.doClass == "paladin":
            self.defenseStat += 5
            self.healthStat += 10
            self.speedStat -= 10
            self.magicStat -= 10
            self.hasMagic = True
            
        if self.hasMagic == False:
            self.magicStat = 0
        
    def randClass(self):
        classes = ["barb", "wiz", "knight", "rouge", "paladin"]
        num = random.randint(0,4)
        final = classes[num]
        return final
        
        
        
        
        



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

   
    
    def update(self):
        
        
        if self.entitiesList[0].healthStat == 0:
            if len(self.entitiesList) > 2:
                winner = "enemies"
            else:
                winner = "enemy"
        elif self.entitiesList[0].healthStat != 0 and self.entitiesList[1].healthStat != 0:
            winner = "noone"
        
        elif self.entitiesList[0].healthStat == 0 and self.entitiesList[1].healthStat == 0:
            winner = "deadlock"
        
        else:
            winner = "player"
        
        return winner
        
        
    def adventuring(self):
        for i in self.entitiesList:
            i.reset_magic()
        
        self.enter_battle()
        
    
    def fighting(self):
        
        
        winner = "" 
        speeds = self.sortSpeeds(self.entitiesList)
        gamePlaying = True
        self.entitiesList[1].print_stats()
        self.entitiesList[0].print_stats()
        while gamePlaying:
            userMove = raw_input("\nenter move(a/d/h/r): ") ###
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
                    
            winner = self.update()
            if winner != "noone":
                self.leave_battle(winner)
                
    def start(self):
        
        
        self.adventuring()
    
    
    def enter_battle(self):
        
        
        self.fighting()
    
    def leave_battle(self, winner):
        
        if winner == "player":
            print("\nyou have vanquished your enemy\n")
        
        elif winner == "enemies":
            print("\nThe " + winner + " have won, you have hurried back to the nearest friendly home\n")
        
        elif winner == "noone":
            print("\nYou ran away ... coward\n")
        else:
            print("\nThe " + winner + " has won, you have hurried back to the nearest friendly home\n")
                    
        if winner != "player" and winner != "noone":
            self.entitiesList[0].refreshStats()
        self.entitiesList[1].randomiseStats()
        self.adventuring()