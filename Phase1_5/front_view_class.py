# utf-8
# FrontView.py

# import群
import tkinter as tk
import tkinter.font as font
import time
import math
import random
import threading
import sys
import signal

class FrontView():
    def __init__(self, yoyakugo_list, mondaisu):
        self.root = tk.Tk()
        self.root.title("経過時間")
        self.root.geometry("400x75+500+100")    
        my_font = font.Font(self.root, family="System", size=50, weight="bold")
        self.label = tk.Label(text="0 分 0 秒", font=my_font)
        self.label.pack()
        self.count = 0
        self.ans_count = 0
        self.syutsudai_list = random.sample(yoyakugo_list, mondaisu)
        self.mondaisu = mondaisu

    def count_up(self):
        self.count
        self.label
        if self.count != 0:
            minutes = int(self.count / 60)
            seconds = self.count % 60
            view_text = "{0} 分 {1} 秒経過".format(minutes, seconds)
            self.label["text"] = view_text
        self.count = self.count + 1

    # スレッド集約
    def count_thread_def(self):
        count_thread = threading.Thread(target=self.count_up)
        count_thread.daemon = True
        count_thread.start()
        self.root.after(1000, self.count_thread_def)

    ## ウィンドウを閉じる（ウィンドウ表示を止める）
    def window_close(self):
        self.root.quit()

    ## 本クラスの開始関数
    def count_main(self):
        self.count_thread_def()
        question_thread = threading.Thread(target=self.question)
        question_thread.daemon = True
        question_thread.start()
        self.root.mainloop()

    ## 入力チェック
    def check_word(self, check_word):
        print(check_word)
        if check_word == sys.stdin.readline().strip():
            print("OK\n")
            return True
        else:
            print("NG\n")
            return False

    ## 指定問題数分出題
    def question(self):
        # ランダムで数値を取得する
        for out_value in self.syutsudai_list:
            if self.check_word(out_value):
                self.ans_count += 1
        self.window_close()

    ## 正当数を出力
    def get_ans_count(self):
        return self.ans_count
        