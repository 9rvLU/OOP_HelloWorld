class DisplayString:

    # コンストラクタ
    # self.string に文字列を登録
    def __init__(self, inputString):
        self.setString(inputString)

    # self.string に文字列を登録
    def setString(self, inputString):
        self.string=inputString
    
    # self.string をターミナルに表示
    def printString(self):
        print(self.string)
