#include <iostream> 
#include <vector> 
#include <cmath>
using namespace std;

int main() 
{ 
    int n;
    cin >> n;
    if(n % 2 != 0 || n == 0) {
        cout << 0;
    }
    else {
        cout << pow(2,(n/2));
    }
}