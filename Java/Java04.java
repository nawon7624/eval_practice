package Java;

import java.util.Scanner;

public class Java04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 양의 짝수 / 양의 홀수 / 양수 아님을 판별해 출력하는 코드
        if (n > 0) {
            if (n % 2 == 0) {
                System.out.println("양의 짝수");
            } else {
                System.out.println("양의 홀수");
            }
        } else {
            System.out.println("양수 아님");
        }
    }
}