package Java;

import java.util.Scanner;

public class Java07 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 팩토리얼을 구해 출력하는 코드 정의
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        System.out.println(n + "! = " + result);
    }
}
