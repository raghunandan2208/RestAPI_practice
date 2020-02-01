from django.shortcuts import render
import requests
# Create your views here.
def get_geographic_info(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')
    # url = 'http://api.ipstack.com/'+str(ip)+'?access_key=bd56c5f352b67d796130bb8bce43d7b3'
    url = 'http://api.ipstack.com/203.187.233.11?access_key=bd56c5f352b67d796130bb8bce43d7b3'
    response = requests.get(url)
    data = response.json()
    return render(request,'testapp/info.html',data)
