# randomをimport
import random

# 6人グループをgroupsという変数に格納
groups = ["A", "B", "C", "D", "E", "F"]

# 2~4で乱数を発生させて r に格納
r = random.randint(2, 4)

"""
a,bに3:3 or 2:4 or 4:2になるようにsampleを使って分ける
bグループは重複を削除するためにsetを使用
昇順にするためにsortedを使用
"""
a = sorted(random.sample(groups, r))
b = sorted(set(groups) - set(a))

# a,bを出力
print(a)
print(b)