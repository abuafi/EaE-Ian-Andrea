package Enums;

public class Dummy implements Comparable<Dummy> {

    private final Integer i;
    private int counter = 100;

    public Dummy(Integer i) {
        this.i = i;
    }

    @Override
    public int compareTo(Dummy o) {
        if (counter > 0) {
            // Busy wait 1000 nanoseconds to simulate a complex object being compared.
            long start = System.nanoTime();
            while(System.nanoTime() < start + 1000);
            counter--;
        }
        return i.compareTo(o.i);
    }

    public String toString() {
        return i+"";
    }
}
