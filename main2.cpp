#include <iostream>
#include<fstream>
#include <time.h>
#include <stdio.h>
#include <cstdio>
using namespace std;
string getExecStr(){
    string _exeStr="http://open.memobird.cn/home/printpaper?ak=";
    if (!(ifstream configF("MemoBird.ini"))){
        throw("No config file exists!");
    }
    if (!(string ak=config.getline())){
        throw("config file empty!");
    }
    _exeStr+=ak;
    _exeStr+="&memoID=";
    try {
        string memoID=config.getline();
        _exeStr+="&useridentifying=";
        string Uident=config.getline();
        _exeStr+="timestamp=";
    }catch{
        throw("config file not full!");
    }
    time_t tt = time(NULL);
    tm* t=localtime(&tt);
    string tStam=(t->tm_year + 1900)+"-"+(t->tm_mon + 1)+"-"+t->tm_mday+"%20"+t->tm_hour+":"+t->tm_min+":"+t->tm_sec;
}

int main()
{
    string exec=getExecStr();
    cout << "Hello world!" << endl;
    return 0;
}
