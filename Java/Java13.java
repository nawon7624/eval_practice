package Java;

import java.util.Scanner;

public class Java13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 평균을 구해 출력하는 코드
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            sum += num;  
        }
        double avg = (double) sum / n;
        System.out.printf("평균: %.2f%n", avg);
    }
}