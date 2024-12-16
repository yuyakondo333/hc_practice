from pokemon import Pokemon

class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)
    
    def change_name(self, new_name):
        super().change_name(new_name)

    def get_name(self):
        return super().get_name()

    def attack(self):
        super_attack = super().attack()
        return f"{super_attack}:{self.get_name()}の10万ボルト!"


if __name__ == "__main__":
    pika = Pikachu("ピカチュウ", "でんき", "", 100)
    print(pika.attack())

    pika.change_name("テキセツ")
    print(pika.get_name())
    pika.change_name("うんこ")
    print(pika.get_name())
