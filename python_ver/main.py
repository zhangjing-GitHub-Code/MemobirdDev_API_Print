#coding:utf-8
def getconf():
    exe="http://open.memobird.cn/home/printpaper?ak\\="
    ak=""
    uid=""
    devid=""
    try:
        fo=open("Memobird.ini")
        s=fo.read()
        s2=s.split("\n")
        ak=s2[0]
        devid=s2[1]
        uid=s2[2]
        #print(s2)
    except:
        raise RuntimeError("config file wrong, please check your format!")
    exe += ak
    exe += "\\&userID\\="
    exe += uid
    exe += "\\&memobirdID\\="
    exe += devid
    return exe


step_status="\033[32m[\033[34m*\033[32m]\033[0m "
error_status="\033[32m[\033[31m!\033[32m]\033[0m "

def main():
# The base64 encoding depends on linux command 'base64'
    unenc=input("\033[32m[\033[34m?\033[32m]\033[0m Enter what you want to print: ")
    import os,base64,json
    exe=getconf()
    #enced=os.popen("echo \"%s\" > preenc && base64 preenc&&rm preenc"%unenc).read()
    enced=base64.b64encode(unenc.encode('gbk'))
    exe+="\\&timestamp\\=2021-9-13%207:16:10"
    exe+="\\&printcontent\\=T:"+enced.decode()
    jso=os.popen("termux-dialog confirm -t \"Do you really want to print?\" -i \"1000 API calls per day and %s left\"").read()
    jso_st=json.loads(jso)
    if jso_st["text"]=="no":
        print(error_status+"Aborted.")
        exit(0)
    try:
        print("\033[32m[\033[34m*\033[32m] \033[0mRequesting print url...")
        json_s=os.popen("curl -fsS "+exe).read() 
        #'{"showapi_res_code":1,"showapi_res_error":"ok","result":2,"smartGuid":"25eccfd3cc4061dc","printcontentid":53576399}'
        st=json.loads(json_s)
        if st["showapi_res_code"]==1:
            print("\033[32m[\033[34m*\033[32m]\033[0m Print sucessfully!")
        else:
            print(error_status+"Some thing went wrong...",end=' ErrMsg:'+st["showapi_res_error"]+"\n")
            #print(st["showapi_res_error"]+"\n")
            exit(1)
    except:
        print(error_status+"Aborted.")
        exit()
    #print(st)
main()
