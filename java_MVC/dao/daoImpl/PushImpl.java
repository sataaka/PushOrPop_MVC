package dao.daoImpl;

import dao.Push;
import entity.Filed;

public class PushImpl implements Push {

    @Override
    public void push(Filed stack, int data) {
        if (stack.getSp() < stack.getStack().length) {
            stack.getStack()[stack.getSp()] = data;
            stack.setSp(stack.getSp() + 1);
        } else {
            System.out.println("スタック領域に空きがない");
        }
    }
}
