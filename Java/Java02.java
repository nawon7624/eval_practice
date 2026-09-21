package Java;

import java.util.Scanner;

public class Java02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        // 월별 일수를 출력하는 코드
        switch (month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                System.out.println("31일");
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                System.out.println("30일");
                break;
            case 2:
            System.out.println("28일");
            break;
            default:
                System.out.println("잘못된 월");
        }
    }
}
