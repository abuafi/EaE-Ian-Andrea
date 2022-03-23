package Enums;
import Sorters.*;

public enum Algorithm {

   BSPPI(),
   BSWN(),
   BSUNC();

   public <T extends Comparable<T>> Sorter<T> create(Class<T> c) {
      return switch (this) {
         case BSPPI -> new BubbleSortPassPerItem<T>();
         case BSWN -> new BubbleSortWhileNeeded<T>();
         case BSUNC -> new BubbleSortUntilNoChange<T>();
      };
   }

}
