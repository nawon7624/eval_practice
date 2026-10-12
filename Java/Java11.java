package Java;

import java.util.Scanner;

public class Java11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 양수의 합을 출력하는 코드
        int sum = 0;
        for (int i = 0; i < n; i ++) {
            int num = sc.nextInt();
            if (num > 0) {
                sum += num;
            }
        }
        System.out.println("양수 합: " + sum);
    }
}
