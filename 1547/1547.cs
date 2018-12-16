using System;
using System.Collections.Generic;

namespace _1547 
{
    public class _1547
    {
        public void solve()
        {
            Dictionary<int, int> balls = new Dictionary<int, int>();
            balls[1] = 1;
            balls[2] = 2;
            balls[3] = 3;

            int count = Int32.Parse(Console.ReadLine());
            for (int i = 0; i < count; i++)
            {
                var line = Console.ReadLine();
                var splited = line.Split(' ');
                int first = Int32.Parse(splited[0]);
                int second = Int32.Parse(splited[1]);

                var temp = balls[first];
                balls[first] = balls[second];
                balls[second] = temp;
            }
            foreach(KeyValuePair<int, int> entity in balls)
            {
                if (entity.Value == 1)
                {
                    Console.WriteLine(entity.Key);
                    break;
                }
            }
        }
    }
}