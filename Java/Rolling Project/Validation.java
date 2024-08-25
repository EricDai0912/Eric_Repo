public class Validation {
    public Validation()
    {

    }

    public boolean isBlank(String value)
    {
        if (value.trim().length() > 0)
        {
            return false;
        }else
        {
            return true;
        }
    }

    public boolean stringLengthInRange(String value, int max, int min)
    {
        if (value.trim().length() <= max && value.trim().length() >= min)
        {
            return true;
        } else
        {
            return false;
        }
    }

    public boolean isCharacterNumeric(char c)
    {
        if (Character.isDigit(c))
        {
            return true;
        }else
        {
            return false;
        }
    }

    public boolean isStringNumeric(String s)
    {
        int total = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (isCharacterNumeric(s.charAt(i)))
            {
                total ++;
            }else
            {
                break;
            }
        }

        if (total == s.length())
        {
            return true;
        }else
        {
            return false;
        }
    }

}