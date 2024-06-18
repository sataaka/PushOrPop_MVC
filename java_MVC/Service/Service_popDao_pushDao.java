package Service;

import entity.Filed;

public interface Service_popDao_pushDao {
    void pushData(Filed stack, int data);
    int popData(Filed stack);
}
