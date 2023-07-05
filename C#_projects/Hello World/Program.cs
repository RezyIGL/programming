namespace HelloWorldBigTextFirstProgram
{
    class mainClassToEnterCodeUsage
    {
        static void Main(String[] args)
        {
            Hello obj = new Hello();
            obj.sayHello();
        }
    }

    class Hello
    {
        public void sayHello()
        {
            Console.WriteLine("Hello, oh mighty C# world! :p");
        }
    }
}