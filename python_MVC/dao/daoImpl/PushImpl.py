# daoImpl/pushImpl.py

from dao.Push import Push
from entity.Filed import Filed

class PushImpl(Push):
    def push(self, stack: Filed, data: int):
        if stack.getSp() < len(stack.getStack()):
            stack.getStack()[stack.getSp()] = data
            stack.setSp(stack.getSp() + 1)
        else:
            print("スタック領域に空きがない")
