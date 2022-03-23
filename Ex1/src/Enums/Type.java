package Enums;

import java.util.*;
import java.util.function.Function;
import java.util.stream.IntStream;

public class Type<T extends Comparable<T>> {
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
