package Java;

import java.util.Scanner;

public class Java14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = sc.nextInt();
        int max = num;
        int min = num;
        // 최댓값과 최솟값을 동시에 출력하는 코드
        for (int i = 1; i < n; i ++) {
            num = sc.nextInt();
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        System.out.println("최댓값: " + max);
        System.out.println("최솟값: " + min);
    }
}

