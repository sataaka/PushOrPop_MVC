# dao/push.py

from abc import ABC, abstractmethod
from entity.Filed import Filed

class Push(ABC):
    @abstractmethod
    def push(self, stack: Filed, data: int):
        pass
