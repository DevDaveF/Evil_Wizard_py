import os # used for clearing the terminal screen so can have more of an app feel
import subprocess # used as part of clearing the terminal screen
import random

# Completed - feels like viewing stats should not lose you a turn need to read specs
# Completed - Add healing mechanic that does not go over max health
# Completed - Health regenertion below 15 saying they had 0 health regen which is false...
# Completed - Prevent player from heal action if fully healed and cycle back to turn without triggering wizard attack
# Completed - Dark wizard health can go over max, check is this against requirements?
# Completed - Added a victory message for the player.
# Completed - How pass special attribute through parent class? Need to create a special ability method in parent that takes child class abilities. Would that use super()?
# Completed - Make Paladin divine shield
# add type commentary through code
# refactor code once counting where use same code multiple times turn into function
# Completed - Ways to do this - wizard attack power 0 until end of turn
# Completed - change control flow for wiard if so if divine shield active flips a bool which flips at end of turn
# Outstanding - Need to add clear text so game looks cleaner on terminal and maybe display permanent stats at top? Check spec
# Completed - Have defeated message and try again? Create printed skull with #'s or lines?
# Completed - Make attack messages specific for class i.e. spells or weapons? check spec - I learned about this in OOP it is one of the principles which one?
# Completed - add two special abilities to each character
# Completed - need to randomize the attack damage by all characters within a range of that characters base attack power
# Completed - issue with player health becoming giant float #
# Completed - need to make sure heal implements
# Completed - Not needed Need to add cooldown mechanic for two special abilities tracked through game. Perhaps counter in loop that resets
# Completed - fix up some screen clearing at load of game and in navigation
# Completed - get special ability activating
# Completed - keep attack power evil wizard going below zero on enfeeblement?
# Outstanding - message on health at max did not happen randomly for mage?
# Completed - dark wizard should heal when doing attacks for special abilities of heros i.e paladin divine shield

