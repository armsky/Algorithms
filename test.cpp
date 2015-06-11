#include <iostream>
#include <array>
#include <vector>

using namespace std;

void af(int g)
{
    g++;
    cout<<g;
}

int main()
{
    int g = 123;
    cout << g << endl;
    af(g);
    cout << g << endl;
    return 0;
}
