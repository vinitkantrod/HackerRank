#include <iostream>

using namespace std;

int main()
{
	char a[100][100];
	int i,j,x = 0;
	cin >> x;
	for(i=0;i<x;i++)
	{
		for(j=0;j<x;j++)
		{
			cin >>a[i][j];
		}
	}
	for(i=1;i<x-1;i++)
	{
		for(j=1;j<x-1;j++)
		{

			if((a[i][j] > a[i][j-1]) and (a[i][j] > a[i-1][j]) and (a[i][j] > a[i][j+1]) and (a[i][j] > a[i+1][j]))
			{
				a[i][j] = 'X';
			}
		}
	}
	for(i=0;i<x;i++)
	{
		for(j=0;j<x;j++)
		{
			cout <<a[i][j];
		}
		cout<<endl;
	}	
	return 0;
}