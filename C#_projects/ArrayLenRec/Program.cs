class main
{

    public static int func(int[] array)
    {
        int myArrLen = array.Length;
        if (myArrLen == 0)
        {
            return 0;
        }
        else
        {
            return 1 + func(array[1..]);
        }
    }

    public static void Main(String[] args)
    {
        Console.WriteLine(func(new int[] { 0, 1, 2, 3, 4, 5 })); // 6
    }

}