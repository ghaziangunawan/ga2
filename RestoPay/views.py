from django.shortcuts import render

# Create your views here.


def show_restopay(request):
    context = {"username": str(request.user).upper(),"user_id" : request.user.id}   
    return render(request, 'restopay.html',context)

def show_withdraw(request):
    context = {"username": str(request.user).upper(),"user_id" : request.user.id}   
    return render(request, 'withdraw.html',context)