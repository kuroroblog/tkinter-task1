import tkinter as tk
import re

# 計算するボタンを選択した場合に実行する関数
def bt_calc():
    e1Value = e1.get()
    e2Value = e2.get()
    e3Value = e3.get()
    if e1Value == '':
        print('お酒の量(ml)を入力ください')
        return
    if e2Value == '':
        print('アルコール度数を入力ください')
        return
    if e3Value == '':
        print('割る水の量(ml)を入力ください')
        return

    # 計算式参考 : https://joytas.net/programming/python/tkinter-sake
    result = (int(e2Value) * int(e1Value)) / (int(e1Value) + int(e3Value))
    # 小数点の表記参考 : https://hibiki-press.tech/python/round_ceil_floor/903
    l2.configure(text=round(result, 1))

# クリアボタンを選択した場合に実行する関数
def bt_clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)

# 入力制限について : https://kuroro.blog/python/YaHEdMd4ScGvrU44zdT6/
def onValidate(S):
    # 入力された文字が半角数字の場合
    # reについて : https://note.nkmk.me/python-re-match-search-findall-etc/
    if re.match(re.compile('[0-9]+'), S):
        return True
    else:
        # 入力不正のブザーを鳴らす。
        root.bell()
        return False

mc='#f0edc7'
sc='#51ada8'

s1={'padx':5,'pady':5,'anchor':tk.W}
s2={'padx':10,'pady':5,'anchor':tk.W}

# Windowを生成する。
# Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
root=tk.Tk()

# Windowの画面サイズを設定する。
# geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
root.geometry('300x500')
# titleを設定
root.title('水割りアルコール度数計算')
# Windowの背景色を設定
root['bg'] = mc

# Windowを親要素として、label Widgetを作成する。
# fg : 文字列色を設定。
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# bg : 背景色
# text : テキスト情報
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
# Windowを親要素とした場合に、label Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
tk.Label(root, fg='white', bg=sc, text='水割りアルコール度数計算').pack(fill=tk.X)

# register : 入力制限を行うための関数の登録を行う。パラメータと関数を紐づけるために必要。
# 入力制限について : https://kuroro.blog/python/YaHEdMd4ScGvrU44zdT6/
vcmd = root.register(onValidate)

# Windowを親要素として、label Widgetを作成する。
# bg : 背景色を設定。
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# text : テキスト情報
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
# Windowを親要素とした場合に、label Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
tk.Label(root, bg=mc, text='お酒の量(ml)').pack(**s1)
# Windowを親要素として、entry Widgetを作成する。
# width : 幅の設定
# validate : 入力制限するオプションの値を設定。
# validatecommand or vcmd : 入力制限用関数の設定。
# Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
e1=tk.Entry(root, width=10, validate="key", validatecommand=(vcmd, '%S'))
# Windowを親要素とした場合に、entry Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
e1.pack(**s2)

# Windowを親要素として、label Widgetを作成する。
# bg : 背景色を設定。
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# text : テキスト情報
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
# Windowを親要素とした場合に、label Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
tk.Label(root, bg=mc, text='アルコール度数').pack(**s1)
# Windowを親要素として、entry Widgetを作成する。
# width : 幅の設定
# validate : 入力制限するオプションの値を設定。
# validatecommand or vcmd : 入力制限用関数の設定。
# Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
e2=tk.Entry(root, width=10, validate="key", validatecommand=(vcmd, '%S'))
# Windowを親要素とした場合に、entry Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
e2.pack(**s2)

# Windowを親要素として、label Widgetを作成する。
# bg : 背景色を設定。
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# text : テキスト情報
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
# Windowを親要素とした場合に、label Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
tk.Label(root, bg=mc, text='割る水の量(ml)').pack(**s1)
# Windowを親要素として、entry Widgetを作成する。
# width : 幅の設定
# validate : 入力制限するオプションの値を設定。
# validatecommand or vcmd : 入力制限用関数の設定。
# Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
e3=tk.Entry(root, width=10, validate="key", validatecommand=(vcmd, '%S'))
# Windowを親要素とした場合に、entry Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
e3.pack(**s2)

# Windowを親要素として、button Widgetを作成する。
# text : テキスト情報
# width : 幅の設定
# height : 高さの設定
# highlightbackground : 囲い線の色
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# command : ボタンを選択した場合に、実行する関数を設定。bt_calcとする。
# Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
calc_bt=tk.Button(root, text='計算する', width=12, height=2, highlightbackground='#ef8f35', command=bt_calc)
# Windowを親要素とした場合に、button Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
calc_bt.pack(padx=10, pady=15, anchor=tk.W)

# Windowを親要素として、button Widgetを作成する。
# text : テキスト情報
# width : 幅の設定
# height : 高さの設定
# highlightbackground : 囲い線の色
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# command : ボタンを選択した場合に、実行する関数を設定。bt_clearとする。
# Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
clear_bt=tk.Button(root, text='クリア', width=12, height=2, highlightbackground=sc, command=bt_clear)
# Windowを親要素とした場合に、button Widgetをどのように配置するのか?
# packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
clear_bt.pack(padx=10, pady=10, anchor=tk.W)

# Windowを親要素として、label Widgetを作成する。
# bg : 背景色を設定。
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# text : テキスト情報
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
l1=tk.Label(root, bg=mc, text='アルコール度数は')
# Windowを親要素とした場合に、label Widgetをどのように配置するのか?
# placeについて : https://kuroro.blog/python/JyaHUKyFyxCa0baFfXg0/
l1.place(x=10, y=400)
# Windowを親要素として、label Widgetを作成する。
# bg : 背景色を設定。
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# font : フォントの設定。
# フォントについて : https://kuroro.blog/python/RZNjLl36upkumxwkTRWl/
# fg : 文字列色を設定。
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
l2=tk.Label(root, bg=mc, font=('Arial', 24), fg='red')
# Windowを親要素とした場合に、label Widgetをどのように配置するのか?
# placeについて : https://kuroro.blog/python/JyaHUKyFyxCa0baFfXg0/
l2.place(x=125, y=392)
# Windowを親要素として、label Widgetを作成する。
# bg : 背景色を設定。
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# text : テキスト情報
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
l3=tk.Label(root, bg=mc, text='度です')
# Windowを親要素とした場合に、label Widgetをどのように配置するのか?
# placeについて : https://kuroro.blog/python/JyaHUKyFyxCa0baFfXg0/
l3.place(x=180, y=400)

# Windowをループさせて、継続的にWindow表示させる。
# mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
root.mainloop()
