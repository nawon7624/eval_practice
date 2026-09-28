package Java;

import java.util.Scanner;

public class Java05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // n의 약수의 합을 구하는 코드
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                sum += i;
            }
        }
        System.out.println("약수 합: " + sum);
    }
}
