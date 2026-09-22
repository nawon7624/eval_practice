package Java;

import java.util.Scanner;

public class Java03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int isMember = sc.nextInt();
        int amount = sc.nextInt();
        // 할인대상 관련 출력하는 코드
        if ( isMember == 1 ) {
            if ( amount >= 10000 ) {
                System.out.println("10% 할인 대상");
            } else {
                System.out.println("할인 대상 아님");
            }
            } else {
                System.out.println("회원만 할인 가능");
        }
    }
}
