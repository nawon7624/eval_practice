package Java;

import java.util.Scanner;

public class Java18 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // TODO: for 로 1..N 순회하며 약수면 공백 구분으로 출력. 끝에 줄바꿈.
        // n의 약수를 나열하는 함수 정의
        for (i=1; i < n; i++) {
            if (n % i == 0) {
                System.out.println(n);
            } 
        }
    }
}
