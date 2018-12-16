using System;
using System.Collections.Generic;

namespace _1003
{
    public class _1003
    {
        public void solve()
        {
            int count = Int32.Parse(Console.ReadLine());
            Dictionary<int, int> one_cache = new Dictionary<int, int>();
            Dictionary<int, int> zero_cache = new Dictionary<int, int>();
            one_cache[1] = 1;
            one_cache[0] = 0;
            zero_cache[2] = 1;
            zero_cache[1] = 0;
            zero_cache[0] = 1;
            for (int i = 0; i < count; i++)
            {
                int n = Int32.Parse(Console.ReadLine());
                fibonacci_dynamic(n, ref one_cache);
                fibonacci_dynamic(n, ref zero_cache);
                Console.WriteLine("{0} {1}", zero_cache[n], one_cache[n]);
            }
        }

        public static int fibonacci_dynamic(int n, ref Dictionary<int, int> cache)
        {
            if(!cache.ContainsKey(n))
            {
                cache[n] = fibonacci_dynamic(n - 1, ref cache) + fibonacci_dynamic(n - 2, ref cache);
            }
            return cache[n];
        }
    }
}