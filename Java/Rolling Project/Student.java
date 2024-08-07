public class Student
{
    private String name;
    private String address;
    private String phoneNo;
    private String email;

    public Student()
    {
        name = "No one";
        address = "No where";
        phoneNo = "No phoneNo";
        email = "No email";
    }

    public Student(String name, String adress, String phoneNo, String email)
    {
        this.name = name;
        this.address = adress;
        this.phoneNo = phoneNo;
        this.email = email;
    }

    public void display()
    {
        System.out.println("Name : " + name);
        System.out.println("Address : " + address);
        System.out.println("phoneNo : " + phoneNo);
        System.out.println("email : " + email);
    }

    public String getName() {
        return name;
    }

    public String getAddress() {
        return address;
    }

    public String getPhoneNo() {
        return phoneNo;
    }

    public String getEmail() {
        return email;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setPhoneNo(String phoneNo) {
        this.phoneNo = phoneNo;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "Student [name=" + name + ", address=" + address + ", phoneNo=" + phoneNo + ", email=" + email + "]";
    }


    
    
}