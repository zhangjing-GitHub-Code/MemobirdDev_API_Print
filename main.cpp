#include<iostream>
#include<fstream>
using namespace std;
string getExeStr() {
	string _exe = "https://open.memobird.cn/home/printpaper?ak=";
	string ak,uid,devid;
	try{
		ifstream conf;
		conf.open("Memobird.ini");
		//getline(conf,ak);
		//getline(conf,uid);
		//getline(conf,devid);
		conf >> ak;
		conf >> uid;
		conf >> devid;
		conf.close();
	}catch(exception *){
		throw("config file wrong, please check your format!");
	}
	_exe += ak;
	_exe += "&userID=";
	_exe += uid;
	_exe += "&memobirdID=";
	_exe += devid;
	return _exe;
}
int main(){
	string webv=getExeStr();
	cout << webv;
	system("pause");
	return 0;
}