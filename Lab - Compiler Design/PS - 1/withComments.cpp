#include <iostream>
using namespace std;
// used instead of std:: everytime
/*
Add sum of two nos
and store in sum 
*/
int main() {
    int num1, num2, sum;
    cout << "Enter two integers: ";
    cin >> num1 >> num2; // input two integers from user
    sum = num1 + num2; // add the two numbers
    cout << "Sum: " << sum << endl; // output the sum
    return 0; // return 0 to indicate successful termination
}