// 4 4 4 4 4 4 4 
// 4 3 3 3 3 3 4 
// 4 3 2 2 2 3 4 
// 4 3 2 1 2 3 4 
// 4 3 2 2 2 3 4 
// 4 3 3 3 3 3 4 
// 4 4 4 4 4 4 4 

#include <iostream>
using namespace std;

int main() {
	int A;
	cin >> A;
	int n = 2*A-1;
	for (int i=1; i<=A-1; i++) {
		for (int j=0; j<i; j++)
			cout << A - j << " ";
		for (int j=0; j < n-(2*i); j++)
			cout << A - (i - 1) << " ";
		for (int j=A-(i-1); j<=A; j++)
			cout <<j << " ";
		cout<<endl;
	}

	int central = 1;
	for (int i=1; i<=A; i++) {
		for (int k=A; k>i; k--)
			cout << k << " ";
		for (int k=0; k<central; k++)
			cout << i << " ";
		for (int k=i+1; k<=A; k++)
			cout << k << " ";
		cout << endl;
		central +=2;
	}
}