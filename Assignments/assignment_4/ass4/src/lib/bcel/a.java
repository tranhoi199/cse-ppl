/* a.java */

public class a {
    public static void main(String[] args) {
        System.out.println(foo());
    }

    public static int foo() {
        int a = 5;
        if (a > 2) {
            while (a > 0) {
                a = 5;
                if (a > 5) return 6; else a = 5;
            }
            a = 7;
        }
        return 4;
    }
}