import java.util.Scanner;
public class Compare {
    private double number1;
    private double number2;
    private double number3;
    
    
    public Compare() {
        number1 = 0;
        number2 = 0;
        number3 = 0;
    }

    

    public Compare(double number1, double number2, double number3) {
        this.number1 = number1;
        this.number2 = number2;
        this.number3 = number3;
    }



    public double getNumber1() {
        return number1;
    }




    public double getNumber2() {
        return number2;
    }




    public double getNumber3() {
        return number3;
    }

    


    public void setNumber1(double number1) {
        this.number1 = number1;
    }




    public void setNumber2(double number2) {
        this.number2 = number2;
    }




    public void setNumber3(double number3) {
        this.number3 = number3;
    }

    public String compareNumbers()
    {
        double largestNumber;
        double secondNumber;
        double thirdNumber;
        if (number1 >= number2 && number1 >= number3)
        {
            if (number2 >= number3) 
            {
                largestNumber = number1;
                secondNumber = number2;
                thirdNumber = number3;
            }
            else
            {
                largestNumber = number1;
                secondNumber = number3;
                thirdNumber = number2;
            }
        }
        else if (number2 >= number1 && number2 >= number3)
        {
            if (number1 >= number3)
            {
                largestNumber = number2;
                secondNumber = number1;
                thirdNumber = number3;
            }
            else
            {
                largestNumber = number2;
                secondNumber = number3;
                thirdNumber = number1;
            }

        }
        else
        {
            if (number1 >= number2)
            {
                largestNumber = number3;
                secondNumber = number1;
                thirdNumber = number2;
            }
            else
            {
                largestNumber = number3;
                secondNumber = number2;
                thirdNumber = number1;
            }
        }

        return "Descending order : " + largestNumber + "," + secondNumber + "," + thirdNumber;
    }


    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.println("Please enter three numbers seprate with a space:");
        Compare comp = new Compare(console.nextDouble(),console.nextDouble(),console.nextDouble());
        System.out.println(comp.compareNumbers());
        
    }
}