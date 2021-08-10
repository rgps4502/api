from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    if request.method == 'GET':
       # list = ['"smsc": "发件人",//string 15,',' "timestamp": "时间", //string 25','"text":"内容",//string 75', '"number":"收件人号码"//string 15']
         def re(request):
             print (request.form['name'])
         return HttpResponse(re)
 
    elif request.method == 'POST':
        return HttpResponse('hello') 
