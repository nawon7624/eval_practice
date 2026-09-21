package Java;

import java.util.Scanner;

public class Java01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int day = sc.nextInt();
        // 평일, 주말을 분류하여 출력하는 코드
        switch (day) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                System.out.println("평일");
                break;
            case 6:
            case 7:
                System.out.println("주말");
                break;
            default:
                System.out.println("잘못된 입력");
                break;
        }
    }
}