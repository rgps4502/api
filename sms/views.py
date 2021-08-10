from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    if request.method == 'GET':
       list = ['"smsc": "发件人",//string 15,',' "timestamp": "时间", //string 25','"text":"内容",//string 75', '"number":"收件人号码"//string 15']
       return HttpResponse(list)
    elif request.method == 'POST':
         def updateItem(request):
             print (request.headers)
             print (request.form)
             print (request.form['name'])
             print (request.form.get('name'))
             print (request.form.getlist('name'))
         return HttpResponse(updateItem(request))
