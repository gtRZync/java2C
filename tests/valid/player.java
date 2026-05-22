class Player {
    private int x;
    private int y;
    //public String ___field;

    public Player(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void move(int x, int y) {
        this.x = this.x + x;
        this.y = this.y + y;
    }

    public static void main(String[] args) {
        Player p = new Player(100, 130);
        p.move(20, -30);
    }
}