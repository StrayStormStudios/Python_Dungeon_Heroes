from hero import Hero

def test_hero_name():
    hero = Hero("test")
    assert hero.name == "test"

#life stats
def test_hero_health():
    hero = Hero("health")
    assert hero.health == 100
    assert hero.max_health == hero.health

    hero.set_health(70)
    assert hero.health == 70
    hero.set_health(50)
    assert hero.health == 50
    hero.set_health(20)
    assert hero.health == 20
    hero.set_health(10)
    assert hero.health == 10

def test_hero_stamina():
    hero = Hero("stamina")
    assert hero.stamina == 50
    assert hero.max_stamina == hero.stamina

def test_hero_food():
    hero = Hero("food")
    assert hero.max_food == 63
    assert hero.food == hero.max_food

def test_hero_gold():
    hero = Hero("gold")
    assert hero.gold == 0

#attack attributes
def test_hero_attack():
    hero = Hero("attack")
    assert hero.attack == 2
    assert hero.strength == 0

#defense attributes
def test_hero_defense():
    hero = Hero("defense")
    assert hero.defense == 2
    assert hero.protection == 0

#speed
def test_hero_speed():
    hero = Hero("speed")
    assert hero.speed == 1


def test_give_hero_food():
    hero = Hero("food")
    assert hero.give_food(50) == hero.food

def test_give_hero_xp():
    hero = Hero("XP")
    assert hero.xp == 0
    hero.give_XP(5)
    assert hero.xp == 5

def test_give_hero_gold():
    hero = Hero("gold")
    assert hero.give_gold(500) == hero.gold

def test_level_up_hero():
    hero = Hero("Level up")
    assert hero.level == 1

    hero.give_XP(10)
    assert hero.level == 2
    hero.give_XP(10*hero.level)
    assert hero.level == 3