#include <iostream>
#include <vector>
#include <algorithm>


long long BinaryPow(int number, int pow)
{
    long long result{ 1 };
    while(pow)
    {
        if (pow & 1)
            result *= number;
        number *= number;

        pow >>= 1;
    }
        return result;
}

void ArrayRadixSort(std::vector<int>& array)
{
    std::vector<std::vector<int>> digits(10);
    int maxItem = *(std::max_element(array.begin(), array.end()));
    int radixes{};
    while (maxItem)
    {
        radixes++; 
        maxItem /= 10;
    }
    for (int r{}; r < radixes; r++)
    {
        for (int d{}; d < digits.size(); d++)
            digits[d].clear();
        for (int item : array)
        {
            int digit = (item / BinaryPow(10,r))%10;
            digits[digit].push_back(item);
        }

        array.clear();

        for (int d{}; d < digits.size(); d++)
        {
            for (auto item : digits[d])
                array.push_back(item);
        }
    }
}


int main()
{
    srand(time(nullptr));
    std::vector<int> array;

    for (int i = 0; i < 10; ++i)
    {
        array.push_back( rand() % 1000 );
    }
    for (int i = 0; i < 10; ++i)
    {
        std::cout << array.at(i) << '\t';
    }

    ArrayRadixSort(array);

    std::cout << std::endl;
    for (int i = 0; i < 10; ++i)
    {
        std::cout << array.at(i) << '\t';
    }


    return 0;
}

