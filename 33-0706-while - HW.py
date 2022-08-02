"""
while
"""
"""
== == 練習題31 == == =
只能用
while 依照以下樣版
x = 0  # 迴圈的   一開始的數字
while x < 3:  # 迴圈  判斷式  結束的數字
    # 要做的事情
    print(x)  # 執行動作
    x = x + 1  # 變數 迴圈的   每次增加的數字

print("End")  # 結束

輸出：
10
11
12
13
14
"""
print("== == 練習題31 == == =")
x=10                       # 迴圈一開始的數字
while x<15:                # 迴圈 判斷式 結束的數字
    #要做的事情
    print(x)               # 執行動作
    x=x+1                  # 變數 迴圈的 每次增加的數字

print("END")
"""
== == 練習題32 == == =
同上一題，修改為
輸出：
22
23
24
"""
print("== == 練習題32 == == =")
x=22                       # 迴圈一開始的數字
while x<25:                # 迴圈 判斷式 結束的數字
    #要做的事情
    print(x)               # 執行動作
    x=x+1                  # 變數 迴圈的 每次增加的數字

print("END")
"""

== == 練習題33 == == =
同上一題，修改為
輸出：
50
53
56
59

"""
print("== == 練習題33 == == =")
x=50                       # 迴圈一開始的數字
while x<60:                # 迴圈 判斷式 結束的數字
    #要做的事情
    print(x)               # 執行動作
    x=x+3                  # 變數 迴圈的 每次增加的數字

print("END")

"""

== == 練習題34 == == =
同上一題，修改為
輸出：

55
44
33
22
11

"""
print("== == 練習題34 == == =")
x=55                        # 迴圈一開始的數字
while x>=11:                # 迴圈 判斷式 結束的數字
    #要做的事情
    print(x)                # 執行動作
    x=x-11                  # 變數 迴圈的 每次增加的數字

print("END")
"""

== == 練習題35 == == =
同上一題，修改為
輸出：

60
40
20

"""

print("== == 練習題35 == == =")
x=60                        # 迴圈一開始的數字
while x>=20:                # 迴圈 判斷式 結束的數字
    #要做的事情
    print(x)                # 執行動作
    x=x-20                  # 變數 迴圈的 每次增加的數字

print("END")

"""
== == 練習題36 == == =
使用input
輸入A數字
為開始的數字
使用input
輸入B數字
為結束的數字

例如輸入
開始的數字為5
例如輸入
結束的數字為10
印出
5
6
7
8
9
10

"""
"""
print("== == 練習題36 == == =")
A=input("請輸入數字A:")
A=int(A)
B=input("請輸入數字B(需大於A數字):")
B=int(B)

x=A                        # 迴圈一開始的數字
while x<(B+1):             # 迴圈 判斷式 結束的數字
    #要做的事情
    print(x)               # 執行動作
    x=x+1                  # 變數 迴圈的 每次增加的數字

print("END")

"""
"""
== == 練習題41 == == =
使用
while , if elif else

印出
-1
-2
-4
-5
"""

print("== == 練習題41 == == =")
x=-1                           # 迴圈一開始的數字
while x>-6:                    # 迴圈 判斷式 結束的數字
    #要做的事情
    if x!=-3:
        print(x)               # 執行動作
    x=x-1                      # 變數 迴圈的 每次增加的數字

print("END")

"""
== == 練習題42 == == =
使用
while , if elif else

當
x
等於3
時, 叁

印出

零
1
2
參
4
伍
6
7
"""
print("== == 練習題42 == == =")
x=0                            # 迴圈一開始的數字
while x<8:                     # 迴圈 判斷式 結束的數字
    #迴圈顯示中有幾點要求
    if x==0:                   # 第一點  當x=0
        print("零")            # 顯示零
    elif x==3:                 # 第二點  當x=3
        print("參")            # 顯示參
    elif x==5:                 # 第三點  當x=5
        print("伍")            # 顯示伍
    else:                      # 其他沒有提到的
        print(x)               # 就幫我直接列印 執行動作
    # 希望迴圈要做的事情
    x=x+1                      # 變數 迴圈的 每次增加的數字

print("END")
"""

== == 練習題43 == == =
使用
while , if elif else

當x等於1時, 一
當x等於2時, 二
當x等於3時, 三
當x等於4時, 四

印出

一
二
三
四

"""
print("== == 練習題43 == == =")
x=1                            # 迴圈一開始的數字
while x<5:                     # 迴圈 判斷式 結束的數字
    # (迴圈中有幾點要求)
    if x==1:                   # 第一點 x=1時
        print("一")             # 顯示一
    elif x==2:                 # 第二點 x=2時
        print("二")            # 顯示二
    elif x==3:                 # 第三點 x=3時
        print("三")            # 顯示三
    else:                      # 其他沒有提到的
        print("四")            # 就幫我直接列印 四
    # 希望迴圈要做的事情
    x=x+1                      # 變數 迴圈的 每次增加的數字

print("END")

"""
== == 練習題44 == == =
輸入最大的數量n
使用2個while
    輸出：

    A
    AA
    AAA
    AAAA
    …..
    直到
    ｎ個
"""
print("== == 練習題44 == == =")

x=input("請輸入數字:")            # 輸入一個數字代表最大值
x=int(x)                        # 轉換成數值
str1=""                         # 設定一個 空白
y=0                             # 設定迴圈起始數
while y<x+1:                    # 當x+1大於y 時 停止迴圈
    print(str1)                 # 列印 當前狀態的str1
    str1 = str1 + "A"           # 當前狀態的str1+字元A
    y=y+1                       # y+1

print("END")

"""
== == 練習題45　 == == =
使用
while , if elif else

透過迴圈，可以一直的玩的終極密碼

輸入二次文字
1.終極密碼的數字
2.要猜的數字0~99的數字

按下“q” 就結束迴圈結束遊戲

例如：
輸入20回答
答案在20~99之間
輸入70回答
答案在20~70之間
......
答對了
繼續下一輪的遊戲

"""

print("== == 練習題45　 == == =")

print("終極密碼遊戲")

answerNumber=input("請輸入答案(0-99):")
answerNumber=int(answerNumber)
guessNumber=input("你猜的數字:")
guessNumber=int(guessNumber)

min=0
min=int(min)
max=99
max=int(max)

if answerNumber==guessNumber:
    print("BINGO")

if answerNumber!=guessNumber:

    while guessNumber>answerNumber:
        max=guessNumber
        print(("0 到"),(max))
        input("請再猜數字:")

        break

    while guessNumber < answerNumber:
        min = guessNumber
        print((min),("到 99") )
        input("請再猜數字:")
        break









