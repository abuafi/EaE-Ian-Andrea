package Enums;

import Sorters.Sorter;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ThreadLocalRandom;
import java.util.function.Function;
import java.util.stream.IntStream;

public class Types<T extends Comparable<T>> {
   public static final Random rand = new Random();
   public static final Types<Integer> INTEGER = new Types<>((Integer s) -> IntStream.range(1, s).boxed().toArray(Integer[]::new), Integer.class);
//   CHAR(),
//   DUMMY()
   ;

   private final Function<Integer, T[]> c;
   private final Class<T> tClass;

   Types(Function<Integer,T[]> c, Class<T> tClass) {
       this.c = c;
       this.tClass = tClass;
   }

   public T[] elements(ArraySize size) {
      return c.apply(size.get());
   }

   public Class<T> getC() {
      return tClass;
   }
}
