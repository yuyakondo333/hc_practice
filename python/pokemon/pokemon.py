from abc import ABCMeta, abstractmethod

class Pokemon(metaclass=ABCMeta):
    def __init__(self, name, type1, type2, hp):
        self.__name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
    
    @abstractmethod
    def change_name(self, new_name):
        # 不適切な名前はエラー
        if new_name == 'うんこ':
            print("不適切な名前です")
        
        self.__name = new_name

    @abstractmethod
    def get_name(self):
        return self.__name
    
    def attack(self):
        return f"{self.get_name()}の攻撃!"
