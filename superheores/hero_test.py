import superheroes


# Testing Hero class
def test_hero_kills_and_deaths():
    batman = superheroes.Hero("Batman")
    batmanAbility = superheroes.Ability("Detective", 100)
    batman.add_ability(batmanAbility)
    superman = superheroes.Hero("Superman")
    batman.fight(superman)
    assert (batman.kills == 1 and batman.deaths == 0) and (superman.kills == 0 and superman.deaths == 1)

def test_hero_add_ability():
    batman = superheroes.Hero("Batman")
    batmanAbility = superheroes.Ability("Detective", 10)
    batman.add_ability(batmanAbility)
    damage = batman.attack()
    assert (damage > -1 and damage < 11)

def test_hero_add_armor():
    batman = superheroes.Hero("Batman")
    batsuit = superheroes.Armor("Bat Suit", 1)
    batman.add_armor(batsuit)
    defence = batman.defence
    assert (defence > -1 and defence < 2)

def test_hero_attack():
    batman = superheroes.Hero("Batman")
    damage = batman.attack()
    assert damage == 0

def test_hero_take_damage():
    batman = superheroes.Hero("Batman")
    batman.take_damage(50)
    assert batman.current_health == 50

def test_hero_take_damage_with_armor():
    batman = superheroes.Hero("Batman")
    batsuit = superheroes.Armor("Bat Suit", 1)
    batman.add_armor(batsuit)
    batman.take_damage(50)
    assert (batman.current_health == 51 or batman.current_health == 50)

def test_hero_death():
    batman = superheroes.Hero("Batman")
    batman.take_damage(100)
    assert batman.is_alive() == False

def test_hero_fight():
    batman = superheroes.Hero("Batman")
    batmanAbility = superheroes.Ability("Detective", 100)
    batman.add_ability(batmanAbility)
    superman = superheroes.Hero("Superman")
    batman.fight(superman)

    catwoman = superheroes.Hero("Cat Woman")
    captainmarvel = superheroes.Hero("Captain Marvel")
    catwomanAbility = superheroes.Ability("Meow", 100)
    catwoman.add_ability(catwomanAbility)
    captainmarvel.fight(catwoman)
    assert (superman.is_alive() == False and captainmarvel.is_alive() == False)


# Testing Ability class
def test_ability_attack():
    batmanAbility = superheroes.Ability("Detective", 100)
    damage = batmanAbility.attack()
    assert (damage > -1 and damage < 101)

# Testing Weapon class
def test_weapon_attack():
    batmanAbility = superheroes.Weapon("Detective", 2)
    damage = batmanAbility.attack()
    assert (damage > 0 and damage < 3)

# Testing Team class
def test_team_count():
    batman = superheroes.Hero("Batman")
    superman = superheroes.Hero("Superman")
    justiceLeague = superheroes.Team("Justice League")

    justiceLeague.add_hero(batman)
    justiceLeague.add_hero(superman)
    justiceLeague.remove_hero(superman)
    assert len(justiceLeague.heroes) == 1

# TODO: Gonna have to update this attack test.
def test_team_attack():
    batman = superheroes.Hero("Batman")
    batAttack= superheroes.Ability("batPunch", attackStrenght=100)
    batman.add_ability(batAttack)
    batsuit = superheroes.Armor("Bat Suit", 1)
    batman.add_armor(batsuit)

    superman = superheroes.Hero("Superman")
    justiceLeague = superheroes.Team("League")
    evilLeague = superheroes.Team("Evil League")

    justiceLeague.add_hero(batman)
    evilLeague.add_hero(superman)
    justiceLeague.attack(evilLeague)
    assert superman.kills == 0 and superman.deaths == 1 and batman.kills == 1 and batman.deaths == 0

def test_team_revive_heroes():
    batman = superheroes.Hero("Batman")
    batAttack= superheroes.Ability("batPunch", attackStrenght=100)
    batman.add_ability(batAttack)
    batsuit = superheroes.Armor("Bat Suit", 1)
    batman.add_armor(batsuit)
    superman = superheroes.Hero("Superman")
    justiceLeague = superheroes.Team("League")
    evilLeague = superheroes.Team("Evil League")
    justiceLeague.add_hero(batman)
    evilLeague.add_hero(superman)
    justiceLeague.attack(evilLeague)
    evilLeague.revive_heroes()
    justiceLeague.revive_heroes(300)
    assert superman.current_health == 100 and batman.current_health == 300

# Test Armor class
def test_armor_block():
    shield = superheroes.Armor("Shield", 5)
    block = shield.block()
    assert (-1 < block < 6)