# Completed - Add try except and while loop to 3 other classes for special attributes
# Outstanding - Refactor while try except as a function rather than have all the code retyped multiple times :)
# Make character icon that goes over their turn menu for their chosen character type
# add animation for each special ability

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        random_factor = round(random.uniform(0.44,1.16),2) # issue with this right now saying float cannot be int i am guessing this combo of random.randrange..conflicts?
        attack_damage = round(self.attack_power * random_factor,2)
        print("random factor of: ",random_factor)
        print("attack damage is: ", attack_damage)
        opponent.health -= attack_damage
        print(f"{self.name} attacks {opponent.name} for {attack_damage} damage!")
        if opponent.health <= 0:
            print(f"\n{opponent.name} has been defeated!")
    
    def special_ability(self, opponent):
        pass
    
    def heal_mechanic(self):
        # Prevents a heal from occurring if health is = to max health
        if self.health < self.max_health:
            # Prevents a heal from pushing player health over max
            if (self.max_health - self.health) > 15:
                self.health += 15
                print(f"{self.name} heals 15 health! Current health: {round(self.health,2)}")
            else:# if player health within less than 15 health, heals difference between max and player health ensuring does not go over max health
                healing_value = round(self.max_health - self.health,2)
                self.health += healing_value
                print(f"{self.name} heals {healing_value} health! Current health: {round(self.health,2)}")

            
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {round(self.health,2)}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    
    def two_hand_strike(self,opponent):
        print("""\n
           __
        ,. |_'.
       / / /:\ )
     _/_/_/::: |
    /o_'/o>::/ /
    / /'/:::/ /
   / /_/::.'_/ 
  / / \__.-'
 / /
/ /
 /  
 \n""")
        print(f"{self.name} takes both hands and wraps them around their weapon's hilt as they heave a mighty swing at the wizard.")
        self.attack_power = 35
        self.attack(opponent)
        self.attack_power = 25
            
    def berserger_rage(self,opponent):
        print("""\n
              
⠄⠠⢀⠂⡐⡀⠂⠀⠐⠁⠈⠓⢊⣟⠆⡠⢂⡔⡠⠤⣉⢁⠌⠒⠉⢦⠱⢌⢆⡰⢄⡐⠡⢀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠡
⠀⢀⠀⠂⠐⣀⠆⠀⡀⢤⢠⡐⠦⡘⢤⢂⡒⢬⠱⣈⠥⠓⡬⢘⠌⣃⠣⠄⡌⣈⠒⠄⡣⠔⠐⠀⡀⢀⠁⠀⠀⠀⠒⠀⠀⠀
⠀⠀⠀⠀⡎⠌⡀⢦⡙⢤⢃⡜⠢⢍⡒⢬⡐⠣⠜⡰⢌⠳⡘⢀⡚⢄⡓⠬⣐⠢⠔⡂⡀⠀⠦⢡⠄⡀⠔⡀⠠⠀⠄⠀⠀⡀
⠀⠀⠀⠰⢂⡜⡘⢦⡘⠦⡡⢌⡓⡌⢲⠡⠜⣡⢋⠔⠃⠨⠅⠀⡜⢢⠜⡒⢤⢃⠝⠰⡑⢆⠄⠃⢎⡱⣀⠀⠂⢀⠀⠀⠀⠈
⠀⠀⠀⠰⡰⢌⡱⢢⡑⢎⡑⢢⠜⡌⠡⡒⢤⡀⠉⠘⡄⡨⠅⠀⢌⠣⢎⡱⠊⠀⠀⠀⢀⣀⠈⠀⠈⠐⢥⢂⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠰⣡⠣⡜⣡⠚⡤⡙⢆⠳⡌⠀⠀⢣⠜⣡⠄⠐⢡⢣⠀⠈⠉⠂⠀⠀⠀⣴⡞⣡⠨⠹⣷⣄⠀⠀⠣⣜⢡⠀⠀⠀⠀
⠀⠀⠀⠰⣡⠓⡜⢤⢋⠴⣉⢎⡱⠀⣠⢊⠅⠎⠱⠈⠀⠈⡀⠉⠀⠀⠀⠀⠀⣼⣿⣷⣤⣤⡾⠿⠿⢃⠀⠆⠘⡠⠱⠐⠂⠀
⠀⠀⠀⠰⣡⢋⡜⢢⢍⢲⠡⢎⠲⠉⠂⠁⠈⠀⠉⠀⠀⠀⢆⢲⠩⣍⢢⠀⡄⠍⠉⠉⠉⠁⠀⠀⠈⠚⢄⠙⢢⠀⢪⠅⡠⢁
⠀⠀⠀⠐⣥⠚⣌⢇⡚⠬⠙⠈⣀⣀⣀⠀⠀⠀⠀⡸⠀⠠⢎⠥⡓⡌⢆⡣⠀⢒⠤⣂⠤⠡⡄⠀⠀⠀⠈⢂⠡⢓⠄⢫⠰⡌
⠀⠀⠀⠐⡬⡙⢆⠊⠀⣠⡖⠋⠛⢻⣿⣿⣷⠀⠡⢥⡁⡘⣌⠲⡱⢌⡣⢜⣡⠈⠒⡥⢚⡱⢌⡣⢆⡄⣀⠀⠂⢉⠲⡀⢉⠔
⠀⠀⠀⠀⡜⡍⠀⠀⣼⣽⡐⠅⢔⣼⣿⠟⠁⠀⢠⡒⠱⡱⢌⣣⠱⣊⡔⢣⠦⡙⡄⢈⠱⡘⢦⡑⢎⠴⣃⠦⠀⠀⢣⠱⡈⢚
⠀⠀⠀⠀⠈⠀⢠⢠⣿⣿⣿⡿⠛⡋⠁⠀⠀⡠⠇⡀⢧⠱⣣⠀⠣⡱⠈⠑⠊⡑⠩⠐⠀⠉⠦⡙⢎⠖⡱⢪⠥⡀⠀⠓⡤⠡
⠀⠀⠀⠀⠠⢂⠃⠼⠋⠁⠀⠂⠹⠀⠀⠀⠈⠁⡰⢜⠪⡕⢦⠀⠀⠁⠀⠀⠀⠉⠀⠀⠀⠀⠰⣐⢆⠦⡉⠳⡸⢔⡀⠀⢲⡀
⠀⠀⠀⠀⠀⢨⢇⡣⠀⠀⠀⠀⡸⢀⣀⠠⢀⠦⣙⠬⢣⡝⠲⠀⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⡰⠍⠊⠀⡑⢂⠱⣩⠒⡄⠀⢆
⠀⠀⠀⠀⠀⣚⠼⡰⢄⡀⠀⠀⡅⠲⣌⠳⣌⠲⣉⠮⣑⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⡴⢐⠀⢡⠐⡹⣘⡄⠈
⠀⠀⠀⠀⠀⠙⢦⡓⣜⢣⠀⠀⡁⢆⡙⢦⡙⢦⡙⠴⠋⠀⠀⢀⣀⡀⣀⢀⠤⠠⠤⠀⠀⠀⠀⠀⢀⣵⡜⠠⠘⣄⠣⢭⠱⡀
⠀⠀⠀⠀⠀⠀⢣⠞⡤⢣⢂⠀⠁⢢⡙⢦⡘⠦⡙⠌⢀⡔⡊⠃⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣴⣿⡞⠿⠃⠀⠈⢖⡀⢫⠘⡅
⠀⠀⠀⠀⠀⠀⠀⢏⡴⢣⠍⣆⠀⢰⡉⢦⡙⠦⡍⢀⠖⡜⠀⠀⠀⡀⠀⣰⣾⣦⡸⣿⣿⠎⠛⠉⠀⠀⠀⠀⠀⠸⣄⠰⡈⠆
⠀⠀⠀⠀⠀⠀⠀⠘⣒⠧⣚⠬⠂⠀⡝⠀⣎⢱⠂⣌⢠⠃⢀⣀⡀⣷⣶⡎⠛⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢜⡂⠅⣣
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠻⣤⢳⡀⠀⠀⠀⠸⣬⠁⡆⢠⠁⡸⢿⡿⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠰⣒
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠣⡽⡀⠀⠀⠀⠶⠘⡜⠠⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠩⣖⣄⠈⠆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⡄⠀⠀⠈⢣⠘⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡓⠆⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⢣⠡⠀⢪⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣬⢳⣄⠐
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠡⠀⣫⠀⡄⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣴⣶⢹⣿⡇⡟⢈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⢁⠰⢣⡰⣫⢆⠀⠀⠀⠀⠀⡀⣴⣷⡜⣿⡷⠙⠻⠂⠉⠀⠀⡠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠈⠣⠵⢀⠫⣒⢀⡄⣾⣿⡷⢻⠟⠁⢉⡠⢔⡰⢪⡕⠲⠌⠡
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠱⣉⠘⣿⠜⠛⠀⢀⡰⣌⠧⠱⠊⠁⠀⡠⠂⢉⡈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⢤⣠⢠⡜⡣⠓⠀⠀⠀⠀⢀⠠⡐⠤⢣⠜
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢀⠐⡜⢢⢃⡝⢌⡁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⢆⡹⢌⠱⠊⠐⠀⡀⣁
\n""")
        self.health -= 25
        print(f"\n{self.name} carves a gash into their leg, losing 25 health with total health now at {self.health}.\nThey then let out a mighty ROAARRR and charge the wizard like a feral animal.\n")
        self.attack_power = 45
        self.attack(opponent)
        self.attack_power = 25
        
    def special_ability(self,opponent):
        ability_prompt = ("\nCall upon the spirits of your ancestors and:\n 1. Crush the wizard with a two handed strike!\n 2. Increase damage through a Berserker rage! \n")
        
        ability_triggered = valid_ability_input(ability_prompt)
                     
        clear_screen()
        
        if ability_triggered == 1:  
            self.two_hand_strike(opponent)              
        elif ability_triggered == 2:
            self.berserger_rage(opponent)


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def over_cast(self,opponent):
        #Increases attack damage but takes a large chunk of life
        self.health -= 50
        print("""\n\n                        .           .
                           o       '   o  .     '   . O
                        '   .   ' .   _____  '    .      .
                         .     .   .mMMMMMMMm.  '  o  '   .
                       '   .     .MMXXXXXXXXXMM.    .   ' 
                      .       . /XX77:::::::77XXX .   .   .
                         o  .  ;X7:::''''''':::7X;   .  '
                        '    . |::'.:'        '::| .   .  .
                           .   ;:.:.            :;. o   .
                        '     . '.:            /.    '   .
                           .     `.':.        .'.  '    .
                         '   . '  .`-._____.-'   .  . '  .
                          ' o   '  .   O   .   '  o    '
                           . ' .  ' . '  ' O   . '  '   '
                            . .   '    '  .  '   . '  '
                             . .'..' . ' ' . . '.  . '
                              `.':.'        ':'.'.'
                                `\\_  |     _//'
                                  \(  |\    )/
                                  //\ |_\  /\\
                                 (/ /\(" )/\ \)
                                  \/\ (  ) /\/
                                     |(  )|
                                     | '' |
                                     |  ' |
                                     |  ' |
                                     |      |
                                     |        `.__,
                                     \_________.
                                     """)
        print(f"\n\n\n{self.name} calls out in a dread language which pierces the air with a wail.\n{self.name} bleeds from their eyes, ears and nose creating a glowing orb of blood suspended above their head.\nThey lose 50 health bringing their total to {round(self.health)}.\nThe air cracks and horrible screams and gnashing of teeth is heard.\nThe orb streaks away and strikes the Evil Wizard causing them to cry out in agaony!\n")
        self.attack_power = 70
        self.attack(opponent)
        self.attack_power = 35

    def enfeeblement(self,opponent):
        #permanently weakens wizard attack power by 1 each time
        print("""\n\n
                  _________-----_____
       _____------           __      ----_
___----             ___------              )
   ----________        ----                 )
               -----__    |             _____)
                    __-                /     |
        _______-----    ___--          \    /)}
  ------_______      ---____            \__/  /
               -----__    \ --    _          /}
                      --__--__     \_____/   \_/|
                              ----|   /          |
                                  |  |___________|
                                  |  | ((_(_)| )_)
                                  |  \_((_(_)|/(_)
                                  \             (
                                   \_____________)

""")
        print(f"\n\n\n{self.name} points at the wizard and utters a curse in a long dead language.\nA burning skull forms in the air and begins screaming.\nIt streaks into the Evil Wizard letting out a piercing scream.\nThe Evil Wizard slightly staggers and turns a shade paler.\n")
        if opponent.attack_power > 5:
            opponent.attack_power -= 1
            print("Evil wizard attack power is: ", opponent.attack_power)
        else:
            print("The Evil wizard cannot be further weakend and has an attack power of: ", opponent.attack_power)

    def special_ability(self,opponent):
        ability_prompt = (f"\n {self.name} opens their dread grimoire and:\n 1. Use their life force to cast a mighty spell!\n 2. Permanently enfeeble the the Evil Wizard! \n")
        
        ability_triggered = valid_ability_input(ability_prompt)
        
        clear_screen()
        
        if ability_triggered == 1:  
            self.over_cast(opponent)              
        elif ability_triggered == 2:
            self.enfeeblement(opponent)
        
        
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        # prevents wizard from regenerating over max health
        if self.health < self.max_health:
            # heals 5 health if wizard has a health value more than 5 lower than max health value 
            if (self.max_health - self.health) > 5:
                self.health += 5
                print(f"{self.name} regenerates 5 health! Current health: {self.health} and attack power of {self.attack_power}")
            else:# heals a value that is 5 or less health value off of max health value
                healing_value = round(self.max_health - self.health,2)
                self.health += healing_value
                print(f"{self.name} regenerates {healing_value} health! Current health: {round(self.health,2)} and attack power of {self.attack_power}")
        
