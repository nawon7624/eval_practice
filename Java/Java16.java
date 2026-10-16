package Java;

import java.util.Scanner;

public class Java16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 양수 / 음수 개수를 출력하는 코드
        int pos = 0;
        int neg = 0;
        for (int i = 0; i < n; i ++) {
            int num = sc.nextInt();
            if (num > 0) {
                pos ++;
            }else if (num < 0) {
                neg ++;
            }
        }
        System.out.println("양수: " + pos);
        System.out.println("음수: " + neg);
    }
}

