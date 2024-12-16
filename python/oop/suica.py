class Suica:
    def __init__(self, deposit=500):
        self.__deposit = deposit

    # 預かり金残高を取得する getter
    @property
    def deposit(self):
        return self.__deposit

    # 残高をチャージする setter
    @deposit.setter
    def charge(self, amount):
        self.__deposit += amount

    # 購入時に残高から価格を引くメソッド
    def reduce_deposit(self, price):
        self.__deposit -= price