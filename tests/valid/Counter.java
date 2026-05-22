class Counter {
    private int count;

    public Counter() {
        count = 0;
    }

    public void bump() {
        int finished = 0;
        while (finished == 0) {
            count = count + 1;
            finished = 1;
        }
    }

    public static void main(String[] args) {
        Counter c = new Counter();
        c.bump();
    }
}
