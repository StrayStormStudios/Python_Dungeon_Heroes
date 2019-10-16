from hero import Hero

def test_hero_name():
    hero = Hero("test")
    assert hero.name == "test"

#life stats
def test_hero_health():
    hero = Hero("health")
    assert hero.health == 100
    assert hero.maxHealth == hero.health

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
    assert hero.maxStamina == hero.stamina

def test_hero_food():
    hero = Hero("food")
    assert hero.maxFood == 63
    assert hero.food == hero.maxFood

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
