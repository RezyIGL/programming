class Program
{
    public static void Main()
    {
        int[] a = new int[5];

        Random random = new();

        for (int i = 0; i < 10; i++){
            Console.WriteLine(random.Next(a.Length));
        }

    }
}