package entity;

public class Filed {
    private int[] stackArray;
    private int sp; // スタックポインタ

    public Filed(int size) {
        stackArray = new int[size];
        sp = 0;
    }

    public int[] getStack() {
        return stackArray;
    }

    public int getSp() {
        return sp;
    }

    public void setSp(int sp) {
        this.sp = sp;
    }
}