class Archer(Character):
    def __init__(self, name, hit_chance):
        super().__init__(name, health=125, attack_power=25)
        
        self.hit_chance = hit_chance
    
    def shoot_and_scoot(self,opponent):
        # reduced attack for chance to evade wizard attack
        print("""\n
         ⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡀⠀⠀⠀⠀⠀⣾⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⢃⣄⠀⠀⠀⠀⠘⠿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠃⠀⠀⠀⠀⠀⠈⣩⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣴⣶⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀
        \n""")
        wizard_attack_miss = "False"
        self.attack_power = 10
        self.attack(opponent)
        self.attack_power = 20
        print("wizard hit chance of: ",self.hit_chance)
        
        if self.hit_chance < 50:
            wizard_attack_miss = "miss attack"
            print(f"The Evil Wizard magical attack misses {self.name}!")
            return wizard_attack_miss
    
    def quick_shot(self,opponent):
        print("""\n
            4$$-.
           4   ".
           4    ^.
           4     $
           4     'b
           4      "b.
           4        $
           4        $r
           4        $F           --------   -$b========4========$b====*P=-
-$b========4========$b====*P=-
           4       *$$F                                                       ---------- -$b========4========$b====*P=-
           4        $$"
           4       .$F
           4       dP
           4      F
           4     @
           4    .
           J.
          '$$     Gilo94'
          \n""")
        # double attack but has a 35% chance of hitting
        print("quick shot hit chance of: ",self.hit_chance)
        
        if self.hit_chance > 50:
            print(f"{self.name} quick shot hits the mark!")
            self.attack(opponent)
            self.attack(opponent)
        else:
            print(f"{self.name} misses the wizard!")
    
    def special_ability(self,opponent):
        ability_prompt = (f"\n {self.name} surveys the field of battle and uses their speed to:\n 1. Shoot and Scoot!\n 2. Quick shot two arrows! \n")
        
        ability_triggered = valid_ability_input(ability_prompt)
        
        clear_screen()
        
        self.hit_chance = random.randint(1,100)
        
        if ability_triggered == 1:  
            return self.shoot_and_scoot(opponent)              
        elif ability_triggered == 2:
            self.quick_shot(opponent)

