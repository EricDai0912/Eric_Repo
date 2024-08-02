public class Unit {

    private String unitCode;
    private String unitDescription;
    private int creditPoint;

    
    public Unit() 
    {
        unitCode = "No unitCode";
        unitDescription = "No unitDescriptiob";
        creditPoint = 0;
    }


    public Unit(String unitCode, String unitDescription, int creditPoint) {
        this.unitCode = unitCode;
        this.unitDescription = unitDescription;
        this.creditPoint = creditPoint;
    }

    public void display()
    {
        System.out.println("unitCode: " + unitCode + " unitDescription: " + unitDescription + 
        " creditPoint: " + creditPoint);
    }

    public String getUnitCode() {
        return unitCode;
    }


    public String getUnitDescription() {
        return unitDescription;
    }


    public int getCreditPoint() {
        return creditPoint;
    }


    public void setUnitCode(String unitCode) {
        this.unitCode = unitCode;
    }


    public void setUnitDescription(String unitDescription) {
        this.unitDescription = unitDescription;
    }


    public void setCreditPoint(int creditPoint) {
        this.creditPoint = creditPoint;
    }


    @Override
    public String toString() {
        return "Unit [unitCode=" + unitCode + ", unitDescription=" + unitDescription + ", creditPoint=" + creditPoint
                + "]";
    }

    
}