package Enums;

import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.function.BiConsumer;

public enum ArrayStatus {

    AS((l, r) -> {}),
    RG(Collections::shuffle),
    SB((l, r) -> Collections.reverse(l))
    ;

    private final BiConsumer<List<?>, Random> listFunction;

    ArrayStatus(BiConsumer<List<?>, Random> listFunction) {
        this.listFunction = listFunction;
    }

    public void apply(List<?> l, Random r) {
        listFunction.accept(l, r);
    }
}
