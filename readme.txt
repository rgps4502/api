參考網址 https://github.com/twtrubiks/django-rest-framework-tutorial/tree/django2
版本不能低於
Django==2.2.1
djangorestframework==3.9.3

開新項目
django-admin startproject api

建立新的app 取名sms
python3 manage.py startapp sms

請在 api/settings.py 裡面的 INSTALLED_APPS 加入設定
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'rest_framework',
    'sms.apps.SmsConfig'
]

定義 models.py
就是api的內容


在命令提示字元 (cmd ) 底下輸入
python manage.py makemigrations sms
python manage.py migrate