#include<iostream>
#include<fstream>
using namespace std;
string getExeStr() {
	string _exe = "https://open.memobird.cn/home/printpaper?ak=";
	ifstream conf("Memobird.ini");
	string ak,uid,devid;
	try{
		getline(conf,ak);
		getline(conf,uid);
		getline(conf,devid);
	}catch(exception){
		cerr << "config file wrong, please check your format!";
	}
	_exe += ak;
	_exe += "&userID=";
	_exe += uid;
	_exe += "&memobirdID=";
	_exe += devid;
	conf.close();
	return _exe;
}
int main(){
	string webv=getExeStr();
	system("pause");
	return 0;
}