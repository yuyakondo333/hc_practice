class Suica:
    def __init__(self, deposit=500):
        self.__deposit = deposit
    
    @property
    # 預かり金残高を取得する getter を定義
    def deposit(self):
        return self.__deposit
    
    # 残高をチャージする setter を定義
    @deposit.setter
    def deposit(self, amount):
        self.__deposit += amount
    
    # 購入時に残高 - 価格 をする reduce_deposit を定義
    def reduce_deposit(self, price):
        self.__deposit -= price


class Juice:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def name(self):
        return self.__name
    
    # 値段を取得する getter を定義
    @property
    def price(self):
        return self.__price
    
    # 在庫を取得する setter を定義
    @property
    def stock(self):
        return self.__stock
    
    # 購入時に在庫を1つ減らす reduce_stock を定義
    def reduce_stock(self):
        self.__stock -= 1
    
    # 在庫を補充する restock を定義
    def restock(self, amount):
        # そのキーの値のstockにamountを加える
        self.__stock += amount

    # str()を呼び出すとreturnの文が返される
    def __str__(self):
        return f"{self.__name}: 価格 {self.__price}円、在庫 {self.__stock}個"


class VendingMachine:
    def __init__(self):
        # 売り上げは0にする
        self.__sales = 0
        # ジュースを辞書型で管理
        # コンストラクタを呼び出した際に
        # Juice classを呼び出してそれぞれの引数に値を渡す
        self.__juice = {
            "ペプシ": Juice("ペプシ", 150, 5),
            "モンスター": Juice("モンスター", 230, 5),
            "いろはす": Juice("いろはす", 120, 5),
        }
    
    # 在庫を補充するメソッドrestockを使用するメソッド
    def restocking(self, name, amount):
        # 取り扱いがない name だったら例外発生
        if name not in self.__juice:
            raise NameError(f"{name}は取り扱いがありません")
        # amountがint変換可能だったら変換する　別の文字列だったら例外発生
        try:
            amount = int(amount)
        except ValueError:
            raise ValueError(f"正の整数を設定してください")
        # amountに渡された値が負の数で例外発生
        if amount < 0:
            raise ValueError(f"正の整数を設定してください")

        self.__juice[name].restock(amount)
        current_stock = self.__juice[name].stock
        return f"{name}が{amount}個追加されて、合計で在庫が{current_stock}個になりました"

    # 購入可能なドリンクのリストを取得
    def get_buyable_juice(self):
        return {name: str(juice) for name, juice in self.__juice.items() if juice.stock > 0}
    
    # 売り上げ金額を取得する get_sales を定義
    def get_sales(self):
        return self.__sales

    # 売り上げ金額を増やす update_sales を定義
    def update_sales(self, price):
        self.__sales += price

    # 購入判定
    def check_buyable(self, suica, juice_name):
        # 取り扱いのないジュースの名前だったら例外発生
        if juice_name not in self.__juice[juice_name].name:
            raise NameError(f"{juice_name}は取り扱いがありません")
        # チャージ残高 < 価格で例外発生
        if suica.deposit < self.__juice[juice_name].price:
            raise ValueError("残高が不足しています")
        # 在庫が0で例外を発生
        if self.__juice[juice_name].stock == 0:
            raise ValueError("在庫が不足しています")

        return True
    
    # 購入プロセス
    def process_purchase(self, suica, juice_name):
        # 購入判定結果を変数に格納
        check_buyable = self.check_buyable(suica, juice_name)

        # check_buyableがTrueだったら
        if check_buyable:
            # ジュースの在庫を減らす
            self.__juice[juice_name].reduce_stock()
            # 売り上げ金額を増やす
            self.update_sales(self.__juice[juice_name].price)
            # Suicaのチャージ残高を減らす
            suica.reduce_deposit(self.__juice[juice_name].price)

        return f"{juice_name}を購入した。Suica残高は{suica.deposit}円です\nこの自動販売機の売り上げ{self.get_sales()}円"


if __name__ == "__main__":
    # 自動販売機クラスのインスタンスを生成
    vending_machine = VendingMachine()
    # 購入可能なリストを取得して変数に格納
    buyable_juices = vending_machine.get_buyable_juice()
    # 購入可能なジュースのリストを出力
    print("↓以下は現在購入可能なジュースのリストです↓")
    for juice in buyable_juices.values():
        print(juice)
    print()

    # Suicaクラスのインスタンスを生成
    suica1 = Suica()
    # 現在のSuicaの残高を変数に格納
    deposit1 = suica1.deposit
    # 結果を出力
    print(f"あなたのSuicaの残高は{deposit1}円です。")
    # suica1に1000円チャージ
    suica1.deposit = 1000
    # チャージした金額を加えた現在のsuicaの残高を変数に格納
    charge_deposit1 = suica1.deposit
    # 結果を出力
    print(f"チャージしたのであなたのSuicaの残高は{charge_deposit1}円に変更されました")

    # いろはすを購入
    irohasu = vending_machine.process_purchase(suica1, "いろはす")
    print(irohasu)
    print()

    # 在庫の補充
    add_pepsi = vending_machine.restocking("ペプシ", 10)
    print(add_pepsi)
    print()

    # いろはすの購入と在庫の補充が反映されているか
    buyable_juices = vending_machine.get_buyable_juice()
    print("↓以下は現在購入可能なジュースのリストです↓")
    for juice in buyable_juices.values():
        print(juice)

