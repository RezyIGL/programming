#include <iostream>
using namespace std;

int intSum(int a, int b) {
    return a + b;
}

int main()
{
    cout << "Hello, World!\n";

    int a = 0;
    int b = 0;

    cout << "Please, enter ur 1st num:\n";
    cin << "Enter a number: " << a;
    cout << "Same with 2nd:\n";
    cin >> b;

    cout << "Your sum is: " << intSum(a, b);

    return 0;
}