class Paladin(Character):
    def __init__(self, name, divine_favor):
        super().__init__(name, health = 150, attack_power=20)
        
        self.divine_favor = divine_favor

    def Divine_Shield(self,opponent):
        # potentially blocks wizard attack and heals paladin at the same time but could also injure him if not favored
        wizard_attack_miss = "False"
        
        if self.divine_favor > 1:
            print("""
                              __ ,..---.._
                            +''''`--''-..`--..__
                           .\ _,/:i--._`:-:+._`.``-._
                          /`.._,,' \   `-.``--:.b....=.
                         |`..__,,..`.    '`.__::i--.-::_
                         )- .....--i'\..      --+`'''-'
                       ,' .'.._,.-'|._-b}
                      /,'<'    V   `oi| \\             _.
                     |/ -|,--.." ,'-. ||\..      _.,;:'_<'
                     ''/ | <o> . <o>' |\||'\    /-'_/' `.
                    |,','|    , .    .-.|:.`.  + .,:..  |
                 ._,:'/ /-\   '^'   -Y"\\ |.| || /,+8d| |
                .|/,'| |/':: ':=:' ,'|  | | \\|| "+)='  |
                |+,';' /|_/ \     _/ \b':.\  \'| .||   ,'
                ,,:-i''_i' | ``-.Y',. ,|`: | \;- | |_,'
          __   |'| |i:'._ ,'     ,' ,; | |-)-'  __--:b__
         .P|   | |/,'|\  - ._   /  /   _,Y-   ,:/'  `.  `'".._
        ,'|| -','' | ._i._   `':| ,..,'     ,Y;'      \       `- ._
       |||||,..    | \ '-.._ _,' /       _,b-'         `.         '-.
       ||||P..i,  .| '....,-' _,'''''-'''               '    _,..    `)
       +'`   <'/  |`-.....---'                       ._         ,._
        |      |                                    ,'``,:-''''/,--`.
       Y|.b_,,:  |              ||                 ,;,Y'      /     |.
     ,' /'----' .'|   ..       |  |         '"   .`Y'     .,-b_....;;,.
    |+|,'     | | \.,  '      ,'  `:.  _     ,/__`     _=:  _,'``-
   / +,'      | /\_........:.'      '"----:::::'Y  .'.|   |||
   |' '      .'/- \\                          /'|| || |   |||
   |||      /|     \L                        /'|| ||/ |   |||
   `.|    ,'/       .|                      / ,'||/o;/    |||
     `..._,,         |                      |/|   '       |||
       ``-'          |                      |,            |||
                     |          ,.          |             |||
  ,=--------....     |          ""          |             |||
,/,'.            i=..+._             ,..    '..;---:::''- | |
'/|           __....b `-''`---....../.,Y'''''j:.,.._      | `._
.'      _.Y.-'       `..       ii:,'--------' |     :-+. .| | b}
|     .=_,.---'''''--...:..--:'  /         _..-----..:=   | | '|}
|    '-''`'---                  ---'_,,,--''           `,.. |  | \.
 \  .                      ,' _,--''        :dg:      _,/ |||   |  }
`::b\`                 _,-i,-'                 ,..---'    ,|:|  | _|
`'--.:-._      ____,,,;.,'' `--._      ''''''''           |'|' .'  '
     ``'--....Y''-'              `''--..._..____._____...,' |  'o-'
                                             `''''`'''i==_+=_=i__
                                                     ||'''- '    `.
                                                      `-.......-''
""")
            wizard_attack_miss = "miss attack"
            print(f"\nThe air grows heavy as {self.name} raises his eyes to the heavens.\nShouting a final desperate prayer {self.name}pleads for help.!\n The sky opens up and a trumpet sounds and {self.name} sees a smiling face in their minds eye.\n")
            divine_heal = self.divine_favor * 2
            self.health += divine_heal
            print(f"\n{self.name} is healed for {divine_heal} health bringing their health too {self.health}\n")
            print(f"The Evil Wizard's attack is blocked by an unseen hand!\n")
            return wizard_attack_miss
        else:
            print(f"{self.name} has been forsaken by the gods! {self.name}'s faith has been found lacking\n")
            divine_wrath = self.divine_favor * 2
            self.health += divine_wrath
            print(f"\n{self.name} is smited for {divine_wrath} health bringing their health too {self.health}\n")
            
    def Holy_Strike(self, opponent):
        print("""
                 .
                / '
                | |
                |.|
                |.|
                |:|      __
              ,_|:|_,   /  )
                (Oo    / _I_
                 +\ \  || __|
                   \ \ ||___|
                    \ / .:.\-]-}
                     \  |.:. /-----'
                        |___|::oOo::|
                        /   |:<_T_>:|
                        |_____\ ::: /
                        | |  \ \:/
                        | |   | |
                        \ /   | \__
                        / |   \____]
                        `-'
         \n""")
        self.attack_power = 40
        divine_cost = -15
        self.health += divine_cost
        print(f"{self.name} is favored by the heavens! Eyes glowing with an inner light {self.name}'s zeal audibly cracks the air!\n{self.name}'s spasms in pain losing {divine_cost} health for divine strength.")
        self.attack(opponent)
        self.attack_power = 20
        
    
    def special_ability(self,opponent):
        ability_prompt = (f"\n {self.name} summons their faith and zeal to:\n 1. Call upon divine protection and favor!\n 2. Strike with the might of the heavens!\n")
        
        ability_triggered = valid_ability_input(ability_prompt)
        
        clear_screen()
        self.divine_favor = random.randint(-10,10)
        
        if ability_triggered == 1:  
            return self.Divine_Shield(opponent)              
        elif ability_triggered == 2:
            self.Holy_Strike(opponent)

