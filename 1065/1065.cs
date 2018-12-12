using System;

namespace _1065
{
    class _1065
    {
        static void solver()
        {
            int max_number = Int32.Parse(Console.ReadLine());
            int count = 0;

            if (max_number < 100)
            {
                Console.WriteLine("{0}", max_number);
            }
            else
            {
                count = 99;
                for(int i = 100; i <= max_number; i++)
                {
                    var number_array = i.ToString().ToCharArray();
                    // length는 최대 3까지다.
                    var temp = Char.GetNumericValue(number_array[0]) - Char.GetNumericValue(number_array[1]);
                    var temp2 = Char.GetNumericValue(number_array[1]) - Char.GetNumericValue(number_array[2]);
                    if(temp == temp2)
                    {
                        count++;
                    }
                }
                Console.WriteLine("{0}", count);
            }
        }
    }
}
