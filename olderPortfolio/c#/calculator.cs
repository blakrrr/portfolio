using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace testing
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("add, subtract, multiply, or divide? ");
            string operation = Console.ReadLine();

            while (operation != "add" && operation != "subtract")
            {
                Console.Write("silly goose that's not an operation, do add or subtract: ");
                operation = Console.ReadLine();
            }

            Console.Write("first value: ");
            string firstValue = Console.ReadLine();
            Console.Write("second value: ");
            string secondValue = Console.ReadLine();
            int firstValueInt = Int16.Parse(firstValue);
            int secondValueInt = Int16.Parse(secondValue);
            int finalValueAdd = firstValueInt + secondValueInt;
            int finalValueSub = firstValueInt - secondValueInt;

            if (operation == "add")
                Console.Write("your result is: " + finalValueAdd);
            if (operation == "subtract")
                Console.Write("your result is: " + finalValueSub);

            Console.ReadLine();
        }
    }
}
