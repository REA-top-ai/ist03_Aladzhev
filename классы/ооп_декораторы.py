def is_alive(func):
    def wrapper(*args, **kwargs):
        hero = args[0]
        if hero.health <= 0:
            print(f"{hero.name} мертв и не может действовать!")
            return None
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Начало действия: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Действие завершено")
        return result
    wrapper.__name__ = func.__name__
    return wrapper


def easter_event(func):
    def wrapper(self, *args, **kwargs):
        health_old = self.health
        mana_old = self.mana
        self.health *= 2
        self.mana *= 1.5
        if self.hero_class == "волшебник":
            self.items["Священный посох"] = {"mana_boost": 5}
            self.mana += 5
        result = func(self, *args, **kwargs)
        self.health = health_old
        self.mana = mana_old
        return result
    return wrapper


class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        if hero_class == "волшебник":
            self.health = 60
        else:
            self.health = 100
        if hero_class == "волшебник":
            self.mana = 50
        else:
            self.mana = 10
        self.hero_class = hero_class
        self.spells_names = {}
        self.items = {}
        if len(self.items) > 6:
            raise ValueError("Не больше 6 предметов")

    @is_alive
    def attack(self, damage):
        print(f"Герой нанес урон: {damage}")

    @log_action
    def heal(self, amount):
        self.health += amount

    @is_alive
    def cast_spell(self, spell_name):
        self.mana -= self.spells_names[spell_name]["mana_cost"]
        print(spell_name)

    def add_spell(self, spell_name, mana_cost, attack_damage = 0, health_increase = 0):
        self.spells_names[spell_name] = {"mana_cost": mana_cost, "attack_damage": attack_damage, "health_increase": health_increase}

    def add_item(self, item_name, parametr, value):
        self.items[item_name] = {parametr: value}

    @easter_event
    def event(self):
        pass
