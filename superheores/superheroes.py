from random import randint
import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
         '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()

        self.armors = list()
        self.deaths = 0
        self.kills = 0
        self.defence = 0


    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
        pass
    def add_weapon(self, weapon):
        '''
        This method will append the weapon object passed in as an argument to the list of abilities that already exists -- self.abilities.

        This means that self.abilities will be a list of abilities and weapons.
        '''
        self.abilities.append(weapon)

    def add_armor(self, armor):
        ''' Add ability to abilities list '''
        self.armors.append(armor)
        self.defence = 0
        for armor in self.armors:
            self.defence += armor.block()
        pass

    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
            print("{} is adding {} damage".format(self.name, damage))
        print("{} is attacking with attack power of {}".format(self.name, damage))
        return damage

    def take_damage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        if self.defence > 0:
            print("{} has armor".format(self.name))
            self.defence -= damage
            if self.defence < 0:
                print("Pierced throught block. Current defence: ", self.defence)
                pierceDamage = self.defence * -1
                self.current_health -= pierceDamage
        else:
            self.current_health -= damage
            print("{} has no armor".format(self.name))
        pass

    def is_alive(self):
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        print("fighting!")
        while self.is_alive() == True and opponent.is_alive() == True:
          opponent.take_damage(self.attack())
          self.take_damage(opponent.attack())
          print("{}'s health is: ".format(self.name), self.current_health)
          print("{}'s health is: ".format(opponent.name), opponent.current_health)

        if self.is_alive() == False:
            self.deaths += 1
            opponent.kills += 1
            print("{} died".format(self.name))


        if opponent.is_alive() == False:
            opponent.deaths += 1
            self.kills += 1
            print("{} died. He has {} deaths.".format(opponent.name, opponent.deaths))


class Ability:
    def __init__(self, name, attackStrenght):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        self.name = name
        self.attackStrenght = attackStrenght

    def attack(self):
        '''
        Return a random attack value
        between 0 and attackStrenght.
        '''
        damage = randint(0, self.attackStrenght)
        print("ability attack damage: ",damage, " by ", self.name)
        return damage

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between one half to the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        damage = randint((self.attackStrenght / 2), self.attackStrenght)
        print("Weapon damage",damage)
        return damage

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        defence = randint(0, self.max_block)
        return defence

class Team:
    def __init__(self, team_name):
        '''Instantiate resources.'''
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(Hero)
        pass

    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if hero == name:
                self.heroes.remove(hero)
        pass

    def view_all_heroes(self):
        '''Print out all heroes to the console.'''
        for hero in self.heroes:
            print("team member: ",hero.name)

    def attack(self, other_team):
        '''
        This function should randomly select a living hero from each team and have them fight until one or both teams have no surviving heroes.

        Hint: Use the fight method in the Hero class.
        '''
        # TODO: Fix, it doesn't work in 1V1
        randomTeamHero = Hero(name="")
        heroesHasAliveMembers = True
        randomTeamEnemy = Hero(name="")
        villainsHaveAliveMembers = True
        canFight = True
        while canFight == True:
            for hero in self.heroes:
                if hero.is_alive() == True:
                    randomTeamHero = hero
                    heroesHasAliveMembers = True
                else:
                    heroesHasAliveMembers = False
            for villain in other_team.heroes:
                if villain.is_alive() == True:
                    randomTeamEnemy = villain
                    villainsHaveAliveMembers = True
                else:
                    villainsHaveAliveMembers = False
            if villainsHaveAliveMembers == False:
                print("{} team has won!".format(self.name))
                canFight = False
            if heroesHasAliveMembers == False:
                print("{} team has won!".format(other_team.name))
                canFight = False
            print("{} against {}".format(randomTeamHero.name, randomTeamEnemy.name))
            if canFight == True:
                randomTeamHero.fight(randomTeamEnemy)
        pass

    def revive_heroes(self, health=100):
        '''
        This method should reset all heroes health to their
        original starting value.
        '''
        for hero in self.heroes:
            if health == 100:
                print("{} is being revived. His health is going back to: {}".format(hero.name, hero.starting_health))
                hero.current_health = hero.starting_health
            else:
                print("{} is being revived. His health is going to: {}".format(hero.name, health))
                hero.current_health = health


        pass

    def stats(self):
        '''
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the console.
        '''
        for hero in self.heroes:
            print("{}   Deaths: {}    Kills: {}".format(hero.name, hero.deaths, hero.kills))
        pass

