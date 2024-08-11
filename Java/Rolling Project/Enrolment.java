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
        student.setName(in.acceptStringInput("Please enter your name"));
        student.setAddress(in.acceptStringInput("Please enter your address"));
        student.setPhoneNo(in.acceptStringInput("Please enter your phone number"));
        student.setEmail(in.acceptStringInput("Please enter your email"));
    }

    public void inputUnitDetails()
    {
        Input in = new Input();
        unit.setUnitCode(in.acceptStringInput("Please enter your unit code"));
        unit.setUnitDescription(in.acceptStringInput("Please enter your unit description"));
        unit.setCreditPoint(in.acceptIntInput("Please enter your credit points"));
    }

    @Override
    public String toString()
    {
        return "Enrolment [date=" + date + ", student=" + student + ", unit=" + unit + "]";
    }

    public static void main(String[] args) {
        
    }

}