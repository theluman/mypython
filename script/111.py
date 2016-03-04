#!/user/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import urllib
import re

#小说章节类
class ZHANGJIE:
    #初始化传入地址
    def __init__(self,zjUrl,Num):
        self.zjUrl = zjUrl    
        self.Num = Num    
    
    #传入页码，获得网页源代码，只看精品
    def getPage(self):
        url = self.zjUrl + str(self.Num)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    #获取每章链接资源
    def getNum(self):
        webcon = self.getPage()
        Num = re.findall('<a href="/p/(\d+)"',webcon)
        print Num
        return Num

#每题内容类
class NEIRONG:
    #初始化，传入地址
    def __init__(self,nrUrl,Num):
        self.nrUrl = nrUrl
        self.Num = Num

    #传入资源页码，获得网页源代码,只看楼主
    def getPage(self):
        url = self.nrUrl + str(self.Num) + '?see_lz=1'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()
        
    #获取小说章节和标题
    def getTitle(self):
        webcon = self.getPage()
        title = re.search('style="width: 450px">(.*)</h1>',webcon).group(1)
        #print title
        return title

    #获得小说内容并打印换行
    def getCon(self):
        webcon = self.getPage()
        con = re.search('支持兰大，一定要记得投票哦！推荐票！(.*)(</div><br>)',webcon).group(1)
        con_n = re.sub('<br>','\n',con)
        return con_n

    #写入文件
    def writeDate(self):
        con_t = self.getTitle()
        con_n = self.getCon()
        with open('/tmp/yydlr.txt','w+') as f:
            f.write(con_t)
            f.write(con_n)

#NR = NEIRONG('http://tieba.baidu.com/p/',3453463389)
#NR.writeDate()
ZJ = ZHANGJIE('http://tieba.baidu.com/f/good?kw=%E9%98%B4%E9%98%B3%E4%BB%A3%E7%90%86%E4%BA%BA&ie=utf-8&cid=0&pn=',3050)
ZJ.getNum()
