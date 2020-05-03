#! Python3
# Typing main program

## import群
import file_access
import time
import math
import sys
import threading
import signal
#from time_view import *
from front_view_class import FrontView

## メッセージ管理
messages = {}

## 言語管理マップ
gengo_manager = {
    "1":"python",
    "2":"c",
    "3":"java",
    "4":"Ruby",
    "99":"END",
}

## 初期設定
def init():
    messages[0] = "start"
    messages[1] = "next"
    messages[2] = "end"

## 入力チェック
"""
def input_check(check_word):
    print(check_word)
    if check_word == input():
        print("OK\n")
        return True
    else:
        print("NG\n")
        return False
"""
## 出力メッセージの制御
def output_massage(message_number):
    # メッセージ番号によって出力メッセージを変えてみる
    messages[message_number]   
    
## タイピング処理（メイン）
if __name__ == "__main__":

    # 主旨説明文
    #yoyakugo_map = file_access.get_yoyakugo_info()
    print("######################################################")
    print("###############  予約語タイピング練習  ###############")
    print("######################################################")
    print("各プログラム言語の予約語を使って、タイピング練習を実施します。\n")
    
    # 言語選択
    # 選択番号初期化
    gengo_name = ""
    while not gengo_name:
        print("以下に示した言語を半角数字で入力してください。")
        print("1:Python 2:c言語 3:Java 4:Ruby 99:タイピングしない")
        gengo_number = input()
        if gengo_number in gengo_manager:
            gengo_name = gengo_manager[gengo_number] 
        else:
            print("再度、入力をお願いします。")

    if gengo_name == "END":
        print("タイピングを終了します。")
        sys.exit()
        
    # 予約語読み込み
    yoyakugo_list = file_access.get_yoyakugo_info(gengo_name)
 
    # 問題数選択
    # 選択番号初期化
    mondaisu = 0
    mondai_number = "" 
    while not mondaisu:
        print("以下に示した問題数を半角数字で入力してください。")
        print("1:10単語 2:20単語 3:全ての単語")
        mondai_number = input()
        if "1" == mondai_number or "2" == mondai_number:
            mondaisu = int(mondai_number) * 10
        elif "3" == mondai_number:
            mondaisu = len(yoyakugo_list)  
        else:
            print("再度、入力をお願いします。")
 
    front_view = FrontView(yoyakugo_list, mondaisu)

    # 開始合図
    input("リターンキー、または、エンターキーを押すと開始します。")
    start_time = time.time()

    ## 時間表示と問題出力
    front_view.count_main()
    
    count = front_view.get_ans_count()
    count_time = math.floor(time.time() - start_time) - 1
    minutes = math.floor(int(count_time) / 60)
    seconds = int(count_time) % 60
    print("かかった時間: {0} 分 {1} 秒".format(str(minutes), str(seconds)))
    print("成功:" + str(count))
    print("失敗:" + str(mondaisu - count))
    #signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(0)
