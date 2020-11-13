#include <bits/stdc++.h>
#include <iostream>

int n, m;
int x, y;
int result;
int map[20][20] = {0};
bool visited[20][20] = {true};

void backtrack(int temp_res, int count)
{
    if (count == n)
    {
        if (true)
        {

        }
        if (result > temp_res) result = temp_res;
        return 
    }
}
int main()
{
    
    std::ios::sync_with_stdio(false);
    std::cin >> n;
    std::cin >> m;

    for (int i = 0; i< n; i++)
    {
        std::cin>> x;
        std::cin>> y;
        std::cin>> map[x-1][y-1];
        visited[x-1][y-1] = false;
    }




    std::cout<<result;
    return 0;

}