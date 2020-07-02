# -*- coding:UTF-8 -*-

# Create by bakashigure in 2020.3.19 | Python3.7.3 64-bit |
# Last modified in 2020.7.2
# twitter @bakashigure
# wtfpl :)

import urllib.request
import re
import os



os.system("title 检测玩家5E历史对局中已经被封号的废物     CompileTime-2020.6.25    Auther-bakashigure")


normal_user_cheat = r'\
<a class="name" target="_blank" href="(.*)">\
<img class="vam" src="(?:.*)" alt="(?:.*)" width="24" height="24">\
<span class="(?:.*)">(.*)</span>\
</a>\
<span class="ban-type ban-type4-simplified-chinese"></span>\
'

vip_user_cheat = r'\
<a class="name" target="_blank" href="(.*)">\
<img class="vam" src="(?:.*)" alt="(?:.*)" width="24" height="24">\
(?:.*)\
(?:.*)\
(?:.*)\
(?:.*)\
<span class="(?:.*)">(.*)</span>\
</a>\
<span class="ban-type ban-type4-simplified-chinese"></span>\
'


class Player:
    def __init__(self):
        self.url='' # user`s 5e url.
        self.id='' # user`s id,match by regular expression.
        self.year=2020 # default set year to 2020.
    
    def playerAuth(self):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        sheaders={
            'User-Agent':user_agent
        } # set user agent 
        
        try:
            self.url = input("输入待检测用户的完整主页,如(https://www.5ewin.com/data/player/sb):")
            self.id = re.match(r'https://www.5ewin.com/data/player/(.*)', self.url)
            self.id = self.id[1]
        except:
            print("用户主页链接不正确，请输入正确的链接")
            return '-1'

        try:
            req=urllib.request.Request(self.url,headers=sheaders)
            resp=urllib.request.urlopen(req)
            self.year = re.match(r'^\d{4}$',input("输入检测年份:2019/2020 :"))[0] # actually if u input some strange number, such as 1145,website will change it to 2020
        except urllib.request.HTTPError as urlE:
            print("在试图打开用户主页时发生错误，错误为",urlE.code,urlE.reason," 请自行检查")
            return '-1'
        except TypeError as yearE:
            print("年份输入不正确",yearE.args)
            return '-1'
        except:
            print("奇怪的错误发生了！")
        return 



def main():
    victim = Player()
    while( victim.playerAuth()=='-1'):
        temp=input("键入回车以重新运行程序")
        os.system("cls")
        
    else:
        global demoCount
        demoCount = 0
        global demoList
        demoList = []
        matchList = []
        for i in range(0, 114514):
            matchList.append("https://www.5ewin.com/api/data/match_list/" +
                            victim.id+"?yyyy="+victim.year+"&page="+str(i+1)) 
            html = urllib.request.urlopen(matchList[i]).read()
            result = re.search(r'"success":true,', html.decode('utf-8'))
            if(result):
                print(result[0])
                demoList.append(re.findall(
                    r'"match_code":"((g([0-9]*)-c-)?([0-9]*))"', html.decode('utf-8')))
                demoCount = i*10+len(demoList[i])
            else:
                break
        os.system("cls")
        print("共找到"+str(demoCount)+"条demo，正在检测对局中已被封号的废物")

        for i in range(0, int(demoCount/10)+1):
            nt = 10
            if(i == int(demoCount/10)):
                nt = (demoCount % 10)
            for j in range(0, nt):
                matchurl = 'https://www.5ewin.com/data/match/'+demoList[i][j][0]
                matchhtml = urllib.request.urlopen(matchurl).read()
                conTitle = str(i*10+j+1)+"/"+str(demoCount)+" "+str(matchurl)  #console title
                sb = "title"+" "+str(conTitle)
                os.system(sb)
                cheat = re.findall(vip_user_cheat, matchhtml.decode('utf-8'))
                if(cheat):
                    cheatListLen = len(cheat)
                    for sb in range(cheatListLen):
                        print("废物: "+str(cheat[sb-1][1])+"\n\
5e主页: "+str(cheat[sb-1][0]))
                        print("对局："+matchurl+"\n")

                cheat = re.findall(normal_user_cheat, matchhtml.decode('utf-8'))
                if(cheat):
                    cheatListLen = len(cheat)
                    for sb in range(cheatListLen):
                        print("废物: "+str(cheat[sb-1][1])+"\n\
5e主页: "+str(cheat[sb-1][0]))
                        print("对局："+matchurl+"\n")

if __name__ == "__main__":
    main()
