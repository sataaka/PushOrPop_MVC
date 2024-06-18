# dao/pop.py

from abc import ABC, abstractmethod
from entity.Filed import Filed

class Pop(ABC):
    @abstractmethod
    def pop(self, stack: Filed) -> int:
        pass
