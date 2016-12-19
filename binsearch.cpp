#include <algorithm>
using namespace std;

int main() {
	int a[] = {2,3,12,34,36,54,29,8,17};
	vector <int> arr (a, a+sizeof(a) / sizeof(int));
	for(int i=0; i<a.size(); i++)
		cout<<a[i]<<" ";
	cout<<endl;
	sort(a.begin(), a.end());
	for(int i=0; i<a.size(); i++)
		cout<<a[i]<<" ";
	cout<<endl;
}