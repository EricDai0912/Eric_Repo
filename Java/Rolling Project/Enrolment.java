public class Enrolment {

    private String date;
    private Student student;
    private Unit unit;

    public Enrolment()
    {
        date = "No date";
    }

    public Enrolment(String date, Student student, Unit unit)
    {
        this.date = date;
        this.student = student;
        this.unit = unit;
    }

    public void display()
    {
        System.out.println("Date: " + date + " student: " + student + " unit: " + unit);
    }

    public String getDate()
    {
        return date;
    }

    public Student getStudent()
    {
        return student;
    }

    public Unit getUnit()
    {
        return unit;
    }

    public void setDate(String date)
    {
        this.date = date;
    }

    public void setStudent(Student student)
    {
        this.student = student;
    }

    public void setUnit(Unit unit)
    {
        this.unit = unit;
    }

    public void inputStudentDetails()
    {
        Input in = new Input();
        Validation valid = new Validation();
        String name = in.acceptStringInput("Please enter your name");
        String address = in.acceptStringInput("Please enter your address");
        String phoneNo = in.acceptStringInput("Please enter your phone number");
        String email = in.acceptStringInput("Please enter your email");
        if (!valid.isBlank(name) && valid.stringLengthInRange(name, 12, 3))
        {
            student.setName(name);
        }
        if (!valid.isBlank(address) && valid.stringLengthInRange(address, 100, 25))
        {
            student.setAddress(address);
        }
        if (!valid.isBlank(phoneNo) && valid.stringLengthInRange(phoneNo, 10, 10) && valid.isStringNumeric(phoneNo))
        {
            student.setPhoneNo(phoneNo);
        }
        if (!valid.isBlank(email))
        {
            student.setEmail(email);
        }
    }

    public void inputUnitDetails()
    {
        Input in = new Input();
        Validation valid = new Validation();
        String unitCode = in.acceptStringInput("Please enter your unit code");
        String unitDescription = in.acceptStringInput("Please enter your unit description");
        int creditPoint = in.acceptIntInput("Please enter your credit points");
        if (valid.stringLengthInRange(unitCode, 7, 7))
        {
            unit.setUnitCode(unitCode);
        }
        if (valid.stringLengthInRange(unitDescription, 250, 1) && !valid.isBlank(unitDescription))
        {
            unit.setUnitDescription(unitDescription);
        }
        
        
        unit.setCreditPoint(creditPoint);
    }

    @Override
    public String toString()
    {
        return "Enrolment [date=" + date + ", student=" + student + ", unit=" + unit + "]";
    }

    public void startProgram()
    {
        boolean flag = true;
        while (flag)
        {
            Input in = new Input();
            int option = in.acceptIntInput("Please enter the option: 1.inputStudentDetails  2.inputUnitDetails  3. Exit");
            switch(option)
            {
                case 1:
                    inputStudentDetails();
                    break;
                case 2:
                    inputUnitDetails();
                    break;
                case 3:
                    break;
             }
        }
    }

    public static void main(String[] args) {
        Enrolment enrolment = new Enrolment();
        enrolment.startProgram();
    }

}