#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char const *argv[])
{
	int x=0;
	float y=0;
	cin >> x>>y;
	float rb = y - (x+0.50);
	
	if(x%5!=0 || x>y || rb<0){
		cout << fixed << setprecision(2) << y;
	}
	else{
		cout << fixed << setprecision(2) << rb;
	}
	return 0;
}
