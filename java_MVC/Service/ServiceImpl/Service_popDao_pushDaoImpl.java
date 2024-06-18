package Service.ServiceImpl;

import dao.Push;
import dao.Pop;
import dao.daoImpl.PushImpl;
import dao.daoImpl.PopImpl;
import entity.Filed;
import Service.Service_popDao_pushDao;

public class Service_popDao_pushDaoImpl implements Service_popDao_pushDao {
    private Push pushDao = new PushImpl();
    private Pop popDao = new PopImpl();

    @Override
    public void pushData(Filed stack, int data) {
        pushDao.push(stack, data);
    }

    @Override
    public int popData(Filed stack) {
        return popDao.pop(stack);
    }
}
