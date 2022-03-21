package Enums;
import Sorters.*;

public enum Algorithm {

   BSPPI(BubbleSortUntilNoChange.class),
   BSWN(BubbleSortWhileNeeded.class),
   BSUNC(BubbleSortUntilNoChange.class);

   private final Class<? extends Sorter> c;

   Algorithm(Class<? extends Sorter> c) {
       this.c = c;
   }

   public <T extends Comparable<T>> Sorter<T> create(Class<T> c) {
      return switch (this) {
         case BSPPI -> new BubbleSortPassPerItem<T>();
         case BSWN -> new BubbleSortWhileNeeded<T>();
         case BSUNC -> new BubbleSortUntilNoChange<T>();
      };
   }

}
