# 配列
l1 = ["chika", "you", "riko", "ruby", "yoshiko", "hanamaru", "kanan", "mari", "dia"]
for name in l1:
    print(name)

# 一部だけ抜き出す
l2 = l1[3:6]
print(l2)

# 要素の追加と削除
l2.append("yohane")
print(l2)
l2.remove("yohane")
print(l2)
