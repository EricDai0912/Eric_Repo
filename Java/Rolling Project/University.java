import java.util.ArrayList;

/**
 * University
 */
public class University 
{

    private ArrayList<Enrolment> enrolments;

    public University()
    {
        enrolments = new ArrayList<>();
    }

    public University(ArrayList<Enrolment> enrolments)
    {
        this.enrolments = enrolments;
    }

    public void display()
    {
        System.out.println(toString());
    }

    public ArrayList<Enrolment> getEnrolments()
    {
        return enrolments;
    }

    public int getEnrolmentsSize()
    {
        return enrolments.size();
    }

    public Enrolment getSpecificEnrolment(int index)
    {
        if (index >= 0 && index < enrolments.size())
        {
            return enrolments.get(index);
        }else
        {
            return null;
        }
    }

    public void removeEnrolment(int index)
    {
        if (index >= 0 && index < enrolments.size())
        {
            enrolments.remove(index);
        }
    }

    public void setEnrollments(ArrayList<Enrolment> enrolments)
    {
        this.enrolments = enrolments;
    }

    public void setSpecificEnrolment(int index, Enrolment enrolment)
    {
        if (index >= 0 && index < enrolments.size())
        {
            enrolments.set(index, enrolment);
        }
    }

    public String toString()
    {
        StringBuffer enrols = new StringBuffer();
        for (Enrolment enrolment : enrolments)
        {
            enrols.append(enrolment.toString() + "\n");
        }
        return enrols.toString();
    }

    public void addEnrolment(Enrolment enrolment)
    {
        enrolments.add(enrolment);
    }
}