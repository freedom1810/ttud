#include <bits/stdc++.h>
#include <iostream>

int m, n; // m số giáo viên, n số khóa học

int count_course[11] = {0};    // đêm xem mỗi giáo viên dạy bao nhiêu khóa
bool conflict[33][31] = {false}; // chekc xem các môn có bị confilct k 
bool courses[11][31] = {false}; //check xem giáo viên được dạy nhưng môn nào 
int result = 100000;
bool teachers[11][31] = {false}; // check xem giáo viên đang dạy những môn nào

bool check_conflict(int course, int teacher)
{
    for (int i = 1; i <= n; i++)
    {
        if (teachers[teacher][i])
        {
            if (conflict[i][course]) return true;
        }
    }
    return false;
}

void vetcan(int course)
{
    if (course > n)
    {
        int temp_result = -1;

        for (int i = 1; i <= m; i++)
        {
            if (temp_result < count_course[i]) 
            {
                temp_result = count_course[i];
            }
        }

        if (result > temp_result)
        {
            result = temp_result;
        }

        return ;
    }

    for (int i = 1;  i <= m; i++)
    {
        if (courses[i][course])
        {
            if (check_conflict(course, i)) continue;

            teachers[i][course] = true;
            count_course[i] += 1;

            bool check = false;
            for (int i = 1; i <= m; i++)
            {
                if (result < count_course[i]) 
                {
                    check = true;
                    break;
                }
            }
            if (check) 
            {
                teachers[i][course] = false;
                count_course[i] -= 1;
                continue;
            }

            vetcan(course + 1);

            teachers[i][course] = false;
            count_course[i] -= 1;
        }    
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin >> m;
    std::cin >> n;

    for (int i = 1; i <= m; i++)
    {   
        int c;
        std::cin >> c;
        for (int j = 0; j < c; j++)
        {
            int j_;
            std::cin >> j_; 
            courses[i][j_] = true;
        }
    }

    int con; 
    std::cin >> con;
    for (int i = 0; i < con; i++)
    {
        int c1, c2;
        std::cin >> c1;
        std::cin >> c2;

        conflict[c1][c2] = true;
        conflict[c2][c1] = true;
    }

    vetcan(1);

    std::cout<< result;
    // std::cout<< temp_result;

}