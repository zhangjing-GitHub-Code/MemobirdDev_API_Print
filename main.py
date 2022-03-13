#coding:utf-8
import getopt,sys,time,os.path
import os,base64,json

step_status="\033[32m[\033[34m*\033[32m]\033[0m "
error_status="\033[32m[\033[31m!\033[32m]\033[0m "

try:
    import requests
except:
    print(error_status+"library `request' is needed for printing.\n"+step_status+"Downloading...")
    os.system("python -m install requests -i https://pypi.tuna.tsinghua.edu.cn/simple")
global config,printstr,isunix
isunix=0
config="Memobird.ini"
helpdoc=""" usage: python %s [options]\n
 options are:\n
    -h,--help \t\t\tshow this help.
    -c,--config,--config-file\tset the cofig file.
    -s,--printstr \t\tprint specified string.
    -f,--file,--print-file\tprint from file.\n
 For more introductions, please see github or readme.
"""%sys.argv[0]
def reqUrl(url):
    try:
        print("\033[32m[\033[34m*\033[32m] \033[0mRequesting print url...")
        r=requests.get(url)
        #json_s=os.popen("curl -fsS \""+exe+"\"").read() 
        st=json.loads(r.text)
        if st["showapi_res_code"]==1:
            print("\033[32m[\033[34m*\033[32m]\033[0m Print sucessfully!")
        else:
            print(error_status+"Some thing went wrong...",end=' ErrMsg:'+st["showapi_res_error"]+"\n")
            #print(st["showapi_res_error"]+"\n")
            exit(1)
    except Exception as e:
        print(error_status+"Aborted by:")
        raise e
        exit()

def readfile(fname):
    fo=open(fname)
    return fo.read()
def getconf(config="Memobird.ini"):
    exe="http://open.memobird.cn/home/printpaper?ak="
    ak=""
    uid=""
    devid=""
    try:
        fo=open(config)
        s=fo.read()
        s2=s.split("\n")
        ak=s2[0]
        devid=s2[1]
        uid=s2[2]
        if s=="":
            raise TypeError
        #print(s2)
    except:
        print(error_status+"config file wrong, please check your format!")
        exit()
    exe += ak
    exe += "&userID="
    exe += uid
    exe += "&memobirdID="
    exe += devid
    return exe

def main(needstr=0,printstr=""):
    global config
# ~The base64 encoding depends on linux command 'base64'~
# I'm f**ker because python has encode and base64 lib
    exe=getconf(config)
    if not needstr:
        unenc=input("\033[32m[\033[34m?\033[32m]\033[0m Enter what you want to print: ")
    elif needstr==2:
        unenc=readfile(printstr)
    else:
        unenc=printstr
    #enced=os.popen("echo \"%s\" > preenc && base64 preenc&&rm preenc"%unenc).read()
    enced=base64.b64encode(unenc.encode('gbk'))
    exe+="&timestamp="+time.strftime("%Y-%m-%d%{}%H:%M:%S".format("%20"),time.localtime())
    exe+="&printcontent=T:"+enced.decode()
    print(exe)
    if os.path.exists("/data/data/com.termux/files/usr/libexec/termux-api"):
        jso=os.popen("termux-dialog confirm -t \"Do you really want to print?\" -i \"1000 API calls per day and %s left\"").read()
        jso_st=json.loads(jso)
        if jso_st["text"]=="no":
            print(error_status+"Aborted.")
            exit(0)
    else:
        flag=input("Do you really want to print?(y/n)")
        if flag not in ("y","Y"):
            print(error_status+"Aborted.")
            exit(0)
        #print(st)
    # Print now~~
    reqUrl(exe)

if __name__=="__main__":
    shortargs = 'f:c:s:h'
    longargs = ['print-file=','file=','help','printstr='] 
    try:
        opts,argv=getopt.getopt(sys.argv[1:],shortargs,longargs)
        #print(opts)
        if opts==[] and sys.argv[1]!='':
            print(helpdoc)
            exit()
        if opts==[]:
            raise TypeError
        ned=0
        stri=""
        for o,a in opts:
        #print(o,a)
        #print(opts)
            if o in ('-f','--file','--print-file'):
            #prints=read(a)
            #print(o,a)
                ned=2
                stri=a
            #cprint(arg)
            if o in ('--config','--config-file','-c'):
            #global config
                config=a
            if o in ('-s','--printstr'):
                ned=1
                stri=a
            elif o in ('-h','--help'):
                print(helpdoc)
                exit()
        main(ned,stri)
    except (getopt.GetoptError,TypeError):
        print("\033[32m[\033[34m*\033[32m] \033[0mNo opts detected, using interactive mode.")
        main()
