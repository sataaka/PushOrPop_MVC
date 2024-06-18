# entity/filed.py

class Filed:
    def __init__(self, size):
        self.stack = [0] * size  # スタックのサイズを指定
        self.sp = 0  # スタックポインタ

    def getStack(self):
        return self.stack

    def getSp(self):
        return self.sp

    def setSp(self, sp):
        self.sp = sp
