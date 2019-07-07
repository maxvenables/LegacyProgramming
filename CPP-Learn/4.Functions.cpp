#include <iostream>
using namespace std;
 void hello() // returns no value
 {
     cout << "hello world" << endl;
 }
 int returnNumber() // returns a number
 {
     return 5;
 }

 int main()
 {
     hello();
     int x = returnNumber();
     cout << x << endl;
 
     return 0;
 }