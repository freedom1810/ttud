#include <bits/stdc++.h>
#include <iostream>

#include <bits/stdc++.h>
#include <iostream>

int n, k;



int result = 1000000000;
int temp_cost = 0;
int src;
bool check;

void vetcan(int visited)
{
    if (visited == n)
    {
        
    }
}

int main()
{
    
    std::ios::sync_with_stdio(false);
    std::cin >> n;
    std::cin >> k;

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

}

