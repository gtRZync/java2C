class MathUtils {
    public int Sum(int a, int b) {
        return a + b;
    }

    public static int Factorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * Factorial(n-1);
    } 

    public static void main(String[] args) {
        MathUtils utils = new MathUtils();
        utils.Sum(10, 5);
        Factorial(5);
    }
}