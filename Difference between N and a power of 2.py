import java.util.Scanner;

public class MinAbsoluteDifference {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int left = (int) Math.pow(2, Math.floor(Math.log(N) / Math.log(2)));
        int right = left * 2;
        int minDifference = Math.min(N - left, right - N);
        System.out.println(minDifference);
    }
}
