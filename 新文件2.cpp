#include <bits/stdc++.h>
#include <fstream>
using namespace std;
char lev, a[10];
int grademain = 0;

int calc_num(int a) {
	switch (a) {
		case 'A':
			return 10;
			break;
		case 'B':
			return 6;
			break;
		case 'C':
			return 2;
			break;
		default:
			return 0;
	}
}

int main() {
	char a[9];
	ifstream fin("level.zmt");
	ofstream fout("grade.zmt");
	for (int i = 1; ; i++) {
		fin >> a[i];
		grademain += calc_num(a[i]);
		break;

	}
	fout << grademain;
	return 0;
}