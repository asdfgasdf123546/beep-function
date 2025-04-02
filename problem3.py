#include<iostream>
#include<Windows.h>
using namespace std;

void RandomBeeps(int num);

int main() {
	srand(time(NULL));
	int num;
	cout << "Choose a number" << endl;
	cin >> num;
	RandomBeeps(num);


	

	

	
}

void RandomBeeps(int num) {
	
	for (int i = 0; i < num; i++) {
		int x = rand() % 1000;
		int y = rand() % 500;
		Beep(x, y);
	}





}
