# service/service_popDao_pushDao.py

from abc import ABC, abstractmethod
from entity.Filed import Filed

class ServicePopDaoPushDao(ABC):
    @abstractmethod
    def push_data(self, stack: Filed, data: int):
        pass

    @abstractmethod
    def pop_data(self, stack: Filed) -> int:
        pass
