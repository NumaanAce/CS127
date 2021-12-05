// Name: Numaan Qureshi
// Email : numaan.qureshi58@myhunter.cuny.edu
// My second program in C++

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    float i;
    cout << "Enter amount in cryptocurrency: " << endl;
    cin >> i;
    cout << fixed << setprecision(2);
    cout << i << " BTC iN USD (as of 07/16/21): $" << (i * 31901.19) << endl;
    cout << i << " ETH in USD (as of 07/16/21): $" << (i * 1901.54) << endl;
    cout << i << " DOGE iN USD (as of 07/16/21): $" << (i * 0.179733) << endl;
    return 0;
}