def clear_screen():
    """Clears the terminal for user accessibility and aesthetics of the program"""
    subprocess.run('cls' if os.name =='nt' else 'clear', shell=True)

def valid_ability_input(ability_menu):
    valid_ability = False
            
    while valid_ability == False:
        try:   
            ability_triggered = int(input(ability_menu))
            if ability_triggered == 1 or ability_triggered == 2:
                valid_ability = True
                return ability_triggered
            else:
                print("Enter valid response 1-2.")
        except ValueError:
            print("Enter valid response 1-2.")    
        


### Main Game ###

def create_character():
    clear_screen()
    
    print("""\n
.s5SSSs.                                                                                         .s5SSSs.                          
sS    SS. .s5SSSs.  .s5SSSs. .s5SSSs.  .s5SSSs.  .s5SSSSs.     .s5SSSSs. .s    s.  .s5SSSs.      SS.       .s    .s. .s. .s        
sS    S%S SS.       sS       SS.       SS.   SSS    SSS           S%S    Ss.   sS  sS            SS.       SS.   s&s S%S sS      
SS    S%S sS        sS       sS    `:; sS    S%S    S%S           S%S    sS    S%S sS            SS        sS    S%S S%S sS        
SS    S%S SSSs.ss   SSSs.    SSSs.     SSSs. S%S    S%S           S%S    SSSs. S%S SSSs.         SSSs.     SS    S%S S%S SS        
SS    S%S SS        SS       SS        SS    S%S    S%S           S%S    SS    S%S SS            SS         SS   S%S S%S SS        
SS    `:; SS        SS       SS        SS    `:;    `:;           `:;    SS    `:; SS            SS         SS   `:; `:; SS        
SS    ;,. SS    ;,. SS       SS    ;,. SS    ;,.    ;,.           ;,.    SS    ;,. SS    ;,.     SS    ;,.   SS  ;,. ;,. SS    ;,. 
;;;;;;;:' `:;;;;;:' :;       `:;;;;;:' :;    ;:'    ;:'           ;:'    :;    ;:' `:;;;;;:'     `:;;;;;:'    `:;;:' ;:' `:;;;;;:' 
                                                                                                                                   
                                                                                                                             
                           SS. SS. s.  .s5SSSSs. .s5SSSs.  .s5SSSs.  .s5SSSs.                                                      
                        sS S%S S%S SS.       SSS       SS.       SS.       SS.                                                     
                        SS S%S S%S S%S     sSSS  sS    S%S sS    S%S sS    S%S                                                     
                        SS S%S S%S S%S    sSS"   SSSs. S%S SS .sS;:' SS    S%S                                                     
                        SS S%S S%S S%S   sSS     SS    S%S SS    ;,  SS    S%S                                                     
                        SS `:; `:; `:;  sSS      SS    `:; SS    `:; SS    `:;                                                     
                        SS ;,. ;,. ;,. sSS       SS    ;,. SS    ;,. SS    ;,.                                                     
                        `:;;:'`::' ;:' `:;;;;;:' :;    ;:' `:    ;:' ;;;;;;;:'    \n""")
    
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    clear_screen()
    
    if class_choice == '1':
        return Warrior(name), class_choice
    elif class_choice == '2':
        return Mage(name), class_choice
    elif class_choice == '3':
        return Archer(name,0), class_choice
    elif class_choice == '4':
        return Paladin(name,0), class_choice
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard, class_choice):
    while wizard.health > 0 and player.health > 0:
        valid_response = False
        
        if class_choice == '1':
            print("""\n        
 [ZZZzzuuuuaaaAAAAAHHH!!!]
                                 /)
                                //
              __*_             //
           /-(____)           //
          ////- -|\          //
       ,____o% -,_          //
      /  \\   |||  ;       //
     /____\....::./\      //
    _/__/#\_ _,,_/--\    //
    /___/######## \/""-(\</
   _/__/ '#######  ""^(/</
 __/ /   ,)))=:=(,    //.
|,--\   /Q...... /.  (/
/       .Q....../..'
       /.Q ..../...'
      /......./.....'
      /...../  \.....'
      /_.._./   \..._'
       (` )      (` )
       | /        \ |
       '(          )'
      /+|          |+'
      |,/          \,/  b'ger
  \n""")
        elif class_choice == '2':
            print("""\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡰⠉⠀⠀⠉⠻⢦⡀⠀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠈⣶⣝⣺⢷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡗⠂⠀⠀⠀⠁⠐⠺⡌⠁⠈⠛⠂⠀⠀
⠀⠀⠀⢀⣠⠴⠚⠊⠉⠉⠁⠈⠉⠉⠑⠓⠦⣄⡀⠀⠀⠀
⢀⣴⣾⣭⡤⢤⣤⣄⣀⣀⣀⣀⣀⣀⣠⣤⡤⢤⣭⣷⣦⡀
⠈⢯⣿⡿⣁⡜⣨⠀⠷⣲⡞⢻⣖⠾⠀⡅⢳⣈⢿⣟⡽⠁
⠀⠀⠈⠙⡟⡜⣸⡀⠀⡅⠇⠘⠢⠀⢀⣇⢣⢻⠋⠁⠀⠀
⠀⠀⠀⠰⡾⡰⡏⠛⠚⠋⣉⣍⠙⠓⠛⢹⢆⢷⠆⠀⠀⠀
⠀⠀⠀⠀⢷⠡⢹⠒⢖⡬⠄⠀⢭⡲⠒⡏⠈⡾⠀⠀⠀⠀
⠀⠀⠀⠀⠸⢇⣏⣦⠀⠀⠀⠀⠀⠀⣴⣽⡼⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠈⠉⠻⣴⠀⠀⣤⠟⠁⠁⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀\n""")
        elif class_choice == '3':
            print("""\n 
                            ⢈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠎⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢀⣠⣴⣶⡶⠿⠿⠛⠛⠉⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠙⠶⢤⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⣰⣶⣮⡁⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⣘⡻⢿⣿⣦⣄⡉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢰⣿⡇⠀⠙⠻⣿⣿⣷⣦⡈⠑⠤⣀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⢿⣧⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣍⠲⢄⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
            ⠀⠈⢿⣧⠀⠀⠀⠀⠀⠈⠻⢟⢿⣿⣿⣇⣿⣷⣮⡙⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⢰⣶⣭⡳⣄⡀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣶⣿⣵⣶⣄⠀
            ⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠀⠁⢿⣿⣿⣿⣿⠏⣼⣿⣟⠿⠿⣿⣿⣿⣿⣿⣇
            ⠀⠀⠀⠀⡠⠗⠂⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⡿⠋⠀⠀⠀⠈⠉⠉⠉⠉
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣿⣄⠈⠙⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠛⠦⢄⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠈⢂⠀⠀⠀⠀⠀
            """)
        elif class_choice == '4':
            print("""
                           _____
            ,             /@@@@@=-
            \\            @@@@@@@@@@=-
             \\          _\@/\@@@@@=-
 Journey of...\\        /_ +\ \@@@@@=-
        ,      \\      (_/   )  \@@@@=-
        \\      \\     (_____)    \@@=-
        _\\_/\_ _\\__  /     \     ~~
  ____,/+-  `/\\  { \_|___(__ )
 >             \\  )_|/  ___  /
 \_/--\___/     \\.` / <-q-p-> /
    _//   )      \(\/\ <-d-b-> /___
 _____  /         \/ \  \|/  //   \__
 /     \/          /   \_____//     \_)
 | /\_  |         (_  /______\\     |||
 | \_ | |         | \|   <    \\    /||
 \_\_\ \/     ____\  |____\    \)  / ||
       /    _/  <____)\    (      / //\\
      /   _/           \    \    (  \\//
     (   /              )  / \    \  \/
     /  /              /  /   \    )
 ---/  / Faith.    ---/  /-----)  /-----
  _/__/  My Gods    _/__/     /  /
 /__/   Bless Me!  /__/     _/__/
                           /__/
                           """)
        
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        while valid_response == False:
            choice = input("Choose an action: ")
            if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                valid_response = True
            else:
                print("Enter valid response 1-4.")
            
        
        wizard_skip_turn = 0
        wizard_only_regen = 0
        ability_trigger = ""
        
        clear_screen()
        
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            ability_trigger = player.special_ability(wizard)
            if ability_trigger == "miss attack":
               wizard_skip_turn = 1
               wizard_only_regen = 1
                
        elif choice == '3':
            if player.health == player.max_health:
                print(f"{player.name} has full health and cannot heal. Please choose another action.")
                wizard_skip_turn = 1
            else:
                player.heal_mechanic()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")


        # if statement that triggers wizard action unless user wants to display stats of character. Doesn't count as in game action.
        if wizard.health > 0 and choice != '4' and wizard_skip_turn != 1: # "and not no_damage"
            wizard.regenerate()
            wizard.attack(player)
        
        # used to create a missed attack by the wizard however he still does regen
        if wizard.health > 0 and choice != '4' and wizard_only_regen == 1:
            wizard.regenerate()
            

        if player.health <= 0:
            print(f"""\n                     
                               /|
                              / |                 
                             /  |
                            /   |
                           |    |
                         --:'''':--
                           :'_' :
                           _:"":\___
            ' '      ____.' :::     '._
           . *=====<<=)           \    :
            .  '      '-'-'\_      /'._.'
                             \====:_ ""
                            .'     //
                           :       :
                          /   :    /
                         :   .      '.
         ,. _            :  : :      :
      '-'    ).          :__:-:__.;--'
    (        '  )        '-'   '-'
 ( -   .00.   - _
(    .'  _ )     )
'-  ()_.\,\,   -")\n
\n
Evil wins...today...\n""")

    if wizard.health <= 0:
       print(f"""  
  _   _   _   _   _
 | | | | | | | | | |
 | |_| |_| |_| |_| |
 |                 |
 |  _   _   _   _  |
 | | | | | | | | | |
 | |_| |_| |_| |_| |
 |                 |
 |    |  ___  |    |
 |    | |   | |    |
 |    | |   | |    |
 |    | |   | |    |
 |    | |___| |    |
 |    |       |    |
 |____|_______|____|
\n The realm is at peace once more...\n""")

def main():
    player,class_choice = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard, class_choice)

if __name__ == "__main__":
    main()
