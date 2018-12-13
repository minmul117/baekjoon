using System;

namespace _2438 
{
    public class _2438
    {
        public void solver()
        {
            int count = Int32.Parse(Console.ReadLine());
            for (int i = 1; i <= count; i++)
            {
                char[] star = new char[i];
                for (int j = 0; j < i; j++)
                {
                    star[j] = '*';
                }
                String result = new String(star);
                Console.WriteLine(result);
            }
        }
    }
}