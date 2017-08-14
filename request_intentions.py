#!/usr/bin/env python
# encoding: utf-8
'''
* liangchaob@163.com 
* 2017.7
'''
#设置中文字符
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


import requests
from lxml import etree 
import json


import HTMLParser


parser = HTMLParser.HTMLParser()


#浏览器 header
# 设置 header
headers = {
    'cache-control': "no-cache",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }



# 获取该页超链接
def get_categories(current_url):
    r = requests.request("GET", current_url, headers=headers)
    e_html = etree.HTML(r.text)
    link_list = e_html.xpath('//a[@class="article_title__txt left"]/@href')
    return link_list



# 获取当前文章内容和标题
def get_articles(current_url):
    r = requests.request("GET", 'http://cv.qiaobutang.com'+current_url, headers=headers)
    e_html = etree.HTML(r.text)
    page_title = e_html.xpath('//div[@class="article__title"]/h1/text()')
    page_title =  page_title[0]
    # print page_title


    page_content=e_html.xpath('//div[@class="article__body"]')
    page_content = etree.tostring(page_content[0])
    page_content = parser.unescape(page_content)

    # print page_content

    json_obj = {
      'title': page_title,
      'content': page_content
    }

    return json_obj






# 获取 categories 下全部超链接
def main():
    total_link_list = []
    for i in xrange(0,50,10):
        current_list = get_categories(current_url = 'http://cv.qiaobutang.com/knowledge/intentions?skip='+str(i))
        total_link_list.extend(current_list)

        # 进度条
        sys.stdout.write(str(i) +'/560 链接已获取! \r')
        sys.stdout.flush()



    article_list = [] 
    link_length = len(total_link_list)
    g = 0
    for link in total_link_list:
        # 进度条
        sys.stdout.write(str(g) +'/560 页面已获取! \r')
        sys.stdout.flush()
        g = g+1

        article_obj = get_articles(link)
        jsonStr = json.dumps(article_obj, sort_keys=True, indent=2) 

        with open('intentions_articles.json','a') as wf:
            wf.write(jsonStr+',\n')

    print 'down!'





if __name__ == '__main__':
    main()



