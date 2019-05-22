# 自作クラスのインポート
import HelloWorldHolder as hwh
import DisplayString as ds

class HelloWorldDisplayer:

    # コンストラクタ
    # メンバ変数にクラスを読み込み
    def __init__(self):
        self.hwHolder=hwh.HelloWorldHolder()
        self.displayStr=ds.DisplayString(self.hwHolder.getHelloWorld())
    
    # DisplayString クラスに文字列を表示するように指示
    def start(self):
        self.displayStr.printString()
