#include <bits/stdc++.h>
using namespace std;
typedef void(*LP)();

void decrypt() {
	cout << "decrypt ready.";
	cout << "using easy way to decrypt.";



	labs;
}

void encrypt() {
	char wd, sp = 'p';
	int a;
	cout << "encrypt ready." << endl;
	cout << "using easy way to crypt.\nEnter the letter to crypt\n>>>";
	cin >> wd;
	a = sp;
	cout << sp;
	labs;
}

int main() {
	LP a[] = {decrypt, encrypt};
	int x = 0;
	cout << "encrypt demo program\n1=encrypt 0=decrypt\n>>>";
	x--;
	cin >> x;
	a[x]();
	return 0;
}
