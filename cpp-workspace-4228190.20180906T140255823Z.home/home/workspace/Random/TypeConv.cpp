#include <iostream>
using namespace std;
string find(int num)
{
    string fe;
    if (num == 2)
    {
        fe = "hey";
    }
    else
    {
        fe = to_string(num); // 
    }
    return fe;
}
 int main()
 {
     int NUM = 2;
     string answer = find(NUM);
     cout << answer;
 }