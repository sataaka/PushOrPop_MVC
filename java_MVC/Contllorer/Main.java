package Contllorer;

import entity.Filed;
import Service.Service_popDao_pushDao;
import Service.ServiceImpl.Service_popDao_pushDaoImpl;

public class Main {
    public static void main(String[] args) {
        Filed stack = new Filed(5); // スタックのサイズを指定
        Service_popDao_pushDao service = new Service_popDao_pushDaoImpl();

        service.pushData(stack, 10);
        System.out.println("SP = " + stack.getSp() + ": stack[" + stack.getStack()[stack.getSp() - 1] + "]");
        service.pushData(stack, 20);
        System.out.println("SP = " + stack.getSp() + ": stack[" + stack.getStack()[stack.getSp() - 1] + "]");
        service.pushData(stack, 30);
        System.out.println("SP = " + stack.getSp() + ": stack[" + stack.getStack()[stack.getSp() - 1] + "]");

        System.out.println("Popped value: " + service.popData(stack) + ", SP = " + stack.getSp());
        System.out.println("Popped value: " + service.popData(stack) + ", SP = " + stack.getSp());
        System.out.println("Popped value: " + service.popData(stack) + ", SP = " + stack.getSp());

        service.pushData(stack, 40);
        service.pushData(stack, 50);

        System.out.println("Popped value: " + service.popData(stack) + ", SP = " + stack.getSp());
        
        // スタックの内容を表示
        for (int i = 0; i <= stack.getSp(); i++) {
            System.out.println("Stack[" + i + "] = " + stack.getStack()[i]);
        }
    }
}
