class HelloWorldHolder:

    # コンストラクタ
    # 文字列を作成してメンバ変数に格納
    def __init__(self):
        self.helloWorld='Hello, world!'
    
    # 文字列を返す
    def getHelloWorld(self):
        return self.helloWorld
