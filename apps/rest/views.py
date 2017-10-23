from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages

def index(request):
    response = "works"
    return HttpResponse(response)

def users(request):
    return render(request, 'rest/users.html', {'all_users': User.objects.all()})

def userinfo(request, user_id):
    return render(request, 'rest/info.html', {'user':User.objects.get(id=user_id)})

def new(request):
    return render(request, 'rest/newuser.html')

def create(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for error in erros.itervalues():
                messages.error(request, error)
            return redirect('/users/new')
        else:
            User.objects.create(first_name=request.POST['input_first_name'], last_name=request.POST['input_last_name'], email=request.POST['input_email'])
            return redirect('/users')

def edit(request, user_id):
    return render(request, 'rest/edit.html', {'user':User.objects.get(id=user_id)})
def update(request, user_id):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for error in erros.itervalues():
                messages.error(request, error)
            tem = '/users/' + user_id + '/edit'
            return redirect(tem)
        else:
            temp = User.objects.get(id=user_id)
            if request.POST['input_first_name']:
                temp.first_name = request.POST['input_first_name']
            if request.POST['input_last_name']:
                temp.last_name = request.POST['input_last_name']
            if request.POST['input_email']:
                temp.email = request.POST['input_email']
            temp.save()
            temp_url = '/users/' + user_id
    return redirect(temp_url)
def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')