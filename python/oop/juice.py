class Juice:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    # 値段を取得する getter
    @property
    def price(self):
        return self.__price

    # str()を呼び出すと返される文字列
    def __str__(self):
        return f"{self.__name}: 価格 {self.__price}円"