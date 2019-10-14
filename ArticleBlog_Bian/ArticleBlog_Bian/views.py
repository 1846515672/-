# 导包
from django.http import HttpResponse
import time
# def index(request):
#     return HttpResponse('hello word')

def say_hello(request,name,age):
    string = "<h1 style='color:green;'>人生苦短,我用python,%s,%s</h1>"%(name,age)
    return HttpResponse(string)

def Birth_day(request, month, day):
    # 设置时间格式
    birthday = time.mktime((2019, int(month), int(day), 0, 0, 0, 0, 0, 0))
    dayth = time.localtime(birthday).tm_yday
    # 创建httml页面格式
    html_1 = """
    <!DOCTYPE html>
    <html lang='en'>
        <head>
            <meta charset=UTF-8>
            <title>生日</title>
            <style>
                .content{
                color:origin;
                text-align:center;
            }
            </style>
        </head>
        <body>
            <h1 align='center'>我的生日是今年的第几天?</h1>
            <p class='content'>%s</p>
        </body>
    </html>
           """
    string = "我的生日:%s月%s日,是今年的第%s天"%(month, day, dayth)
   # 连接httml_1
    return HttpResponse(html_1%string)


def cf_table(request):
    html_1 = """<!DOCTYPE html>
              <html lang='en'>
              <head>
              <meta charset='UTF-8'>
              </head>
              <body>
              <table align=center style="border:solid 0px ;">
           """
    for i in range(1, 10):
        html_1 += '<tr>'
        for j in range(1, i+1):
            html_1 += '<td>'
            html_1 += '{} x {} = {} &nbsp'.format(i, j, j*i)
            html_1 += '</td>'
        html_1 += '</tr>'
    html_1 += '''
    </table>
    </body>
    </html>
    '''
    return HttpResponse(html_1)

def timer(request):
    # 当前时间
    t1 = time.time()
    html_2 = """
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset=UTF-8>
        <title>时间倒计时</title>
    </head>
    <body>
    <script>
    
    """