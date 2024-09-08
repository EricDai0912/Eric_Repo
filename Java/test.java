import java.util.Scanner;

public class Test {
    public boolean isPrime(int number)
    {
        if (number > 1)
        {
            for (int i = 2; i < number / 2; i++)
            {
                if (number % i == 0)
                {
                    return false;
                }
            }
            return true;
        }else{
            return false;
        }
    }
    public static void main(String[] args) {
        Test t = new Test();
        Scanner console = new Scanner(System.in);
        System.out.println("Please enter a number to check if it is prime number:");
        int number = console.nextInt();
        if (t.isPrime(number))
        {
            System.out.println("This number is a prime number");
        }else
        {
            System.out.println("This number is not a prime number");
        }
    }
}
