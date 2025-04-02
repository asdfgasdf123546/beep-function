#include<iostream>
#include<Windows.h>
using namespace std;

int main() {

	int choice;
	cout << "type 1 for a low note, 2 for a medium note, and 3 for a high note" << endl;
	cin >> choice;
	if (choice == 1)
		Beep(100, 50);
	else if (choice == 2)
		Beep(500, 50);
	else if (choice == 3)
		Beep(1000, 50);
	else
		cout << "Incorrect input.";

	
}
