import Enums.Algorithm;
import Enums.ArraySize;
import Enums.Dummy;
import Enums.Types;
import Sorters.BubbleSortUntilNoChange;
import Sorters.Sorter;

import java.lang.reflect.GenericDeclaration;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.TypeVariable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Instance<T extends Comparable<T>> {

    Types<T> type;
    Algorithm algo;
    ArraySize size;

    public Instance(Types<T> type, Algorithm algo, ArraySize size) {
        this.type = type;
        this.algo = algo;
        this.size = size;
    }

    public static void main(String[] args) {
        int i = 0;
        List<Instance<?>> sorters = new ArrayList<>();
        sorters.add(new Instance<>(Types.INTEGER, Algorithm.BSUNC, ArraySize.LARGE));


        sorters.forEach(Instance::run);
    }

    public void run() {
        Sorter<T> sorter = algo.create(type.getC());
        T[] list = type.elements(size);
        long start = System.nanoTime();
        sorter.sort(list);
        long end = System.nanoTime();
        System.out.println(end - start);

    }

}
