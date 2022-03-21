package Enums;

public class Dummy implements Comparable<Dummy> {

    private final Integer i;

    public Dummy(Integer i) {
        this.i = i;
    }

    @Override
    public int compareTo(Dummy o) {
        try {
            Thread.sleep(1);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return i.compareTo(o.i);
    }
}
