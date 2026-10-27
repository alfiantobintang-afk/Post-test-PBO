class hero():
    def __init__(self, nama, health, attack, armor, mana=50):
        self.name = nama
        self.health = health
        self.attack = attack
        self.armor = armor
        self.mana =mana
    def __str__(self):
        return f'nama hero {self.hero}'
balmond = hero('balmond', 100, 15, 4)
print(balmond)
    