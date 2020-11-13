#include <bits/stdc++.h>
#include <iostream>

int n, b;

int result = 1000000000;
int temp_cost = 0;
int src;
bool check;

int main()
{
    
    std::ios::sync_with_stdio(false);
    std::cin >> n;
    int cost[2*n+1][2*n+1];
    for(int i = 0; i < 2*n + 1; i++)
    {
        for(int j = 0; j < 2*n + 1; j++)
        {
            std::cin>> cost[i][j];
        }
    }

    int point[n];
    for (int i = 1; i <= n; i++)
    {
        point[i-1] = i;
    }
    
    do {
        temp_cost = 0;
        src = 0;
        check = false;
        for (auto p: point)
        {
            if (cost[src][p] > 0)
            {
                temp_cost += cost[src][p] + cost[p][p+n];
                src = p+n;
            }
            else
            {
                check = true;
                break;
            }
        }

        if (check == false)
        {   
            if (cost[src][0] > 0)
            {
                if (temp_cost +cost[src][0] < result)
                    result = temp_cost+cost[src][0];
            }
            
        }

    } while ( std::next_permutation(point, point+n) );
    
    std::cout<< result;

    return 0;

}