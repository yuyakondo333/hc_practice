from juice import Juice

class VendingMachine:
    def __init__(self):
        self.__sales = 0
        self.__juices = []

        # 初期ジュースを追加
        for _ in range(5):
            self.__juices.append(Juice("ペプシ", 150))
        for _ in range(5):
            self.__juices.append(Juice("モンスター", 230))
        for _ in range(5):
            self.__juices.append(Juice("いろはす", 120))

    def restocking(self, name, amount):
        if amount < 0:
            raise ValueError("正の整数を設定してください")
        for _ in range(amount):
            if name == "ペプシ":
                self.__juices.append(Juice("ペプシ", 150))
            elif name == "モンスター":
                self.__juices.append(Juice("モンスター", 230))
            elif name == "いろはす":
                self.__juices.append(Juice("いろはす", 120))
            else:
                raise NameError(f"{name}は取り扱いがありません")
        return f"{name}が{amount}個追加されました"

    def get_buyable_juice(self, suica):
        buyable_juices = {}
        stock = {}
        for juice in self.__juices:
            if juice.name not in stock:
                stock[juice.name] = {"count": 0, "price": juice.price}
            stock[juice.name]["count"] += 1
        for name, data in stock.items():
            if suica.deposit >= data["price"] and data["count"] > 0:
                buyable_juices[name] = f"{name}: 価格 {data['price']}円、在庫 {data['count']}個"
        return buyable_juices

    def get_sales(self):
        return self.__sales

    def update_sales(self, price):
        self.__sales += price

    def process_purchase(self, suica, juice_name):
        for i, juice in enumerate(self.__juices):
            if juice.name == juice_name:
                if suica.deposit < juice.price:
                    raise ValueError("残高が不足しています")
                del self.__juices[i]
                self.update_sales(juice.price)
                suica.reduce_deposit(juice.price)
                return f"{juice_name}を購入した。Suica残高は{suica.deposit}円です\nこの自動販売機の売り上げ{self.get_sales()}円"
        raise NameError(f"{juice_name}は在庫切れです")