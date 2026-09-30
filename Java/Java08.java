package Java;

import java.util.Scanner;

public class Java08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 자릿수를 세어 출력하는 코드
        int count = 0;
        while (n > 0) {
            n /= 10;
            count++;
        }
        System.out.println(count + "자리");
    }
}
