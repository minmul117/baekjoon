using System;

namespace _1000
{
    class _1000
    {
        static void result(string[] args)
        {
            var number = Console.ReadLine();
            var a_b = number.Split(" ");
            Console.WriteLine(Int32.Parse(a_b[0]) + Int32.Parse(a_b[1]));
        }
    }
}
