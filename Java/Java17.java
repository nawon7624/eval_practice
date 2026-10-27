package Java;

import java.util.Scanner;

public class Java17 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // n의 약수의 개수를 구하는 코드
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                count++;
            }
        }
        System.out.println("약수 개수: " + count);
    }
}

