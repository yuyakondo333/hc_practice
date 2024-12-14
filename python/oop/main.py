from suica import Suica
from vending_machine import VendingMachine

if __name__ == "__main__":
    suica1 = Suica()
    vending_machine = VendingMachine()

    buyable_juices = vending_machine.get_buyable_juice(suica1)
    print("↓以下は現在購入可能なジュースのリストです↓")
    for juice in buyable_juices.values():
        print(juice)

    suica1.charge = 1000
    print(f"チャージしたのであなたのSuicaの残高は{suica1.deposit}円に変更されました")

    irohasu = vending_machine.process_purchase(suica1, "いろはす")
    print(irohasu)

    add_pepsi = vending_machine.restocking("ペプシ", 10)
    print(add_pepsi)

    buyable_juices = vending_machine.get_buyable_juice(suica1)
    print("↓以下は現在購入可能なジュースのリストです↓")
    for juice in buyable_juices.values():
        print(juice)
