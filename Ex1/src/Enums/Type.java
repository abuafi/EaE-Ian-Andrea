package Enums;

import java.util.*;
import java.util.function.Function;
import java.util.stream.IntStream;

public class Type<T extends Comparable<T>> {
   // To add another type, add another static variables and a function that takes an integer as the size and creates a sorted array of that type.
   public static final Type<Integer> INTEGER = new Type<>((Integer s) -> IntStream.range(1, s).boxed().toArray(Integer[]::new), Integer.class);
   public static final Type<Dummy> DUMMY = new Type<>((Integer s) -> IntStream.range(1, s).mapToObj(Dummy::new).toArray(Dummy[]::new), Dummy.class);
   public static final Type<String> STRING = new Type<>((Integer s) -> IntStream.range(1, s).mapToObj(i -> String.format("%04d",i)).toArray(String[]::new), String.class);
   public static final List<Type<?>> TYPES = List.of(INTEGER, DUMMY, STRING);

   private final Function<Integer, T[]> c;
   private final Class<T> tClass;

   Type(Function<Integer,T[]> c, Class<T> tClass) {
       this.c = c;
       this.tClass = tClass;
   }

   /**
    * Given the size and status variables, generates the array the Instance needs to sort.
    * @param size the array size variable of the instance
    * @param status the array status variable of the instance
    * @param random the Random generator of the Instance
    * @return the array to sort
    */
   public T[] elements(ArraySize size, ArrayStatus status, Random random) {
      T[] list = c.apply(size.get());
      status.apply(Arrays.asList(list), random);
      return list;
   }

   public Class<T> getC() {
      return tClass;
   }

   public String name() {
      return tClass.getSimpleName().toUpperCase(Locale.ROOT);
   }
}
