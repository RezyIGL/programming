using System.Transactions;

namespace LinkedList
{
    class main
    {
        static void Main(String[] args)
        {
            LinkedList list1 = new LinkedList("aboba");

            LinkedList list2 = new LinkedList(0, 1);
            LinkedList l = new LinkedList(1, 2);

            for (int i = 2; i <= 10; i++)
            {
                l = new LinkedList(i, i+1);
            }

            Console.Write(list1.printData() + "\n");
            LinkedList x = list2;

            for (int i = 1; i <= 10; i++)
            {
                Console.Write(x.printData() + "\n");
                x = x.setNext();
            }

        }
    }

    class LinkedList
    {
        private dynamic? _val;
        private dynamic? _next;

        public LinkedList(dynamic? val = null, dynamic? next = null)
        {
            _val = val;
            _next = next;
        }

        public dynamic? printData()
        {
            return _val;
        }

        public dynamic? setNext()
        {
            return _next;
        }
    }

}