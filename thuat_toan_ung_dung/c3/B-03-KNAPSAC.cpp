#include <bits/stdc++.h>
#include <iostream>

int n, b;

int value[33];
int cost[33];

int max_value = 0;
int max_cost = 0;
int v = 0;

void backtrack(int i)
{
    // std::cout<<i << " ";
    if(i > n)
    {
        if (max_value > v)
        {
            v = max_value;
        }
        return;
    }
    backtrack(i+1);
    if (max_cost + cost[i] <=b)
    {
        max_value += value[i];
        max_cost += cost[i];
      
        backtrack(i+1);
        max_value -= value[i];
        max_cost -= cost[i];
    } 

}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin >> n;
    std::cin >> b;

    for(int i = 0; i < n; i++)
    {
        std::cin >> cost[i];
        std::cin >> value[i];

    }
    backtrack(0);
    std::cout<<v;
    
    return 0;
}