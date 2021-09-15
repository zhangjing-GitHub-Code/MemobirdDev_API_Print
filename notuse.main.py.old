import time,os
def getExecStr(printstr):
    _exeStr="http://open.memobird.cn/home/printpaper?ak=";
    config=open("Memobird.ini",'r')
    #if config.read()=="":
    #    raise TypeError("config file empty!")
    ak=config.readline()
    _exeStr+=ak.strip('\n')
    _exeStr+="&memobirdID="
    try:
        memoID=config.readline()
        if not memoID: raise
        _exeStr+=memoID.strip('\n')
        _exeStr+="&useridentifying="
        Uident=config.readline()
        if not Uident: raise
        _exeStr+=Uident.strip('\n')
        _exeStr+="&timestamp="
        config.close()
    except:
        raise TypeError("config file not full!")
        config.close()
    timestr=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    _exeStr+=timestr
    os.system("echo \"{}\" >> print.txt".format(printstr))
    pribase=os.popen("base64 print.txt").read()
    os.system("rm print.txt")
    _exeStr+="&printcontent=T:"
    _exeStr+=pribase
    return _exeStr
print(getExecStr(input("print:")))
