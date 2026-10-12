package Java;

import java.util.Scanner;

public class Java12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 제곱의 합을 출력하는 코드
        int sum = 0;
        for (int i = 1; i <= n; i ++) {
            sum += i*i;
        }
        System.out.println("제곱합: " + sum);
    }
}

