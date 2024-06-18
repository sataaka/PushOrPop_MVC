package dao.daoImpl;

import dao.Pop;
import entity.Filed;

public class PopImpl implements Pop {

    @Override
    public int pop(Filed stack) {
        if (stack.getSp() > 0) {
                        //Filedクラスの変数に
            int value = stack.getStack()[stack.getSp() - 1];
            stack.setSp(stack.getSp() - 1);
            return value;
        } else {
            System.out.println("スタックが空です");
            return -999; // エラー値を返す
        }
    }
}