public enum Types {
    INTEGER(Integer.class),
    CHAR(Character.class),
    DUMMY(Dummy.class)
    ;

    private final Class<? extends Comparable<?>> c;

    Types(Class<? extends Comparable<?>> c) {
        this.c = c;
    }
}
