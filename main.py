import os # used for clearing the terminal screen so can have more of an app feel
import subprocess # used as part of clearing the terminal screen
import random

# Completed - feels like viewing stats should not lose you a turn need to read specs
# Need to add heal per character class
# Need to add clear text so game looks cleaner on terminal and maybe display permanent stats at top? Check spec
# Have defeated message and try again? Create printed skull with #'s or lines?
# Make attack messages specific for class i.e. spells or weapons? check spec - I learned about this in OOP it is one of the principles which one?
# add two special abilities to each character
# need to randomize the attack damage by all characters within a range of that characters base attack power
# Add special victory message for players

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        random_factor = random.randrange(0.5,1.10,0.5) # issue with this right now saying float cannot be int i am guessing this combo of random.randrange..conflicts?
        print(random_factor)
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=20)
    
    def evade_attack(self):
        # evades the next attack
        pass
    
    def quick_shot(self):
        # double attack but has a cooldown of X turns
        pass


class Paladin(Character):
    def __init__(self, name):
        super().init__(name, health = 150, attack_power=20)

    def Holy_Strike(self):
        #applies bonus damage to attack
        pass
    
    def Divine_Shield(self):
        #blocks next attack but has cooldown of X turns
        pass

def clear_screen():
    """Clears the terminal for user accessibility and aesthetics of the program"""
    subprocess.run('cls' if os.name =='nt' else 'clear', shell=True)

### Main Game ###

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        clear_screen()
        
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            pass  # Implement special abilities
        elif choice == '3':
            pass  # Implement heal method
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")


        # if statement that triggers wizard action unless user wants to display stats of character. Doesn't count as in game action.
        if wizard.health > 0 and choice != '4':
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
       print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