class Arena:
    def __init__(self):
        '''
        Declare variables
        '''
        teamOne = input("Name of first team: ")
        teamTwo = input("Name of second team: ")
        # TODO: Need to add more verifying of input
        if teamOne is not None and teamTwo is not None:
            self.team_one = Team(str(teamOne))
            self.team_two = Team(str(teamTwo))
            print("{} vs {}".format(self.team_one.name, self.team_two.name))
    def create_ability(self):
        '''
        This method will allow a user to create an ability.

        Prompt the user for the necessary information to create a new ability object.

        return the new ability object.
        '''
        abilityInputName = input("Name of ability: ")
        abilityInputDamage = input("{}'s damage: ".format(abilityInputName))

        ability = Ability(name=abilityInputName, attackStrenght=int(abilityInputDamage))
        print("Your new ability: [name: {}    damage: {}]".format(ability.name, ability.attackStrenght))
        return ability

    def create_weapon(self):
        '''
        This method will allow a user to create a weapon.

        Prompt the user for the necessary information to create a new weapon object.

        return the new weapon object.
        '''
        weaponInputName = input("Name of weapon: ")
        weaponInputDamage = input("{}'s damage: ".format(weaponInputName))

        weapon = Weapon(name=weaponInputName, attackStrenght=int(weaponInputDamage))
        print("Your new weapon: [name: {}    damage: {}]".format(weapon.name, weapon.attackStrenght))
        return weapon

    def create_armor(self):
        '''
        This method will allow a user to create a piece of armor.

        Prompt the user for the necessary information to create a new armor object.

        return the new armor object.
        '''
        armorInputName = input("Name of armor: ")
        armorInputDamage = input("{}'s damage: ".format(armorInputName))

        armor = Armor(name=armorInputName, max_block=int(armorInputDamage))
        print("Your new armor: [name: {}    damage: {}]".format(armor.name, armor.max_block))
        return armor


    def create_hero(self):
        '''
        This method should allow a user to create a hero.

        User should be able to specify if they want armors, weapons, and abilites. Call the methods you made above and use the return values to build your hero.

        return the new hero object
        '''
        heroName = input("Name of hero: ")
        heroHealth = int(input("{}'s health: ".format(heroName)))
        hero = Hero(name=heroName, starting_health=heroHealth)

        addPower = ""
        while addPower != 0:
            addPower = input("(W) if you want to add a weapon\n(A) if you want to add an ability\n(D) if you want to add armor\n(Anything else) if you want to finish hero: ")
            addPower = str(addPower).upper()
            if addPower == "W":
                hero.add_weapon(self.create_weapon())
                print("Added weapon to hero")
            elif addPower == "A":
                hero.add_ability(self.create_ability())
                print("Added ability to hero")
            elif addPower == "D":
                hero.add_armor(self.create_armor())
                print("Added armor to hero")
            else:
                print("Finished making hero")
                addPower = 0
        return hero

    def build_team_one(self):
        '''
        This method should allow a user to create team one.
        Prompt the user for the number of Heroes on team one and
        call self.create_hero() for every hero that the user wants to add to team one.

        Add the created hero to team one.
        '''
        teamMembers = input("Number of members for {} team: ".format(self.team_one.name))
        teamMembers = int(teamMembers)
        while teamMembers != 0:
            print("Team members left to create: ", teamMembers)
            self.team_one.add_hero(self.create_hero())
            teamMembers -= 1
            self.team_one.view_all_heroes()

    def build_team_two(self):
        '''
        This method should allow a user to create team two.
        Prompt the user for the number of Heroes on team two and
        call self.create_hero() for every hero that the user wants to add to team two.

        Add the created hero to team two.
        '''
        teamMembers = input("Number of members for {} team: ".format(self.team_two.name))
        teamMembers = int(teamMembers)
        while teamMembers != 0:
            print("Team members left to create: ", teamMembers)
            self.team_two.add_hero(self.create_hero())
            teamMembers -= 1
            self.team_two.view_all_heroes()

    def team_battle(self):
        '''
        This method should battle the teams together.
        Call the attack method that exists in your team objects to do that battle functionality.
        '''
        self.team_one.attack(other_team=self.team_two)


    def show_stats(self):
        '''
        This method should print out battle statistics
        including each team's average kill/death ratio.

        Required Stats:
        Declare winning team
        Show both teams average kill/death ratio.
        Show surviving heroes.
        '''
        numberOfKills_team_one = list()
        numberOfKills_team_two = list()

        numberOfDeaths_team_one = list()
        numberOfDeaths_team_two = list()

        team_one_alive_heores = list()
        team_two_alive_heroes = list()

        for hero in self.team_one.heroes:
            if hero.is_alive() == True:
                team_one_alive_heores.append(hero)
            numberOfKills_team_one.append(hero.kills)
            numberOfDeaths_team_one.append(hero.deaths)
        for villain in self.team_two.heroes:
            if villain.is_alive() == True:
                team_two_alive_heroes.append(villain)
            numberOfKills_team_two.append(villain.kills)
            numberOfDeaths_team_two.append(villain.deaths)

        team_one_averageDeaths = sum(numberOfDeaths_team_one) / float(len(numberOfDeaths_team_one))
        team_two_averageDeaths = sum(numberOfDeaths_team_two) / float(len(numberOfDeaths_team_two))

        team_one_averageKills = sum(numberOfKills_team_one) / float(len(numberOfKills_team_one))
        team_two_averageKills = sum(numberOfKills_team_two) / float(len(numberOfKills_team_two))

        for i in team_one_alive_heores:
            print("{}'s alive member: {}".format(self.team_one.name, i.name))
        for i in team_two_alive_heroes:
            print("{}'s alive member: {}".format(self.team_two.name, i.name))

        print("{}'s Kills: {}   Deaths: {}\n{}'s Kills:{}   Deaths: {}".format(self.team_one.name,team_one_averageKills, team_one_averageDeaths, self.team_two.name, team_two_averageKills, team_two_averageDeaths))

if __name__ == "__main__":
    # arena = Arena()
    # arena.build_team_one()
    # arena.build_team_two()
    # if len(arena.team_one.heroes) > 0 and len(arena.team_two.heroes) > 0:
    #     arena.team_battle()
    # arena.show_stats()


    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
