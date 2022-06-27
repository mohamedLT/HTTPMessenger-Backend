from django.http import HttpResponse,JsonResponse
from django.utils.timezone import make_aware
from django.core.serializers.json import DjangoJSONEncoder
import pprint
import datetime
from .models import *
import json






def get_list(request):
    return JsonResponse(list(user.objects.values()),safe=False)

def get_active(request):
    return JsonResponse(list(user.objects.filter(active=True).values()),safe=False)


def add_message(request):
    msg_keys = ["time","sender","content","users"]
    data =json.loads(request.body.decode("utf-8"))
    has_keys = all(key in data for key in msg_keys)
    if has_keys:
        print(data["users"])
        sender = user.objects.get(user_name__exact=data["sender"])
        viewers = list(user.objects.filter(user_name__in=data["users"]))
        time = datetime.datetime.strptime(data["time"],'%d/%m/%Y %H:%M')
        msg= Message.objects.create(sender=sender,content=data["content"],time=make_aware(time))
        for i in range(len(viewers)):
            msg.users.add(viewers[i])
        return JsonResponse({"value":True},safe=False)
    else:
        return JsonResponse({"value":False},safe=False)

def add_user(req):
    keys = ["full_name","user_name","password"]
    data =json.loads(req.body.decode("utf-8"))
    print(data)
    has_keys = all(key in data for key in keys)
    if has_keys:
        user_name = data["user_name"]
        full_name = data["full_name"]
        password = data["password"]
        if not user.objects.filter(user_name=user_name).exists():
            user.objects.create(full_name=full_name,user_name=user_name,password=password)
            return JsonResponse({"value":True,"reason":""},safe=False)
        else :
            return JsonResponse({"value":False,"reason":"user name already used"},safe=False)
    else :
        return JsonResponse({"value":False,"reason":"uncorrect data"},safe=False)




def check_user(req):
    keys = ["user_name","password"]
    data =json.loads(req.body.decode("utf-8"))
    has_keys = all(key in data for key in keys)
    if has_keys :
        us = user.objects.get(user_name=data["user_name"])
        if not user.objects.filter(user_name=data["user_name"]).exists():
            return JsonResponse({"value":False,"reason":"user name does not exist"},safe=False)
        if us.password==data["password"]:
            print("true")
            return JsonResponse({"value":True},safe=False)
        else :
            print("false")
            return JsonResponse({"value":False,"reason":"wrond password"},safe=False)
    else :
        print("false")
    
        return JsonResponse({"value":False,"reason":"uncorrect data"},safe=False)


        
    


def fetch_msgs(req):
    
    keys = ["users"]
    data =json.loads(req.body.decode("utf-8"))
    has_keys = all(key in data for key in keys)
    if has_keys :
        al = Message.objects.all()
        #pprint.pprint(al)
        #print(al)
        s = [msg_model2dict(x) for x in al]
        filtred = [msg for msg in s if all( name in data["users"] for name in msg["users"] )]
        result = [] 
        [result.append(x) for x in filtred if x not in result] 
        print(result)
        
    return JsonResponse(result,safe=False,encoder=DjangoJSONEncoder)


def msg_model2dict(msg:Message):
    res = {}
    res["time"]=msg.time.strftime('%d/%m/%Y %H:%M')
    res["content"]=msg.content
    res["sender"]=msg.sender.user_name
    res["users"]=[x.user_name for x in msg.users.all()]
    return res



