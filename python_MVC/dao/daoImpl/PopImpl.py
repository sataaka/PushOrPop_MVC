# daoImpl/popImpl.py

from dao.Pop import Pop
from entity.Filed import Filed

class PopImpl(Pop):
    def pop(self, stack: Filed) -> int:
        if stack.getSp() > 0:
            value = stack.getStack()[stack.getSp()]
            stack.setSp(stack.getSp() - 1)
            return value
        else:
            print("スタックが空です")
            return -999  # エラー値を返す
