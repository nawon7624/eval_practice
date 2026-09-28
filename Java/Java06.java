package Java;

import java.util.Scanner;

public class Java06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // n개 정수의 합을 구하는 코드
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += sc.nextInt();
        }
        System.out.println("합계: " + sum);
    }
}