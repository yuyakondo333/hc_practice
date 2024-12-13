class Suica:
    def __init__(self, deposit=500):
        self.__deposit = deposit

    @property
    # 預かり金残高を取得する getter
    def deposit(self):
        return self.__deposit

    @deposit.setter
    # 残高をチャージする setter
    def deposit(self, amount):
        self.__deposit += amount

    # 購入時に残高から価格を引くメソッド
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

    # 値段を取得する getter
    @property
    def price(self):
        return self.__price

    # 在庫を取得する getter
    @property
    def stock(self):
        return self.__stock

    # 購入時に在庫を1つ減らすメソッド
    def reduce_stock(self):
        self.__stock -= 1

    # 在庫を補充するメソッド
    def restock(self, amount):
        self.__stock += amount

    # str()を呼び出すと返される文字列
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
            "ペプシ": Juice("ペプシ", 150, 0),
            "モンスター": Juice("モンスター", 230, 5),
            "いろはす": Juice("いろはす", 120, 5),
        }

    # 在庫を補充するメソッドrestockを使用するメソッド
    def restocking(self, name, amount):
        # 取り扱いがない name だったら例外発生
        if name not in self.__juice:
            raise NameError(f"{name}は取り扱いがありません")
        # amountが整数に変換可能か確認
        try:
            amount = int(amount)
        except ValueError:
            raise ValueError(f"正の整数を設定してください")
        # 負の値が渡された場合の例外
        if amount < 0:
            raise ValueError(f"正の整数を設定してください")

        # 在庫を補充
        self.__juice[name].restock(amount)
        current_stock = self.__juice[name].stock
        return f"{name}が{amount}個追加されて、合計で在庫が{current_stock}個になりました"

    # 購入可能なドリンクのリストを取得するメソッド
    def get_buyable_juice(self, suica):
        buyable_juices = {}
        for name, juice in self.__juice.items():
            try:
                # 購入可能か判定
                self.check_buyable(suica, name)
                buyable_juices[name] = str(juice)
            except (ValueError, NameError):
                # 例外が発生した場合はスキップ
                continue
        return buyable_juices

    # 売り上げ金額を取得する getter
    def get_sales(self):
        return self.__sales

    # 売り上げ金額を増やすメソッド
    def update_sales(self, price):
        self.__sales += price

    # 購入判定
    def check_buyable(self, suica, juice_name):
        # 取り扱いのないジュースの名前だったら例外発生
        if juice_name not in self.__juice:
            raise NameError(f"{juice_name}は取り扱いがありません")
        # チャージ残高が価格未満だった場合の例外
        if suica.deposit < self.__juice[juice_name].price:
            raise ValueError("残高が不足しています")
        # 在庫が0の場合の例外
        if self.__juice[juice_name].stock == 0:
            raise ValueError("在庫が不足しています")
        return True

    # 購入プロセス
    def process_purchase(self, suica, juice_name):
        check_buyable = self.check_buyable(suica, juice_name)

        if check_buyable:
            # ジュースの在庫を減らす
            self.__juice[juice_name].reduce_stock()
            # 売り上げ金額を増やす
            self.update_sales(self.__juice[juice_name].price)
            # Suicaのチャージ残高を減らす
            suica.reduce_deposit(self.__juice[juice_name].price)

        return f"{juice_name}を購入した。Suica残高は{suica.deposit}円です\nこの自動販売機の売り上げ{self.get_sales()}円"


if __name__ == "__main__":
    # Suicaクラスのインスタンスを生成
    suica1 = Suica()
    # 自動販売機クラスのインスタンスを生成
    vending_machine = VendingMachine()

    # 購入可能なリストを取得して変数に格納
    buyable_juices = vending_machine.get_buyable_juice(suica1)
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
    buyable_juices = vending_machine.get_buyable_juice(suica1)
    print("↓以下は現在購入可能なジュースのリストです↓")
    for juice in buyable_juices.values():
        print(juice)
