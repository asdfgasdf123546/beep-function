#include<iostream>
#include<Windows.h>
using namespace std;

int main() {

	int choice;
	cout << "how many notes should we play?" << endl;
	cin >> choice;
	for (int i = 0; i < choice; i++)
		Beep(1000+i*200, 200);


	

	

	
}
