package Enums;

public enum ArraySize {
    SMALL(10),
    MEDIUM(100),
    LARGE(1000)
    ;

    private final int size;

    ArraySize(int size) {
        this.size = size;
    }

    public int get() {
        return size;
    }
}
