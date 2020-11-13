// #include <stdio.h>
#include <bits/stdc++.h>
#include <iostream>

// #include<cstdlib> 
// #include<cstdio> 

typedef struct point
{
	int x;
    int y;
}custom_point;


int main()
{
    std::ios::sync_with_stdio(false);
    int t = 0;
    std::cin >> t;
    
    for(int i = 0; i < t; i++)
    {
        int l = 0;
        int c = 0;

        int res = 0;
        std::unordered_map<std::string, int> dict_res;

        std::string s;

        std::cin >> l;
        std::cin >> c;

        // load map1
        int map1[l][c];
        std::vector<custom_point> list_nghi_ngo;
            
        for(int index_l = 0; index_l < l; index_l++)
        {
            for(int index_c = 0; index_c < c; index_c++)
            {
                std::cin >> map1[index_l][index_c];

                
                if(map1[index_l][index_c] == 1)
                {
                    custom_point p;
                    p.x = index_l;
                    p.y = index_c;
                    list_nghi_ngo.push_back(p);
                }
            }
        }

        // load map2
        int map2[l][c];
        std::vector<custom_point> list_nghi_ngo2;
        
        for(int index_l = 0; index_l < l; index_l++)
        {
            for(int index_c = 0; index_c < c; index_c++)
            {
                std::cin >> map2[index_l][index_c];

                if(map2[index_l][index_c] == 1)
                {
                    custom_point p;
                    p.x = index_l;
                    p.y = index_c;
                    list_nghi_ngo2.push_back(p);
                }
            }
        }

        // for (auto p1: list_nghi_ngo) 
        for(auto p1 = list_nghi_ngo.begin(); p1 != list_nghi_ngo.end(); p1++)
        {
            // for (auto p2: list_nghi_ngo2)
            for(auto p2 = list_nghi_ngo2.begin(); p2 != list_nghi_ngo2.end(); p2++)
            {
                // s = std::to_string(p1.x - p2.x) + "_" + std::to_string(p1.y - p2.y);
                s = std::to_string(p1->x - p2->x) + "_" + std::to_string(p1->y - p2->y);
                if (dict_res.find(s) == dict_res.end())
                {
                    dict_res[s] = 1;
                }
                else
                {
                    dict_res[s] += 1;
                }
            }
        }

        // for (auto x : dict_res) 
        // {
        //     if (res < x.second) res = x.second;
        // }

        for (auto x = dict_res.begin(); x != dict_res.end(); x++) 
        {
            if (res < x->second) res = x->second;
        }

        if(res > 0)
        {
            std::cout<< res <<"\n";
        }
        else
        {
            std::cout<< -1 << "\n";
        }
    }

    return 0;
}