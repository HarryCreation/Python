from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Contact.models import *
# Create your views here.
import json
@csrf_exempt
def add_employee(request):
    try:
        if request.method == "POST":
            data =  json.loads(request.body)
            if Employees.objects.filter(name=data['name'],
                salary = data['salary'],
                join_date = data['join_date'],
                position = data['position'],
                user = User.objects.get(id=int(data['user']))).exists():
                return JsonResponse(data={'Sucess':False}, status=400)
            
            employee = Employees.objects.create(
                name=data['name'],
                salary = data['salary'],
                join_date = data['join_date'],
                position = data['position'],
                user = User.objects.get(id=int(data['user']))
            )
            employee.save()
        return JsonResponse(data={"Sucess":True}, status=201)
    except Exception as e:
        print(e)
        return JsonResponse(data={'Sucess': False}, status=500)

    