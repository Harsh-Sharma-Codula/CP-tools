#include"bits/stdc++.h" 
using namespace std;
int main(int argc, char const *argv[])
{
	string file="g++ -std=c++17 ";
	file+=argv[1];
	file+=".cpp -o ";
	file+=argv[1];
	const char *command = file.c_str();
	system(command);
	cout<<"Compliation Finished\n";
	return 0;
}