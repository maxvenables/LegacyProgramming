#include <iostream>
using namespace std;
 void print_nums()
 {
     for(int x = 0; x<1; x--)
     {
         int newnum = rand() % 10;
         cout << "\033[1;32m" << newnum << " ";
     }
 }
 int main()
 {
     print_nums();
 }