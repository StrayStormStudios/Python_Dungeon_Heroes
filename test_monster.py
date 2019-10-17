from monster import Monster

def test_monster_name():
    monster = Monster("test")
    assert monster.name == "test"

#life stats
def test_monster_health():
    monster = Monster("health")
    assert monster.health == 100
    assert monster.current_health == monster.health

    monster.set_health(70)
    assert monster.current_health == 70
    monster.set_health(50)
    assert monster.current_health == 50
    monster.set_health(20)
    assert monster.current_health == 20
    monster.set_health(10)
    assert monster.current_health == 10

def test_monster_stamina():
    monster = Monster("stamina")
    assert monster.stamina == 10
    assert monster.max_stamina == monster.stamina

def test_monster_food():
    monster = Monster("food")
    assert monster.max_food == 40
    assert monster.food == monster.max_food

def test_monster_gold():
    monster = Monster("gold")
    assert monster.gold == 0

#attack attributes
def test_monster_attack():
    monster = Monster("attack")
    assert monster.attack == 2
    assert monster.damage == 0

#defense attributes
def test_monster_defense():
    monster = Monster("defense")
    assert monster.defense == 2
    assert monster.protection == 0

#speed
def test_monster_speed():
    monster = Monster("speed")
    assert monster.speed == 1

