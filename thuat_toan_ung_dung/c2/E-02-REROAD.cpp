// #include <stdio.h>
#include <bits/stdc++.h>
#include <iostream>


// void print_list(int& x)
// {
//     for (auto i : x.begin())
//     {
//         std::cout<< i << " ";
//     }
//     std::cout<<"\n";
// }

int main()
{
    // std::ios::sync_with_stdio(false);
    int n = 0;
    std::cin >> n;

    int roads[n];

    int num_road = 0;
    int temp = 0;

    for (int i = 0; i < n; i++)
    {   
        std::cin >> roads[i];
        // std::cout<<"roads[i] : "<<roads[i]<<"\n";
    }

    for (int i = 0; i < n; i++)
    {
        if (i==0)
        {
            num_road++;
            temp = roads[i];
        }
        else
        {
            if (temp != roads[i])
            {
                num_road++;
                temp = roads[i];
            }
        }
    }

    int q = 0;
    std::cin >> q;
    int q_i, c_i;

    int prev, next, recent;

    for (int i = 0; i < q; i++)
    {   
        // for (auto r : roads)
        // {
        //     std::cout<<r <<" ";

        // }
        // std::cout<<"\n";

        std::cin >> q_i;
        std::cin >> c_i;
        q_i = q_i - 1;
        prev = roads[q_i - 1];
        next = roads[q_i + 1];
        recent = roads[q_i];

        if (recent == c_i)
        {
            std::cout << num_road << "\n";
            continue;
        }
        else if (q_i > 0 && q_i < n - 1)
        {
            if (prev == next)
            {
                if (recent == prev) //111 222 333
                {
                    if (c_i != recent) num_road = num_road + 2;
                }
                else // 121 212 313 ...
                {
                    if (c_i == prev) num_road = num_road - 2;
                }    
            }
            else if (prev == recent || recent == next) //221 223 || 122 133 233 211...
            {
                if (c_i != prev && c_i != next) num_road++;

            }
            else  // 123 132 321 
            {
                if (c_i == prev || c_i == next) num_road--;
            }
        }
        else if (q_i == 0)
        {
            if (c_i != next && recent == next) num_road++;
            if (c_i == next && recent != next) num_road--;
        }
        else if (q_i == n - 1)
        {
            if (c_i != prev && recent == prev) num_road++;
            if (c_i == prev && recent != prev) num_road--;

        }

        roads[q_i] = c_i;

        std::cout << num_road << "\n";
    }

    
}