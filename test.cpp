#Usage:
#	test <number-of-io(input,output)-files>



#include"bits/stdc++.h"

using namespace std;
#define fast ios_base::sync_with_stdio(false);cin.tie(nullptr)
#define i64 int64_t
#define deb(x) cout<<"["<<#x<<"="<<x<<"]"<<"\n"
#define pb push_back
int to_int(string s){ int cu=0; for(auto i:s){ cu=10*cu+(i-'0');} return cu;}

int main(int argc,char *argv[])
{
	string numb(argv[1]);
	cout<<"bcpp sol\n\n";
	system("bcpp sol");
	for(int i=1;i<to_int(numb)+1;++i)
	{
		string file="sol<in";
		file+=to_string(i);
		file+=">res";
		file+=to_string(i);
		cout<<"\n"<<file<<"\n\n";
		const char *command = file.c_str();
		system(command);
		string comm="fc res";
		comm+=to_string(i);
		comm+=" out";
		comm+=to_string(i);
		cout<<comm<<"\n";
		const char *command1 = comm.c_str();
		system(command1);
	}
	return 0;
}
