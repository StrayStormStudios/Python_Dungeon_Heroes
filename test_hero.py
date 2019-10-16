from hero import Hero

def test_hero_name():
    hero = Hero("test")
    assert hero.name == "test"

def test_hero_health():
    hero = Hero("health")
    assert hero.health == 100

    hero.set_health(70)
    assert hero.health == 70
    hero.set_health(50)
    assert hero.health == 50
    hero.set_health(20)
    assert hero.health == 20
    hero.set_health(10)
    assert hero.health == 10
