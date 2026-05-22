class Battery {
    public int level;

    public Battery(int level) {
        this.level = level;
    }

    public int drain(int amount) {
        if (level == 0) {
            return 0;
        }
        level = level - amount;
        return level;
    }

    public static void main(String[] args) {
        Battery b = new Battery(100);
        b.drain(25);
    }
}
