package Java;

import java.util.Scanner;

public class Java15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x;
        // 양수를 받을 때까지 반복 입력받는 코드
        do {
            x = sc.nextInt();
        } while (x <= 0);
        System.out.println("입력값: " + x);
    } 
}