from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from testapp.mixins import SerializeMixin,HttpResponseMixin

# Create your views here.
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not availble'})
            return self.render_to_http_response(json_data,status = 404)
        else:
            json_data=self.serialize([emp,])
            return self.render_to_http_response(json_data)

class EmployeeListCBV(SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')
