package Java;

import java.util.Scanner;

public class Java10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x;
        // 유효한 값이 들어오면 입력값을 출력하는 코드
        do {
            x = sc.nextInt();
        } while (x < 1 || x > 100);
        System.out.println("입력값: " + x);
    }
}
