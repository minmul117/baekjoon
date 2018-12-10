using System;

namespace _1075
{
    class _1075
    {
        static void result(string[] args)
        {
            while(true)
            {
                var N = Console.ReadLine();
                var F = Console.ReadLine();
                if (N == null || F == null)
                {
                    break;
                }
                else
                {
                    int result = calculate(N, F);
                }
            }
        }

        static int calculate(string N, string F)
        {
            int n = Int32.Parse(N);
            int f = Int32.Parse(F);
            
            int remainder = n % f;
            int centurion_rest = n % 100; // 99
            int except_centurion = n - centurion_rest; // 900
            int result = Math.Abs((except_centurion % f) - f) % f;
            Console.WriteLine("{0:D2}", result);
            return result;
        }
    }
}