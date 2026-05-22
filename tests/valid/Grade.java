class Grade {
    public int classify(int score) {
        if (score == 100) {
            return 1;
        } else {
            return 0;
        }
    }

    public static void main(String[] args) {
        Grade g = new Grade();
        g.classify(100);
    }
}
