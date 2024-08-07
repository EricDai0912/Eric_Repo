import java.util.Scanner;
public class Input {

    private Scanner console;

    public Input(){
        console = new Scanner(System.in);
    }

    public char acceptCharInput(String prompt, int i)
    {
        System.out.println(prompt);
        char input = console.nextLine().charAt(i);
        return input;
    }

    public double acceptDoubleInput(String prompt)
    {
        System.out.println(prompt);
        double input = console.nextDouble();
        return input;
    }

    public int acceptIntInput(String prompt)
    {
        System.out.println(prompt);
        int input = console.nextInt();
        return input;
    }

    public String acceptStringInput(String prompt)
    {
        System.out.println(prompt);
        String input = console.nextLine();
        return input;
    }
}