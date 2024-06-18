# serviceImpl/service_popDao_pushDaoImpl.py

from service.ServicePopDaoPushDao import ServicePopDaoPushDao
from dao.daoImpl.PushImpl import PushImpl
from dao.daoImpl.PopImpl import PopImpl
from entity.Filed import Filed

class ServicePopDaoPushDaoImpl(ServicePopDaoPushDao):
    def __init__(self):
        self.pusher = PushImpl()
        self.popper = PopImpl()

    def push_data(self, stack: Filed, data: int):
        self.pusher.push(stack, data)

    def pop_data(self, stack: Filed) -> int:
        return self.popper.pop(stack)
