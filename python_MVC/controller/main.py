# controller/main.py
import sys
import os

# プロジェクトのルートディレクトリをsys.pathに追加
#  リストの末尾に新しいディレクトリ   親ディレクトリ     親ディレクトリ    絶対パス       現在のファイルパス(main.py)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.Filed import Filed
from service.serviceImpl.service_popDao_pushDaoImpl import ServicePopDaoPushDaoImpl

def main():
    stack_size = 5
    stack = Filed(stack_size)
    service = ServicePopDaoPushDaoImpl()

    service.push_data(stack, 10)
    print(f"SP = {stack.getSp()}: stack[{stack.getSp() - 1}] = {stack.getStack()[stack.getSp() - 1]}")

    service.push_data(stack, 20)
    print(f"SP = {stack.getSp()}: stack[{stack.getSp() - 1}] = {stack.getStack()[stack.getSp() - 1]}")

    service.push_data(stack, 30)
    print(f"SP = {stack.getSp()}: stack[{stack.getSp() - 1}] = {stack.getStack()[stack.getSp() - 1]}")

    popped_value = service.pop_data(stack)
    print(f"Popped value = {popped_value}, SP = {stack.getSp()}, Stack = {stack.getStack()}")

if __name__ == "__main__":
    main()
