#首先在编写时必须有一定的标准
#要求反应聊天内容并输出相关信息，因此函数参数应主要为字符串，为减少主程序端的代码量，将处理全部置于插件中其次是否需要协程
#返回值应为可以处理的图片类型、字符串等
#库的引用尽量不用缩写防止不同库产生的冲突
#api网站：https://www.juhe.cn/
import urllib.parse
import urllib.request
import sys
import json

NewsChannels = {'推荐':'top','国内':'guonei','国际':'guoji','娱乐':'yule','体育':'tiyu','军事':'junshi','科技':'keji','财经':'caijing',
                '时尚':'shishang','游戏':'youxi','汽车':'qiche','健康':'jiankang','帮助':0}
key = 'ab187693580c9c8330e8b7aea14404c6'
url = 'http://v.juhe.cn/toutiao/index'
NewsHelpDocs = "这里是帮助文档：\n目前支持的新闻类型包括：推荐、国内、国际、娱乐、体育、军事、科技、财经、时尚、游戏、汽车、健康\n使用方法：@我发送包含类型关键字的新闻即可。"

def News( include ):
    NewsString = ''
    for i in NewsChannels.keys():  #查找类别
        if i in include:
            type = NewsChannels[i]
            break
    try:                           #若文本内无类别，则进行判断
        if isinstance(type, int):
            NewsString = NewsHelpDocs
            return NewsString
        else:
            params = {'type':type,'key' : key,'page_size':5}
    except :
        params = {'type':'top','key' : key,'page_size':5}
    quarys = urllib.parse.urlencode(params) #获得请求包

    reque__ = urllib.request.Request(url,data = quarys.encode('utf-8')) #请求
    response = urllib.request.urlopen(reque__) #发送并接收
    content = response.read()
    if(content):
        try:
            result = json.loads(content)
            error_code = result['error_code']
            if (error_code == 0):
                data = result['result']['data']
                for i in data:
                    # 更多字段可参考接口文档
                    NewsString=NewsString +"新闻标题：%s\n新闻时间：%s\n新闻链接：%s\n\n" % (i['title'], i['date'], i['url'])
            else:
                NewsString=NewsString +"请求失败:%s %s" % (result['error_code'], result['reason'])
        except Exception as e:
            NewsString=NewsString +"解析结果异常：%s" % e
    return NewsString



