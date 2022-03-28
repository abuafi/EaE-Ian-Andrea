import Enums.Algorithm;
import Enums.ArraySize;
import Enums.ArrayStatus;
import Enums.Type;
import Sorters.Sorter;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Instance<T extends Comparable<T>> {
    Type<T> type;
    Algorithm algo;
    ArraySize size;
    ArrayStatus status;

    private final Random random = new Random(0);

    public Instance(Type<T> type, Algorithm algo, ArraySize size, ArrayStatus status) {
        this.type = type;
        this.algo = algo;
        this.size = size;
        this.status = status;
    }

    public List<Long> run() {
        List<Long> times = new ArrayList<>();
        Sorter<T> sorter = algo.create(type.getC());
        int iterations = 500;
        while(iterations > 0) {
            T[] list = type.elements(size, status, random);
            long start = System.nanoTime();
            sorter.sort(list);
            long end = System.nanoTime();
            times.add(end - start);
            iterations--;
        }
        System.out.println(toString());
        return times;
    }

    public String toString() {
        return algo + " " + size + " " + type.name() + " " + status;
    }

}
