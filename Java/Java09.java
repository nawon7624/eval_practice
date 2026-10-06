package Java;

import java.util.Scanner;

public class Java09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;
        int sum = 0;
        // 0이 입력되면 종료 후 합계를 출력하는 코드
        do {
            n = sc.nextInt();
            sum += n;
        } while (n != 0);
        System.out.println("합계: " + sum);
    }
}
